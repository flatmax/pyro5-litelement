import Pyro5.api

@Pyro5.api.expose
class RemoteControl:
    def __init__(self):
        self._status = "idle"
        self._value = 0

    def set_value(self, value):
        self._value = value
        return f"Value set to {self._value}"

    def get_value(self):
        return self._value

    def get_status(self):
        return self._status

    def start(self):
        self._status = "running"
        return "System started"

    def stop(self):
        self._status = "stopped"
        return "System stopped"
