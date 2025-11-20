import gradio
from groq import Groq
client = Groq(
    #api_key="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",
)
def initialize_messages():
    return [{
        "role": "system",
        "content": """You are a highly experienced medical doctor with
        excellent clinical knowledge and years of successful patient care.
        Your role is to assist people by providing clear, accurate, and
        professional medical guidance based on general medical knowledge.
        Explain everything in simple and understandable language.
        Do NOT provide harmful or unsafe advice, and do not prescribe
        medications or treatments that require a physical examination.
        Always encourage users to consult a licensed medical professional
        for diagnosis or emergency situations."""
    }]
messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama-3.3-70b-versatile",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
iface = gradio.ChatInterface(
        customLLMBot,
        chatbot=gradio.Chatbot(height=300),
        textbox=gradio.Textbox(placeholder="Ask me any medical / health related question"),
        title="Doctor Assistance ChatBot",
        description="An AI medical assistant for general health guidance and information",
        theme="soft",
        examples=[
            "Hi",
            "I have a fever and body pain, what should I do?",
            "How to control high blood pressure?",
            "What are the symptoms of diabetes?"
        ]
)
