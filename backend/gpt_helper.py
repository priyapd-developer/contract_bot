# GPT-4 prompts for suggested alternatives & Hindi → English
import openai

# Make sure you have OPENAI_API_KEY in your environment variables
openai.api_key = "YOUR_API_KEY"

def suggest_safer_clause(clause_text):
    prompt = f"Suggest a safer version of this contract clause for a small business in simple English:\n\n{clause_text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    return response.choices[0].message.content.strip()

def translate_hindi_to_english(text):
    prompt = f"Translate this Hindi contract text into clear English:\n\n{text}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    
    return response.choices[0].message.content.strip()
