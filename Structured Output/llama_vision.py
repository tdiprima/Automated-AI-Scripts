# https://ollama.com/blog/structured-outputs
from ollama import chat
from pydantic import BaseModel
from typing import List, Optional, Literal

class Object(BaseModel):
    name: str
    confidence: float
    attributes: str 

class ImageDescription(BaseModel):
    summary: str
    objects: List[Object]
    scene: str
    colors: List[str]
    time_of_day: Literal['Morning', 'Afternoon', 'Evening', 'Night']
    setting: Literal['Indoor', 'Outdoor', 'Unknown']
    text_content: Optional[str] = None

path = 'beach.jpg'

response = chat(
    model='llama3.2-vision',
    format=ImageDescription.model_json_schema(),  # Pass in the schema for the response
    messages=[
        {
            'role': 'user',
            'content': 'Analyze this image and describe what you see, including any objects, the scene, colors and any text you can detect.',
            'images': [path],
        },
    ],
    options={'temperature': 0},  # Set temperature to 0 for more deterministic output
)

image_description = ImageDescription.model_validate_json(response.message.content)
print(image_description)

# summary='A palm tree stands on a sandy beach with the ocean in the background.' objects=[Object(name='tree', confidence=0.999, 
# attributes='palm tree'), Object(name='ground', confidence=0.998, attributes='sand')] scene='beach' colors=['#F7D2C4', '#FFB6C1', 
# '#FF69B4'] time_of_day='Afternoon' setting='Outdoor' text_content='The image shows a palm tree standing on a sandy beach, 
# with the ocean visible in the background. The sky is blue and cloudy, suggesting that it is afternoon. The overall atmosphere 
# of the image is one of relaxation and tranquility, evoking feelings of warmth and sunshine.'

