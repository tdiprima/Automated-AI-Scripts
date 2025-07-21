# Complete example with function calling for SmolLM3
from transformers import AutoModelForCausalLM, AutoTokenizer
import json
import re

checkpoint = "HuggingFaceTB/SmolLM3-3B"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

# Define the tool
tools = [
    {
        "name": "get_weather",
        "description": "Get the weather in a city",
        "parameters": {
            "type": "object", 
            "properties": {
                "city": {
                    "type": "string", 
                    "description": "The city to get the weather for"
                }
            }
        }
    }
]

# Simulate the weather function
def get_weather(city):
    # In reality, this would call a weather API
    return f"The weather in {city} is sunny with a temperature of 72°F (22°C)."

# Initial conversation
messages = [
    {
        "role": "user",
        "content": "Hello! How is the weather today in Bayport, NY, USA?"
    }
]

# First generation - model will request to call the function
inputs = tokenizer.apply_chat_template(
    messages,
    enable_thinking=False,
    xml_tools=tools,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt"
)

outputs = model.generate(inputs, max_new_tokens=256, temperature=0.7)
response = tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)
print("Model's first response:", response)

# Parse the function call from the response
# The model typically outputs something like:
# <tool_call> {"name": "get_weather", "arguments": {"city": "Bayport, NY, USA"}} </tool_call>
tool_call_pattern = r'<tool_call>\s*({.*?})\s*</tool_call>'
match = re.search(tool_call_pattern, response, re.DOTALL)

if match:
    # Extract and parse the function call
    function_call = json.loads(match.group(1))
    function_name = function_call["name"]
    arguments = function_call["arguments"]
    
    print(f"\nFunction call detected: {function_name}")
    print(f"Arguments: {arguments}")
    
    # Execute the function
    if function_name == "get_weather":
        result = get_weather(arguments["city"])
        print(f"Function result: {result}")
        
        # Add the assistant's function call to the conversation
        messages.append({
            "role": "assistant",
            "content": response
        })
        
        # Add the function result to the conversation
        messages.append({
            "role": "tool",
            "name": "get_weather",
            "content": result
        })
        
        # Generate the final response with the function result
        inputs = tokenizer.apply_chat_template(
            messages,
            enable_thinking=False,
            xml_tools=tools,
            add_generation_prompt=True,
            tokenize=True,
            return_tensors="pt"
        )
        
        outputs = model.generate(inputs, max_new_tokens=256, temperature=0.7)
        final_response = tokenizer.decode(outputs[0][inputs.shape[-1]:], skip_special_tokens=True)
        print(f"\nFinal answer: {final_response}")
else:
    print("No function call detected in the response")

# Alternative: If you want to see the full conversation history
print("\n--- Full Conversation ---")
for msg in messages:
    role = msg.get("role", "")
    name = msg.get("name", "")
    content = msg.get("content", "")
    if name:
        print(f"{role} ({name}): {content}")
    else:
        print(f"{role}: {content}")