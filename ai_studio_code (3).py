import google.generativeai as genai

def analyze_incident(image_path):
    model = genai.GenerativeModel('gemini-pro-vision')
    image = PIL.Image.open(image_path)
    response = model.generate_content([
        "Analyze this construction site safety violation. Describe the risk and suggest an immediate corrective action.", 
        image
    ])
    return response.text