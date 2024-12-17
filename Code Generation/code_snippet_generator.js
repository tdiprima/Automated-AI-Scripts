const axios = require('axios');

async function generateCodeSnippet(taskDescription) {
    const prompt = `Task: ${taskDescription}`;

    try {
        const response = await axios.post('http://localhost:11434/api/generate', {
            prompt: prompt,
            model: 'code-snippet-generator',
        }, { responseType: 'stream' });

        // console.log("Generated Code Snippet:\n", response.data); // all of it

        let fullResponse = "";
        // Stream the response data
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
                            console.log(fullResponse);
                        }
                    } catch (error) {
                        console.error("Error parsing JSON line:", error);
                    }
                }
            }
        });
        
        response.data.on('end', () => {
            console.log("\nStream ended.");
        });
    } catch (error) {
        console.error("Error generating code snippet:", error);
    }
}

// Example usage with a specific task
generateCodeSnippet("Create a JavaScript function that fetches data from an API and handles errors gracefully.");
