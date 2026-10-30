import os 
from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")


def get_ai_suggestion(description):
    if not api_key:
        raise ValueError("API key is missing")
    client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)

    prompt =  f"""
You are CampusFlow's helpdesk AI assistant. Analyze this reported issue: {description}

Provide a concise troubleshooting report using this structure:
1. POSSIBLE CAUSES
List the 3 most likely causes.

2. TROUBLESHOOTING STEPS
Give 3 to 5 simple steps in the correct order.

3. RECOMMENDED SOLUTION
Suggest the most appropriate solution based on the information available.

4. WHEN TO ESCALATE
Explain when the issue should be referred to a technician.

Rules:
- Use simple, professional language.
- Keep explanations brief.
- Do not assume the exact cause without evidence.
- Avoid unnecessary technical jargon.
- Do not recommend risky hardware repairs to ordinary users.
- Use plain text headings and numbered lists.
- Do not use Markdown tables.
"""

    response = client.chat.completions.create(model="nvidia/nemotron-3-ultra-550b-a55b:free", messages=[{"role": "user", "content": prompt}])

    return response.choices[0].message.content
