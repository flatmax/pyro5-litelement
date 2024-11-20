import Pyro5.api
from remote_object import RemoteControl

def main():
    # Create the Pyro daemon
    daemon = Pyro5.api.Daemon()

    # Create the remote object
    remote_control = RemoteControl()

    # Register the object with Pyro
    uri = daemon.register(remote_control)

    # Print the URI so clients can use it
    print(f"Object URI: {uri}")

    # Start the event loop
    print("Server is running. Ctrl-C to exit.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
