prompt = """Return ONLY valid JSON, no other text, in this exact shape:
{"topic": "...", "difficulty": "beginner|intermediate|advanced"}

Do not wrap the JSON in ``` marks or the word json. Output raw JSON only, starting with { or [.

Classify the following  questions: 
"How do I reverse a string in Python?"
"What is the difference between a list and a tuple?"
"How do I implement a custom context manager using __enter__ and __exit__?"
"""

import anthropic
import json

client = anthropic.Anthropic()  # establishing the connection


def return_json(response, prompt):
    raw_text = response.content[0].text
    data = json.loads(raw_text)

    clean_data = []
    for i in data:
        clean_data.append((i["topic"], i["difficulty"]))

    return clean_data


# create the call
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[{"role": "user", "content": prompt}],
    system="You are a grumpy old sea captain.",
)

outcome = return_json(response, prompt)
print(outcome)
