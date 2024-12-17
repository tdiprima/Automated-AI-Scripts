const axios = require('axios');
const fs = require('fs');
const path = require('path');

async function analyzeCodeSegment(codeSegment, question = null) {
    const prompt = question
        ? `Question: ${question}\n\nCode Segment:\n${codeSegment}`
        : `Analyze this code segment:\n\n${codeSegment}`;

    try {
        const response = await axios.post('http://localhost:11434/api/generate', {
            prompt: prompt,
            model: 'codebase-analyzer' // Custom model for codebase analysis
        }, { responseType: 'stream' });

        // Stream response and accumulate if necessary
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
                            console.log("Analysis Result:\n", fullResponse);
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
        console.error("Error analyzing code segment:", error);
    }
}

// Recursive function to scan a directory for code files
function scanDirectory(directory) {
    const codeSegments = [];
    fs.readdirSync(directory).forEach(file => {
        const filePath = path.join(directory, file);
        const stat = fs.statSync(filePath);
        if (stat.isDirectory()) {
            codeSegments.push(...scanDirectory(filePath));
        } else if (file.endsWith('.js') || file.endsWith('.py') || file.endsWith('.java')) {
            const code = fs.readFileSync(filePath, 'utf8');
            codeSegments.push({ filePath, code });
        }
    });
    return codeSegments;
}

// Main function to analyze codebase
function analyzeCodebase(directory, question = null) {
    const codeSegments = scanDirectory(directory);
    for (const { filePath, code } of codeSegments) {
        console.log(`\nAnalyzing ${filePath}...`);
        analyzeCodeSegment(code, question);
    }
}

// Example usage
const codebaseDirectory = './path_to_codebase'; // Set this to your codebase directory
analyzeCodebase(codebaseDirectory, "What dependencies does this code use?");
