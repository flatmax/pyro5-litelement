import { LitElement, html, css } from 'https://cdn.jsdelivr.net/gh/lit/dist@2/core/lit-core.min.js';

class RemoteControl extends LitElement {
    static styles = css`
        :host {
            display: block;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            max-width: 500px;
            margin: 0 auto;
        }
        .status {
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            background: #f0f0f0;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            margin: 5px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .value-control {
            margin: 20px 0;
        }
        input {
            padding: 8px;
            margin-right: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    `;

    static properties = {
        status: { type: String },
        value: { type: Number },
        objectId: { type: String }
    };

    constructor() {
        super();
        this.status = 'Unknown';
        this.value = 0;
        this.objectId = 'example.remote_control';  // Use the exact name we registered
        this.updateStatus();
    }

    async callMethod(method, params = []) {
        if (!this.objectId) return;
        try {
            console.log(`Calling ${method} with params:`, params);
            const response = await fetch(`http://localhost:8080/pyro/${this.objectId}/${method}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    args: params,
                    kwargs: {}
                }),
            });
            
            if (!response.ok) {
                const errorText = await response.text();
                console.error(`Server responded with ${response.status}:`, errorText);
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const result = await response.json();
            console.log(`Result from ${method}:`, result);
            if (result.error) {
                throw new Error(result.error);
            }
            return result.result;
        } catch (error) {
            console.error(`Error calling ${method}:`, error);
            throw error; // Re-throw to handle in the calling function
        }
    }

    async updateStatus() {
        try {
            this.status = await this.callMethod('get_status') || 'Unknown';
            this.value = await this.callMethod('get_value') || 0;
        } catch (error) {
            console.error('Error updating status:', error);
        }
    }

    async handleStart() {
        try {
            await this.callMethod('start');
            this.updateStatus();
        } catch (error) {
            console.error('Error starting:', error);
        }
    }

    async handleStop() {
        try {
            await this.callMethod('stop');
            this.updateStatus();
        } catch (error) {
            console.error('Error stopping:', error);
        }
    }

    async handleSetValue() {
        try {
            const input = this.shadowRoot.querySelector('#valueInput');
            const newValue = parseInt(input.value);
            console.log('Setting value to:', newValue);
            if (!isNaN(newValue)) {
                await this.callMethod('set_value', [newValue]);
                await this.updateStatus();
            } else {
                console.error('Invalid input value:', input.value);
            }
        } catch (error) {
            console.error('Error setting value:', error);
        }
    }

    render() {
        return html`
            <div>
                <h2>Remote Control Panel</h2>
                <div class="status">
                    Status: ${this.status}
                </div>
                <div class="status">
                    Current Value: ${this.value}
                </div>
                <div>
                    <button @click=${this.handleStart}>Start</button>
                    <button @click=${this.handleStop}>Stop</button>
                </div>
                <div class="value-control">
                    <input type="number" id="valueInput" placeholder="Enter new value">
                    <button @click=${this.handleSetValue}>Set Value</button>
                </div>
            </div>
        `;
    }
}

customElements.define('remote-control', RemoteControl);
