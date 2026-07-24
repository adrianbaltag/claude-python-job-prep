import anthropic

client = anthropic.Anthropic()  # establishing the connection

# create the call
response = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=500,
    messages=[{"role": "user", "content": "who am I?"}],
    system="You are a grumpy old sea captain. Answer every question in character, complaining about the weather at least once.",
)

reply = response.content[0].text
print(reply)
