import subprocess
import sys
import time
import signal
import os

def signal_handler(sig, frame):
    print("\nShutting down services...")
    for process in processes:
        if process.poll() is None:  # if process is still running
            process.terminate()
            try:
                process.wait(timeout=5)  # wait up to 5 seconds for graceful shutdown
            except subprocess.TimeoutExpired:
                process.kill()  # force kill if it doesn't shut down gracefully
    sys.exit(0)

# Register signal handler for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)

# List to keep track of all processes
processes = []

def main():
    # Start the Pyro server
    print("Starting Pyro server...")
    server_process = subprocess.Popen([sys.executable, "server.py"],
                                    bufsize=1,  # Line buffered
                                    text=True,  # Use text mode instead of binary
                                    stdout=None,  # Use parent's stdout
                                    stderr=None)  # Use parent's stderr
    processes.append(server_process)

    # Give the server time to start
    time.sleep(2)

    # Start the HTTP gateway
    print("Starting HTTP gateway...")
    gateway_process = subprocess.Popen([sys.executable, "-m", "Pyro5.utils.httpgateway", 
                                      "-e", r"Pyro\.|example\."],
                                     bufsize=1,  # Line buffered
                                     text=True,  # Use text mode instead of binary
                                     stdout=None,  # Use parent's stdout
                                     stderr=None)  # Use parent's stderr
    processes.append(gateway_process)

    print("\nAll services started!")
    print("Use Ctrl+C to stop all services")
    
    # Wait for processes to finish or for user interrupt
    try:
        while True:
            # Check if any process has terminated
            for process in processes:
                if process.poll() is not None:
                    print(f"Process terminated with exit code {process.poll()}")
                    return
            time.sleep(0.1)
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        signal_handler(signal.SIGINT, None)
