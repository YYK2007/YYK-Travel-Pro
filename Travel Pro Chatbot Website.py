import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a travel consultant that help customers plan their travels."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "YYK Travel Pro")

demo.launch(share=True) 