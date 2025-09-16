# Image Analyzer with Google Gemini 2.0 Flash

This Python script uses the OpenAI package to call the Google Gemini 2.0 Flash model via OpenRouter API to analyze images.

## Setup

1. Create a Python virtual environment (recommended):
   ```bash
   # On Windows
   python -m venv venv
   
   # On macOS/Linux
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   # On Windows (Command Prompt)
   venv\Scripts\activate
   
   # On Windows (PowerShell)
   venv\Scripts\Activate.ps1
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Get an API key from [OpenRouter](https://openrouter.ai/)

5. Set your API key as an environment variable:
   ```bash
   # On Windows (Command Prompt)
   set OPENROUTER_API_KEY=your_api_key_here
   
   # On Windows (PowerShell)
   $env:OPENROUTER_API_KEY="your_api_key_here"
   
   # On macOS/Linux
   export OPENROUTER_API_KEY=your_api_key_here
   ```

   Alternatively, you can create a `.env` file based on `.env.example` and use the `python-dotenv` package to load it:
   ```bash
   cp .env.example .env
   # Edit .env with your API key
   ```

## Usage

1. Place your images in the `input` folder

2. Run the script:
   ```bash
   python image_analyzer.py
   ```

3. Follow the prompts to select an image and enter your analysis prompt

## Direct Usage

You can also use the analyzer directly in your code:

```python
from image_analyzer import analyze_image

# Make sure to set your OPENROUTER_API_KEY environment variable
result = analyze_image("input/your_image.jpg", "Describe this image", api_key)
print(result)
```

See `example_usage.py` for a complete example.

## Features

- Supports multiple image formats (PNG, JPG, JPEG, GIF, BMP, WEBP)
- Automatic image type detection for proper encoding
- Interactive image selection
- Customizable analysis prompts
- Base64 encoding for image transmission
- Error handling for API calls

## How It Works

The script uses the OpenAI Python package to connect to the OpenRouter API, which provides access to the Google Gemini 2.0 Flash model. Images are encoded in base64 format and sent as part of the chat completion request.

## Example Prompts

- "Describe the contents of this image in detail"
- "What objects can you identify in this image?"
- "Analyze the colors and composition of this image"
- "Identify any text present in this image"
- "What is the style of this image? (photograph, painting, etc.)"
- "Estimate the age of the people or objects in this image if possible"