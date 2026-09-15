import os
from google import genai
from google.genai import types

def explain_code_error(error_log: str) -> str:
    # Pass your API key directly or let it use GEMINI_API_KEY environment variable
    client = genai.Client(api_key="GEMINI_API_KEY")
    
    config = types.GenerateContentConfig(
        system_instruction="You are a helpful coding assistant. Explain the error concisely in bullet points and provide a corrected snippet.",
        temperature=0.2,
    )

    print("Analyzing error with Gemini...\n")
    
    # Updated model name to a supported endpoint
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"Explain this Python error/issue and show how to fix it:\n\n{error_log}",
        config=config,
    )
    
    return response.text

if __name__ == "__main__":
    sample_error = """
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    Code:
    age = 25
    message = "I am " + age + " years old"
    """
    
    explanation = explain_code_error(sample_error)
    
    print("--- AI Explanation ---")
    print(explanation)