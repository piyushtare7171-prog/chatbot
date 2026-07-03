from transformers import pipeline

chatbot = pipeline(
    "text-generation",
    model="gpt2"
)

def get_response(text):
    result = chatbot(
        text,
        max_new_tokens=80,
        do_sample=True,
        temperature=0.7
    )

    return result[0]["generated_text"]
