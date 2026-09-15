# AI Code Explainer

A Python CLI tool built using the `google-genai` SDK and Gemini API to analyze Python error logs and generate actionable fixes.

## Features
- Automates code debugging using Gemini models.
- Custom system instructions for concise output.
- Low temperature setting for deterministic results.

## How to Run
1. Install requirements: `pip install google-genai`
2. Set API Key: `export GEMINI_API_KEY="your-key"`
3. Run script: `python explain_error.py`
