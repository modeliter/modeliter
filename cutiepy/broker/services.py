from cutiepy.eventlogs import EventLog
from datetime import datetime, timezone
from pydantic.dataclasses import dataclass
from typing import Optional
import uuid

@dataclass
class BrokerService:
    event_log: EventLog

    ##############
    ## Commands ##
    ##############

    def create_task(self, task_id: Optional[str], function_serialized: str) -> dict:
        if task_id is not None and self._task_exists(task_id=task_id):
            raise RuntimeError(f"Task with ID {task_id} already exists.")

        event = {
            "timestamp": datetime.isoformat((datetime.now(timezone.utc))),
            "event_type": "CREATED_TASK",
            "task_id": task_id or str(uuid.uuid4()),
            "function_serialized": function_serialized,
        }
        self.event_log.append(event)
        return self.task(task_id=task_id)

    def register_worker(self, worker_id: str) -> dict:
        if self._worker_is_registered(worker_id=worker_id):
            raise RuntimeError(f"Worker with ID {worker_id} already exists.")

        event = {
            "timestamp": datetime.isoformat(datetime.now(timezone.utc)),
            "event_type": "REGISTERED_WORKER",
            "worker_id": worker_id,
        }
        self.event_log.append(event)
        return self.worker(worker_id=worker_id)

    def send_worker_heartbeat(self, worker_id: str) -> dict:
        if not self._worker_is_alive(worker_id=worker_id):
            raise RuntimeError(f"Worker with ID {worker_id} is not alive.")

        event = {
            "timestamp": datetime.isoformat(datetime.now(timezone.utc)),
            "event_type": "SENT_WORKER_HEARTBEAT",
            "worker_id": worker_id,
        }
        self.event_log.append(event)
        return self.worker(worker_id=worker_id)

    #############
    ## Queries ##
    #############

    def task(self, task_id: str) -> Optional[dict]:
        tasks = self.tasks()
        for task in tasks:
            if task["task_id"] == task_id:
                return task
        return None

    def tasks(self) -> list[dict]:
        events = self.event_log.events()
        events = filter(lambda event: "task_id" in event, events)

        tasks_dict = {}
        for event in events:
            match event["event_type"]:
                case "CREATED_TASK":
                    task_id = event["task_id"]
                    tasks_dict[task_id] = {
                        "created_at": event["timestamp"],
                        "task_id": event["task_id"],
                        "function_serialized": event["function_serialized"],
                        "status": "WAITING",
                    }
                case _event_type:
                    raise RuntimeError(f"Unexpected task event type: {_event_type}")

        return list(tasks_dict.values())

    def worker(self, worker_id: str) -> Optional[dict]:
        workers = self.workers()
        for worker in workers:
            if worker["worker_id"] == worker_id:
                return worker
        return None

    def workers(self) -> list[dict]:
        events = self.event_log.events()
        events = filter(lambda event: "worker_id" in event, events)

        workers_dict = {}
        for event in events:
            match event["event_type"]:
                case "REGISTERED_WORKER":
                    worker_id = event["worker_id"]
                    workers_dict[worker_id] = {
                        "registered_at": event["timestamp"],
                        "worker_id": event["worker_id"],
                        "status": "AVAILABLE",
                    }
                case "SENT_WORKER_HEARTBEAT":
                    worker_id = event["worker_id"]
                    worker = workers_dict[worker_id]
                    worker["last_heartbeat_timestamp"] = event["timestamp"]
                    workers_dict[worker_id] = worker
                case _event_type:
                    raise RuntimeError(f"Unexpected worker event type: {_event_type}")
        
        return list(workers_dict.values())

    ######################
    ## Helper Functions ##
    ######################

    def _task_exists(self, task_id: str) -> bool:
        task = self.task(task_id=task_id)
        return task is not None

    def _worker_is_alive(self, worker_id: str) -> bool:
        worker = self.worker(worker_id)
        if worker is None:
            return False
        return worker["status"] != "DROPPED"

    def _worker_is_dropped(self, worker_id: str) -> bool:
        worker = self.worker(worker_id)
        if worker is None:
            return False
        return worker["status"] == "DROPPED"

    def _worker_is_registered(self, worker_id: str) -> bool:
        worker = self.worker(worker_id)
        return worker is not None

def build_broker_service(event_log: EventLog) -> BrokerService:
    return BrokerService(event_log=event_log)
