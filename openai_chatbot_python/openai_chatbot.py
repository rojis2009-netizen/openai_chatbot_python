import openai

API_KEY = "api key"
openai.api_key = API_KEY
openai.api_base = "URL"

messages_list = [
    {"role": "system", "content": "you are a helpful assistant"}
]

while True:

    user_input = input("you:")

    print("Connecting to the LLM...")

    messages_list.append(
        {"role": "user", "content": user_input}
    )

    response = openai.ChatCompletion.create(

        messages = messages_list,
        model = "gpt-4o-mini"

)
    messages_list.append(
        {"role": "assistant", "content": response['choices'][0]['message']['content']}
    )

    print(response['choices'][0]['message']['content'])
