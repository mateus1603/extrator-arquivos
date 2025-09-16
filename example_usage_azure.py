import os
from dotenv import load_dotenv
from image_analyzer_azure import analyze_file

# Load environment variables from .env file
load_dotenv()

def main():
    # Get Azure OpenAI credentials from environment variables
    api_key = os.getenv("AZURE_OPENAI_KEY")
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not all([api_key, azure_endpoint, deployment_name]):
        print("Please set the following environment variables:")
        print("AZURE_OPENAI_KEY")
        print("AZURE_OPENAI_ENDPOINT")
        print("AZURE_OPENAI_DEPLOYMENT")
        print("You can either:")
        print("1. Set them in your environment")
        print("2. Create a .env file with your credentials")
        return
    
    # Specify file path
    file_path = "input/example.pdf"  # Change this to your file path

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        print("Please place a file in the 'input' folder and update the path in this script")
        print("Supported formats: PNG, JPG, JPEG, GIF, BMP, WEBP, PDF")
        return
    
    # Define your prompt
    prompt = """
    Extraia as seguintes informações a partir do arquivo:
    'Empresa Compradora:',
    'Volume de Energia:',
    'Sazonalização:',
    'Flexibilidade:',
    Analise bastante, pense bastante e responda de maneira curta somente os campos solicitados em forma de dicionário em Camel Case.
    """
    
    # Analyze the file
    print("Analyzing file...")
    try:
        result = analyze_file(file_path, prompt, api_key, azure_endpoint, deployment_name)
        print("\nAnalysis result:")
        print(result)
    except Exception as e:
        print(f"Error analyzing file: {e}")

if __name__ == "__main__":
    main()