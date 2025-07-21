# The checkpoint you are trying to load has model type `smollm3` but Transformers does not recognize this architecture.
# https://medium.com/data-science-in-your-pocket/smollm3-the-best-small-llm-for-everything-3fa53713ebb7
from transformers import AutoModelForCausalLM, AutoTokenizer

checkpoint = "HuggingFaceTB/SmolLM3-3B"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

tools = [
    {
        "name": "get_weather",
        "description": "Get the weather in a city",
        "parameters": {"type": "object", "properties": {"city": {"type": "string", "description": "The city to get the weather for"}}}}
]

messages = [
    {
        "role": "user",
        "content": "Hello! How is the weather today in Copenhagen?"
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    enable_thinking=False, # True works as well, your choice!
    xml_tools=tools,
    add_generation_prompt=True,
    tokenize=True,
    return_tensors="pt"
)

outputs = model.generate(inputs)
print(tokenizer.decode(outputs[0]))
