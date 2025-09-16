import os
from dotenv import load_dotenv
from image_analyzer import analyze_image

# Load environment variables from .env file
load_dotenv()

def main():
    # Get API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("Please set the OPENROUTER_API_KEY environment variable")
        print("You can either:")
        print("1. Set it in your environment")
        print("2. Create a .env file with your API key")
        return
    
    # Specify image path
    image_path = "input/nano_banana.png"  # Change this to your image path

    # Check if image exists
    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        print("Please place an image in the 'input' folder and update the path in this script")
        print("Supported formats: PNG, JPG, JPEG, GIF, BMP, WEBP")
        return
    
    # Define your prompt
    prompt = """
    Extraia as seguintes informações a partir do arquivo de imagem:
    'Empresa Compradora:',
    'Volume de Energia:',
    'Sazonalização:',
    'Flexibilidade:',
    Analise bastante, pense bastante e responda de maneira curta somente os campos solicitados em forma de dicionário em Camel Case.
    """
    
    # Analyze the image
    print("Analyzing image...")
    try:
        result = analyze_image(image_path, prompt, api_key)
        print("\nAnalysis result:")
        print(result)
    except Exception as e:
        print(f"Error analyzing image: {e}")

if __name__ == "__main__":
    main()