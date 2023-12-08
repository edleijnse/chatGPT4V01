import tkinter as tk
from openai import OpenAI

client = OpenAI()
import json


class GPTAPI:
    def generate_answer(self, question):
        messages = [{"role": "user", "content": question}]
        try:
            response = client.chat.completions.create(model="gpt-4", messages=messages)
            return response.choices[0].message.content
        except Exception as e:
            return str(e)


class GPTGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GPT-4 GUI")
        self.api = GPTAPI()

        self.input_label = tk.Label(root, text="Enter your question:")
        self.input_label.pack()

        self.input_field = tk.Text(root, width=80, height=5)
        self.input_field.pack()

        self.output_label = tk.Label(root, text="Answer:")
        self.output_label.pack()

        self.output_field = tk.Text(root, height=30, width=80)
        self.output_field.pack()

        self.generate_button = tk.Button(root, text="Generate Answer", command=self.update_answer)
        self.generate_button.pack()

        self.clear_button = tk.Button(root, text="Clear Fields", command=self.clear_fields)
        self.clear_button.pack()

        # Adding Close button
        self.close_button = tk.Button(root, text="Close", command=self.root.quit)
        self.close_button.pack()

    def update_answer(self):
        question = self.input_field.get("1.0", tk.END).strip()
        answer = self.api.generate_answer(question)
        self.output_field.insert(tk.END, answer)

    def clear_fields(self):
        self.input_field.delete('1.0', tk.END)
        self.output_field.delete('1.0', tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = GPTGUI(root)
    root.mainloop()