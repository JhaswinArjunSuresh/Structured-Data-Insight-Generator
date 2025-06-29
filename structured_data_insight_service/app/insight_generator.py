from openai import OpenAI
import json

client = OpenAI()

def generate_insights(profile_dict):
    prompt = f"""
Here is a data profile in JSON:
{json.dumps(profile_dict, indent=2)}

Provide insights, trends, anomalies, and any business suggestions.
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user", "content": prompt}]
    )
    return response.choices[0].message.content

