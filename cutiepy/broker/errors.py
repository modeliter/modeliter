class TaskAlreadyExistsError(Exception):
    def __init__(self, task_id: str) -> None:
        message = f"Task with ID {task_id} alreeady exists."
        return super().__init__(message)

class WorkerDroppedError(Exception):
    def __init__(self, worker_id: str) -> None:
        message = f"Worker with ID {worker_id} has been dropped."
        return super().__init__(message)

class WorkerAlreadyRegisteredError(Exception):
    def __init__(self, worker_id: str) -> None:
        message = f"Worker with ID {worker_id} has already been registered."
        return super().__init__(message)

class WorkerNotRegisteredError(Exception):
    def __init__(self, worker_id: str) -> None:
        message = f"Worker with ID {worker_id} is not registered."
        return super().__init__(message)
