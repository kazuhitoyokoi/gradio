import gradio as gr
import time

def generate(
    message: str,
    chat_history: list[dict],
):

    output = ""
    for character in message:
        output += character
        time.sleep(0.3)
        yield output


demo = gr.ChatInterface(
    fn=generate,
    examples=[
        ["Hey"],
        ["Can you explain briefly to me what is the Python programming language?"],
    ],
    cache_examples=True,
    cache_mode="lazy",
    type="messages",
)


if __name__ == "__main__":
    demo.launch()