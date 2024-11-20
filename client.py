import Pyro5.api

def main():
    # Get a Proxy to the remote object
    # Replace the URI below with the one printed by the server
    uri = input("Enter the URI of the remote object: ")
    remote_control = Pyro5.api.Proxy(uri)

    # Example usage
    print("Initial status:", remote_control.get_status())
    
    print("Starting system...")
    print(remote_control.start())
    print("Current status:", remote_control.get_status())
    
    print("\nSetting value to 42...")
    print(remote_control.set_value(42))
    print("Current value:", remote_control.get_value())
    
    print("\nStopping system...")
    print(remote_control.stop())
    print("Final status:", remote_control.get_status())

if __name__ == "__main__":
    main()
