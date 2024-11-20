import Pyro5.api

def main():
    try:
        # Get a proxy to the remote object using the name server
        remote_control = Pyro5.api.Proxy("PYRONAME:example.remote_control")

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

    except Pyro5.errors.NamingError:
        print("Error: Could not find the remote object. Is the server running?")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
