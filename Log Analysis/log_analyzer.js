const axios = require('axios');
const fs = require('fs');

async function analyzeLogs(logData) {
    const prompt = `Analyze the following logs and suggest fixes or troubleshooting steps:\n\n${logData}`;

    try {
        const response = await axios.post('http://localhost:11434/api/generate', {
            prompt: prompt,
            model: 'log-analyzer' // Custom model for log analysis
        }, { responseType: 'stream' });

        // Accumulate the response if it's streamed
        let fullResponse = '';
        response.data.on('data', (chunk) => {
            const lines = chunk.toString().trim().split('\n');
            for (const line of lines) {
                if (line.trim()) {
                    try {
                        const jsonResponse = JSON.parse(line);
                        if (jsonResponse.response) {
                            fullResponse += jsonResponse.response;
                        }
                        if (jsonResponse.done) {
                            console.log("Log Analysis Result:\n", fullResponse);
                        }
                    } catch (error) {
                        console.error("Error parsing JSON line:", error);
                    }
                }
            }
        });

        response.data.on('end', () => {
            console.log("\nAnalysis completed.");
        });

    } catch (error) {
        console.error("Error analyzing logs:", error);
    }
}

// Example usage: read logs from a file and analyze
const logFile = './server_logs.txt';
fs.readFile(logFile, 'utf8', (err, data) => {
    if (err) {
        console.error("Error reading log file:", err);
        return;
    }
    analyzeLogs(data);
});
