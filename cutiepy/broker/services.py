from cutiepy.eventlogs import EventLog
from datetime import datetime, timezone
from pydantic.dataclasses import dataclass
from typing import Optional
import uuid

def build_broker_service(event_log: EventLog):
    return BrokerService(event_log=event_log)


@dataclass
class BrokerService:
    event_log: EventLog

    def create_task(self, task_id: Optional[str], function_serialized: str) -> dict:
        if task_id is not None and self._task_exists(task_id=task_id):
            raise RuntimeError(f"Task with ID {task_id} already exists.")

        event = {
            "timestamp": datetime.isoformat((datetime.now(timezone.utc))),
            "event_type": "CREATE_TASK",
            "task_id": task_id or str(uuid.uuid4()),
            "function_serialized": function_serialized,
        }
        self.event_log.append(event)
        return event

    def tasks(self) -> list[dict]:
        events = self.event_log.events()
        events = filter(lambda event: "task_id" in event, events)
        events = sorted(events, key=lambda event: event["timestamp"])
        tasks = {}
        for event in events:
            match event["event_type"]:
                case "CREATE_TASK":
                    task_id = event["task_id"]
                    tasks[task_id] = {
                        "created_at": event["timestamp"],
                        "task_id": event["task_id"],
                        "function_serialized": event["function_serialized"],
                    }
                case _event_type:
                    raise RuntimeError(f"Unexpected task event type: {_event_type}")

        return list(tasks.values())


    def _task_exists(self, task_id: str) -> bool:
        events = self.event_log.events()
        events = filter(lambda event: event.event_type == "CREATED_TASK", events)
        return any(map(lambda event: event.task_id == task_id, events))
