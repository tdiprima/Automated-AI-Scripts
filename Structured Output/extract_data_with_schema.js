const { Ollama } = require('ollama');

async function getFriendsList() {
  try {
    const ollama = new Ollama({ host: 'http://localhost:11434' });

    const response = await ollama.chat({
      model: 'llama3.2',
      messages: [
        {
          role: 'user',
          content:
            "I have two friends. The first is Ollama, 22 years old, busy saving the world, and the second is Alonso, 23 years old and wants to hang out. Return a list of friends in JSON format. Only return JSON; nothing else."
        }
      ],
      options: {
        temperature: 0 // Make the response deterministic
      }
    });

    console.log("Raw Response:", response);

    // Attempt to parse the content as JSON
    try {
      const parsedContent = JSON.parse(response.message.content);
      console.log("Parsed Content:", parsedContent);
    } catch (parseError) {
      console.error("Failed to parse JSON:", parseError);
      console.log("Response content:", response.message.content);
    }
  } catch (error) {
    console.error("Error fetching friends list:", error);
  }
}

getFriendsList();
