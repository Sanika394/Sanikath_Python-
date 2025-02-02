import google.generativeai as genai
import os

# Load API key
api_key = "AIzaSyAA-h--SY4QUdD2IKUd3g4xt9BKfRnHUEo"


if not api_key:
    raise ValueError("API Key not found! Set GOOGLE_GEMINI_API_KEY in your environment.")

genai.configure(api_key=api_key)

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")

    try:
        response = model.generate_content(
            prompt,  
            generation_config={
                "max_output_tokens": 50,  # Limit output size
                "temperature": 0.5,       
                "top_p": 0.9
            }
        )

        # Extract text from response
        response_text = response.candidates[0]['content']['parts'][0]['text']
        print(f"Extracted Response: {response_text}")  # Debugging output
        return response_text.strip()

    except Exception as e:
        print(f"API Error: {e}")
        return "Error in AI response."

if __name__ == "__main__":
    print(get_gemini_response("What is coding?"))


