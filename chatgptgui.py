import tkinter as tk
from openai import OpenAI

client = OpenAI()
import json

class GPTGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GPT-4 GUI")

        self.input_label = tk.Label(root, text="Enter your question:")
        self.input_label.pack()

        self.input_field = tk.Text(root, width=80, height=5)
        self.input_field.pack()

        self.output_label = tk.Label(root, text="Answer:")
        self.output_label.pack()

        self.output_field = tk.Text(root, height=30, width=80)
        self.output_field.pack()

        self.generate_button = tk.Button(root, text="Generate Answer", command=self.generate_answer)
        self.generate_button.pack()

        self.clear_button = tk.Button(root, text="Clear Fields", command=self.clear_fields)  # New clear button
        self.clear_button.pack()

    def generate_answer(self):
        question = self.input_field.get("1.0", tk.END).strip()
        messages = [{"role": "user", "content": question}]
        try:
            response = client.chat.completions.create(model="gpt-4", messages=messages)
            response_message = response.choices[0].message.content
            answer = response_message
        except Exception as e:
            answer = str(e)
        self.output_field.delete('1.0', tk.END)  # Clear previous output
        self.output_field.insert(tk.END, answer)
    def clear_fields(self):  # New method to clear fields
        self.input_field.delete('1.0', tk.END)
        self.output_field.delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GPTGUI(root)
    root.mainloop()
