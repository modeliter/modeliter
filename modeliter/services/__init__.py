class ServiceResult:
    def __init__(self, arg):
        if isinstance(arg, Exception):
            self.success = False
            self.exception = arg
