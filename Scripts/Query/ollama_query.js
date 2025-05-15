/**
 * Fetching Ollama responses
 */
const ollamaModel = 'mistral';
const prompt = 'Is it Friday yet?';
let partialResponse = '';

async function fetchData() {
    try {
        // Sends a POST request to the API with the prompt and model.
        const res = await fetch('http://localhost:11434/api/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt, model: ollamaModel })
        });

        // Checks if the response is OK (200-299).
        if (!res.ok) {
            throw new Error(`Server error: ${res.status}`);
        }

        // Reads the response body as a stream.
        const reader = res.body.getReader();
        const decoder = new TextDecoder();
        let done = false;

        while (!done) {
            const { value, done: streamDone } = await reader.read();
            done = streamDone;

            if (value) {
                // Decodes the chunked response into a string.
                const chunk = decoder.decode(value, { stream: true });
                const jsonStrings = chunk.trim().split('\n');
                
                jsonStrings.forEach(str => {
                    try {
                        // Parses each JSON string and appends its response to partialResponse.
                        const data = JSON.parse(str);
                        if (data.response) {
                            partialResponse += data.response;
                        }
                    } catch (e) {
                        console.log('JSON parse error:', e);
                    }
                });
            }
        }

        // Logs the final response to the console.
        console.log(partialResponse);
    } catch (error) {
        console.log('Fetch error:', error);
    }
}

fetchData();
