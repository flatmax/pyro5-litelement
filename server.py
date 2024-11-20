import Pyro5.api
import Pyro5.nameserver
import threading
from remote_object import RemoteControl

def run_nameserver():
    # Start the name server
    Pyro5.nameserver.start_ns_loop()

def run_daemon():
    # Create and configure the daemon
    daemon = Pyro5.server.Daemon()
    
    # Locate the name server
    ns = Pyro5.api.locate_ns()
    
    # Create and register the remote object
    remote_control = RemoteControl()
    uri = daemon.register(remote_control)
    
    # Register with the name server
    ns.register("example.remote_control", uri)
    
    print(f"Remote control registered as: example.remote_control")
    print("Server is running. Ctrl-C to exit.")
    
    # Start the daemon's request loop
    daemon.requestLoop()

def main():
    try:
        # Create threads for name server and daemon
        nameserver_thread = threading.Thread(target=run_nameserver)
        daemon_thread = threading.Thread(target=run_daemon)

        # Start the threads
        nameserver_thread.start()
        # Give the name server a moment to start
        import time
        time.sleep(2)
        daemon_thread.start()

        # Join the threads to keep them running
        nameserver_thread.join()
        daemon_thread.join()
        
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
