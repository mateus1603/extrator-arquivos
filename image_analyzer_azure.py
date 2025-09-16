import base64
import os
import io
from openai import AzureOpenAI
from pdf2image import convert_from_path

def encode_image(image_path):
    """Encode image to base64 string"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def convert_pdf_to_images(pdf_path):
    """Converts a PDF file to a list of base64 encoded images."""
    images = convert_from_path(pdf_path)
    base64_images = []
    for image in images:
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        base64_images.append(base64.b64encode(buffered.getvalue()).decode('utf-8'))
    return base64_images

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
        return 'png'

def analyze_media(base64_images, prompt, api_key, azure_endpoint, deployment_name):
    """
    Analyze a list of images using Azure OpenAI.
    
    Args:
        base64_images (list): A list of base64 encoded image strings.
        prompt (str): Prompt to guide the analysis
        api_key (str): Azure OpenAI API key
        azure_endpoint (str): Azure OpenAI endpoint
        deployment_name (str): Azure OpenAI deployment name for the model
    
    Returns:
        str: Analysis result from the model
    """
    # Initialize AzureOpenAI client
    client = AzureOpenAI(
        api_version="2024-02-15-preview",
        azure_endpoint=azure_endpoint,
        api_key=api_key,
    )
    
    content = [{"type": "text", "text": prompt}]
    for base64_image in base64_images:
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{base64_image}"
            }
        })

    # Create the completion request
    completion = client.chat.completions.create(
        model=deployment_name,
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
        max_tokens=500
    )
    
    return completion.choices[0].message.content

def analyze_file(file_path, prompt, api_key, azure_endpoint, deployment_name):
    """
    Analyzes a file (image or PDF) using Azure OpenAI.
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        base64_images = convert_pdf_to_images(file_path)
    else:
        base64_images = [encode_image(file_path)]
        
    return analyze_media(base64_images, prompt, api_key, azure_endpoint, deployment_name)


def main():
    # Get Azure OpenAI credentials from environment variables
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("AZURE_OPENAI_KEY")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not all([api_key, azure_endpoint, deployment_name]):
        print("Please set the following environment variables:")
        print("AZURE_OPENAI_KEY")
        print("AZURE_OPENAI_ENDPOINT")
        print("AZURE_OPENAI_DEPLOYMENT")
        return
    
    # Check if input folder exists
    input_folder = "input"
    if not os.path.exists(input_folder):
        print(f"Input folder '{input_folder}' not found")
        return
    
    # Get all image and pdf files from input folder
    supported_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.pdf')
    files = [f for f in os.listdir(input_folder) 
                   if f.lower().endswith(supported_extensions)]
    
    if not files:
        print(f"No supported files found in '{input_folder}' folder")
        print(f"Supported formats: {', '.join(supported_extensions)}")
        return
    
    # Display available files
    print("Available files:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    
    # Select a file
    try:
        choice = int(input("Select a file by number: ")) - 1
        if choice < 0 or choice >= len(files):
            print("Invalid selection")
            return
    except ValueError:
        print("Invalid input")
        return
    
    selected_file = files[choice]
    file_path = os.path.join(input_folder, selected_file)
    
    # Get user prompt
    prompt = input("Enter your prompt for file analysis: ")
    if not prompt:
        prompt = "Analyze this file and describe what you see"
    
    # Analyze the file
    print("\nAnalyzing file...")
    try:
        result = analyze_file(file_path, prompt, api_key, azure_endpoint, deployment_name)
        print("\nAnalysis result:")
        print(result)
    except Exception as e:
        print(f"Error analyzing file: {e}")

if __name__ == "__main__":
    main()