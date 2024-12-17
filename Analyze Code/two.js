const axios = require('axios');

async function analyzeCodeWithCustomModel(codeSnippet, taskType) {
    const prompt = `Task: ${taskType}. Analyze this code:\n\n${codeSnippet}`;
    let fullResponse = "";

    try {
        const response = await axios.post('http://localhost:11434/api/generate', {
            prompt: prompt,
            model: 'my-code-analyzer' // Use your custom model's name
        }, { responseType: 'stream' });

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
                            console.log(`Final Output for ${taskType}:\n`, fullResponse);
                        }
                    } catch (error) {
                        console.error("Error parsing JSON line:", error);
                    }
                }
            }
        });
        
        response.data.on('end', () => {
            console.log(`\nStream ended for ${taskType}.`);
        });

    } catch (error) {
        console.error("Error analyzing code:", error);
    }
}

// Example usage
const codeSnippet = `
function exampleFunction(input) {
    if (!input) return null;
    let result = [];
    for (let i = 0; i < input.length; i++) {
        result.push(input[i] * 2);
    }
    return result;
}
`;

// Run analysis by task type
analyzeCodeWithCustomModel(codeSnippet, 'vulnerability');
analyzeCodeWithCustomModel(codeSnippet, 'refactoring');
analyzeCodeWithCustomModel(codeSnippet, 'documentation');
