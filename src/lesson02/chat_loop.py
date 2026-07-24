import anthropic

client = anthropic.Anthropic()
conversation_history = []  # the growing transcript history, empty at the start

keep_chatting = True
while keep_chatting:
    user_message = input("You: ")

    if user_message == "quit":
        keep_chatting = False
    else:
        conversation_history.append({"role": "user", "content": user_message})

        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=500,
            messages=conversation_history,  # the WHOLE transcript, not just the latest line
            temperature=1,
            system="Your Jack Sparrow, the famous pirate captain from Caraibe",
        )

        reply_text = response.content[0].text
        print("Claude:", reply_text)

        conversation_history.append({"role": "assistant", "content": reply_text})
