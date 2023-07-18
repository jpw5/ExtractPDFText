import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog
import PyPDF2


def openFile():
    filename = filedialog.askopenfilename(title="Open PDF file",
                                          initialdir=r'C:\Users\kn849jw\PycharmProjects\Extract PDF Text',
                                          filetypes=[('PDF files', '*.pdf')])
    filename_label.configure(text=filename)
    output_file_text.delete("1.0", tk.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        output_file_text.insert(tk.END, current_text)


root = ctk.CTk()
root.resizable(0, 0)
root.title("PDF Text Extractor")

filename_label = ctk.CTkLabel(root, text="No File Selected")
output_file_text = tk.Text(root)
output_file_button = ctk.CTkButton(root, text="Open PDF File", command=openFile)

filename_label.pack()
output_file_text.pack()
output_file_button.pack()

root.mainloop()
