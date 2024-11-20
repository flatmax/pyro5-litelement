# Pyro5 LitElement Remote Control

A web-based distributed application that demonstrates the integration of Pyro5 remote objects with a modern web frontend using LitElement web components.

## Features

- Remote object control through web interface
- Real-time status updates
- Value setting and monitoring
- Clean, modern UI using LitElement
- Distributed architecture using Pyro5
- HTTP Gateway integration for web access

## Architecture

### Backend (Python)
- Pyro5 nameserver for object registration and discovery
- Remote control object with status and value management
- HTTP Gateway for web accessibility
- Multi-threaded server handling

### Frontend (Web)
- LitElement-based web components
- Modern JavaScript with async/await
- Real-time UI updates
- Error handling and status feedback

## Prerequisites

### Python Requirements
- Python 3.12 or higher
- Pyro5

### Node.js Requirements
- Node.js (Latest LTS version)
- npm (comes with Node.js)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/flatmax/pyro5-litelement.git
   cd pyro5-litelement
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install Node.js dependencies:
   ```bash
   npm install
   ```

## Running the Application

1. Start the server and HTTP gateway:
   ```bash
   python start_services.py
   ```
   This will start:
   - Pyro5 nameserver
   - Remote control server
   - HTTP gateway (exposed at http://localhost:8080/pyro/)

2. Open `index.html` in your web browser
   - You can use any local web server, for example:
     ```bash
     python -m http.server
     ```
     Then visit http://localhost:8000

## Usage

1. The web interface shows:
   - Current status of the remote control
   - Current value
   - Control buttons for start/stop
   - Input field for setting new values

2. Available operations:
   - Start the remote control
   - Stop the remote control
   - Get current status
   - Get current value
   - Set new value

## Development

### Project Structure
```
pyro5-litelement/
├── README.md
├── requirements.txt
├── package.json
├── index.html
├── remote-control.js     # LitElement component
├── remote_object.py      # Pyro5 remote object
├── server.py            # Pyro5 server
├── start_services.py    # Service starter
└── client.py           # Python client example
```

### Adding New Features
1. Remote Object:
   - Add new methods to `remote_object.py`
   - Register them with `@Pyro5.api.expose`

2. Web Interface:
   - Extend the LitElement component in `remote-control.js`
   - Add new UI elements in the `render()` method
   - Implement corresponding methods for new functionality

## Troubleshooting

1. Connection Issues:
   - Ensure the Pyro5 nameserver is running
   - Check HTTP gateway exposure patterns
   - Verify CORS settings if needed

2. Common Errors:
   - 500 Internal Server Error: Check Python server logs
   - Object not found: Verify object registration
   - Communication errors: Check network connectivity

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

[Add your license here]

## Acknowledgments

- Pyro5 team for the excellent distributed object system
- LitElement team for the web components framework
