import tkinter as tk
from tkinter import filedialog, ttk



class NotePad:
    def __init__(self, root):
        self.root = root
        self.root.title("Bob's NotePad")

        self.text_area = tk.Text(self.root, wrap="word", padx=5, pady=5, border=5, )
        self.text_area.pack(expand=True, fill="both")

        self.frame = tk.Frame(self.root)
        self.frame.pack()

        self.button_save = ttk.Button(self.frame, text="Save", command=self.save_file)
        self.button_save.pack(side="left")

        self.button_load = ttk.Button(self.frame, text="Load", command=self.load_file)
        self.button_load.pack(side="left")


    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])

        if file_path:

            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))

            self.root.title(file_path.split("/")[-1].split(".")[0])

            print(f"File saved to {file_path}")


    def load_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt")])

        if file_path:

            with open(file_path, "r") as file:
                the_text = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, the_text)

            self.root.title(file_path.split("/")[-1].split(".")[0])

            print(f"File loaded from {file_path}")


    def run(self):
        self.root.mainloop()


def main():
    root = tk.Tk()
    app = NotePad(root)
    app.run()


if __name__ == '__main__':
    main()
