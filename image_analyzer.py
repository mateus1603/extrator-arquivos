import base64
import os
from openai import OpenAI

def encode_image(image_path):
    """Encode image to base64 string"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def get_image_type(image_path):
    """Get the image type for the data URL"""
    ext = os.path.splitext(image_path)[1].lower()
    if ext == '.jpg' or ext == '.jpeg':
        return 'jpeg'
    elif ext == '.png':
        return 'png'
    elif ext == '.gif':
        return 'gif'
    elif ext == '.bmp':
        return 'bmp'
    elif ext == '.webp':
        return 'webp'
    else:
        # Default to jpeg for unknown types
        return 'jpeg'

def analyze_image(image_path, prompt, api_key):
    """
    Analyze an image using Google Gemini 2.0 Flash via OpenRouter API
    
    Args:
        image_path (str): Path to the image file
        prompt (str): Prompt to guide the analysis
        api_key (str): OpenRouter API key
    
    Returns:
        str: Analysis result from the model
    """
    # Encode the image
    base64_image = encode_image(image_path)
    
    # Determine image type
    image_type = get_image_type(image_path)
    
    # Initialize OpenAI client with OpenRouter
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    
    # Create the completion request
    completion = client.chat.completions.create(
        model="google/gemini-2.0-flash-exp:free",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/{image_type};base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        max_tokens=500
    )
    
    return completion.choices[0].message.content

def main():
    # Get API key from environment variable
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Please set the OPENROUTER_API_KEY environment variable")
        return
    
    # Check if input folder exists
    input_folder = "input"
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' not found")
        return
    
    # Get all image files from input folder
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
    image_files = [f for f in os.listdir(input_folder) 
                   if f.lower().endswith(image_extensions)]
    
    if not image_files:
        print(f"No image files found in '{input_folder}' folder")
        print(f"Supported formats: {', '.join(image_extensions)}")
        return
    
    # Display available images
    print("Available images:")
    for i, image_file in enumerate(image_files, 1):
        print(f"{i}. {image_file}")
    
    # Select an image
    try:
        choice = int(input("Select an image by number: ")) - 1
        if choice < 0 or choice >= len(image_files):
            print("Invalid selection")
            return
    except ValueError:
        print("Invalid input")
        return
    
    selected_image = image_files[choice]
    image_path = os.path.join(input_folder, selected_image)
    
    # Get user prompt
    prompt = input("Enter your prompt for image analysis: ")
    if not prompt:
        prompt = "Analyze this image and describe what you see"
    
    # Analyze the image
    print("\nAnalyzing image...")
    try:
        result = analyze_image(image_path, prompt, api_key)
        print("\nAnalysis result:")
        print(result)
    except Exception as e:
        print(f"Error analyzing image: {e}")

if __name__ == "__main__":
    main()