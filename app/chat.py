import openai, os
import base64
# API_TOKEN = os.getenv('API_TOKEN')
openai.api_key = "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"

class GPT:
    
    def __init__(self):    
        pass  
        
    def create_prompt(self, label):
        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
            {"role": "system", "content": "You are a medical AI Diagnostic expert and a radiologist."},
            {"role": "user", "content": f"""
            My X-ray model predicted: {label}.
            Can you explain what this means in a single para! if it predicted
            nothing then it means no disease detected then just tell that there is no disease detected.   
            """}
            ]   
        )
        return response['choices'][0]['message']['content']
    
    
    def _encode_image(self, image):
        with open(image, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")