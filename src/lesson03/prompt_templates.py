"""
    Write at least one function that takes 2+ parameters and returns an f-string prompt (e.g. build_prompt(topic, tone) → "Explain {topic} in a {tone} tone.").
Call that function with at least two different sets of arguments to prove it's reusable.
Feed at least one of the built prompts into a real client.messages.create() call and print Claude's reply — reuse what you already know from Lessons 1–2.

"""

import anthropic


def build_prompt(topic, tone):
    return f"Explain {topic} in a {tone} tone"


print(
    build_prompt(
        "python", "as a python dev, but in a plain manner, easy to understand, for kids"
    )
)


def first_call():

    client = anthropic.Anthropic()  # establishing the connection
    my_prompt = build_prompt("python", "friendly")
    # create the call
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        messages=[{"role": "user", "content": my_prompt}],
        system="You are a grumpy old sea captain. Answer every question in character, complaining about the weather at least once.",
    )

    reply = response.content[0].text
    print(reply)


first_call()
