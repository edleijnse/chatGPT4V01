import tkinter as tk
import openai
import json

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
API_KEY = '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'
openai.api_key = API_KEY

class GPTGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GPT-4 GUI")

        self.input_label = tk.Label(root, text="Enter your question:")
        self.input_label.pack()

        self.input_field = tk.Text(root,width=40, height=5)
        self.input_field.pack()

        self.output_label = tk.Label(root, text="Answer:")
        self.output_label.pack()

        self.output_field = tk.Text(root, height=30, width=40)
        self.output_field.pack()

        self.generate_button = tk.Button(root, text="Generate Answer", command=self.generate_answer)
        self.generate_button.pack()

    def generate_answer(self):
        question = self.input_field.get("1.0", tk.END).strip()
        messages = [{"role": "user", "content": question}]
        functions = [
            {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            }
        ]

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,

        )
        response_message = response["choices"][0]["message"]["content"]
        answer = response_message

        self.output_field.delete('1.0', tk.END)  # Clear previous output
        self.output_field.insert(tk.END, answer)

if __name__ == "__main__":
    root = tk.Tk()
    app = GPTGUI(root)
    root.mainloop()
