// File: script.js
async function fetchTelemetryData() {
    try {
        const response = await fetch('/api/v1/telemetry/data');
        const data = await response.json();

        document.getElementById('altitude').textContent = data.altitude.toFixed(2);
        document.getElementById('speed').textContent = data.speed.toFixed(2);
        document.getElementById('battery').textContent = data.batteryLevel.toFixed(2);
        document.getElementById('gps').textContent = `${data.latitude.toFixed(4)}, ${data.longitude.toFixed(4)}`;
        document.getElementById('heading').textContent = data.heading.toFixed(2);
        
        const statusElem = document.getElementById('status');
        statusElem.textContent = data.status;
        statusElem.className = data.status === "low battery" ? 'alert' : '';
    } catch (error) {
        console.error('Error fetching telemetry data:', error);
    }
}

setInterval(fetchTelemetryData, 2000); // Fetch every 2 seconds
