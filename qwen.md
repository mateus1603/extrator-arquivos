# Qwen Customization Guide

This file contains customization settings and preferences for this project when using Qwen Code.

## Project Information
- **Project Name**: Sistema Solar - Image Analyzer
- **Description**: Python script that uses the OpenAI package to call the Google Gemini 2.0 Flash model via OpenRouter API to analyze images
- **Primary Language**: Python
- **Frameworks/Libraries**: OpenAI Python SDK, python-dotenv

## Code Style Preferences
- **Indentation**: 4 spaces
- **Line Endings**: LF
- **Quote Style**: Double quotes for strings, single quotes for keys
- **Semicolons**: Not used
- **Naming Conventions**: snake_case for variables and functions, PascalCase for classes

## Development Environment
- **Python Version**: 3.7+
- **Package Manager**: pip
- **Virtual Environment**: Created with `python -m venv venv`

## Testing Preferences
- **Testing Framework**: pytest
- **Test Directory**: tests/
- **Coverage Threshold**: 80%

## Build/Deployment Information
- **Installation Command**: pip install -r requirements.txt
- **Run Command**: python image_analyzer.py

## Qwen Code Preferences
- **Preferred Tools**: Python development, API integration, file system operations
- **Workflow Patterns**: Create project structure, implement core functionality, add documentation, verify with compilation test
- **Common Tasks**: API integration, environment variable management, image processing

## Notes
- Uses OpenRouter API to access Google Gemini 2.0 Flash model
- Supports multiple image formats (PNG, JPG, JPEG, GIF, BMP, WEBP)
- Requires OpenRouter API key set as environment variable
- Images should be placed in the 'input' folder