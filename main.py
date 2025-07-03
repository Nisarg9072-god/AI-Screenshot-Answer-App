import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import pytesseract
import google.generativeai as genai
import mss
from tkinter import messagebox

# --- SETUP ---
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
genai.configure(api_key="your_api_key_here")  # Replace with your actual API key
model = genai.GenerativeModel("gemini-2.0-flash-exp")

print(pytesseract.get_tesseract_version())

# --- Take Screenshot with MSS ---
def clear_all():
    question_box.delete("1.0", tk.END)
    answer_box.delete("1.0", tk.END)

def take_full_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        sct_img = sct.grab(monitor)
        img = Image.frombytes("RGB", sct_img.size, sct_img.rgb)
        return img, monitor

# --- Snipping Tool Class ---
class SnipTool:
    def __init__(self, full_img, monitor):
        self.full_img = full_img
        self.monitor = monitor
        self.start_x = self.start_y = None
        self.rect = None

        self.root = tk.Toplevel()
        self.root.geometry(f"{monitor['width']}x{monitor['height']}+{monitor['left']}+{monitor['top']}")
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.attributes("-transparentcolor", "black")

        self.canvas = tk.Canvas(self.root, cursor="cross", bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.tk_img = ImageTk.PhotoImage(full_img)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_img)

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_drag(self, event):
        self.canvas.coords(self.rect, self.start_x, self.start_y, event.x, event.y)

    def on_release(self, event):
        x1, y1 = min(self.start_x, event.x), min(self.start_y, event.y)
        x2, y2 = max(self.start_x, event.x), max(self.start_y, event.y)
        self.root.destroy()

        cropped = self.full_img.crop((x1, y1, x2, y2))
        cropped.save("screenshot.png")
        process_question_and_answer(cropped)


# --- Main Processing Logic ---
def process_question_and_answer(img):
    try:
        question_text = pytesseract.image_to_string(img).strip()
        if not question_text:
            raise ValueError("No question found in the image!")

        # Send to Gemini first (before updating UI)
        response = model.generate_content(
            f"Answer this question in a simple and understandable way:\n\n{question_text}"
        )
        answer_text = response.text.strip()

        # Update UI only after both question & answer are ready
        question_box.delete("1.0", tk.END)
        question_box.insert(tk.END, question_text)

        answer_box.delete("1.0", tk.END)
        answer_box.insert(tk.END, answer_text)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# --- Trigger from Button ---
def handle_screenshot():
    window.withdraw()
    img, monitor = take_full_screenshot()
    SnipTool(img, monitor)
    window.after(2000, lambda: window.deiconify())

def handle_enter_key():
    typed_question = entry_box.get().strip()
    if not typed_question:
        messagebox.showwarning("No Input", "Please type a question first.")
        return

    # Set the question in the Question Text box
    question_box.delete("1.0", tk.END)
    question_box.insert(tk.END, typed_question)

    # Ask Gemini
    try:
        response = model.generate_content(
            f"Answer this question in a simple and understandable way:\n\n{typed_question}"
        )
        answer_text = response.text.strip()
        answer_box.delete("1.0", tk.END)
        answer_box.insert(tk.END, answer_text)
    except Exception as e:
        messagebox.showerror("Error", f"Gemini failed to answer:\n{str(e)}")

    # Clear the entry field after processing
    entry_box.delete(0, tk.END)

# --- UI Window ---

BG_COLOR = "#1e1e1e"
FG_COLOR = "#ffffff"
BTN_COLOR = "#3a3a3a"
BTN_TEXT = "#ffffff"
HIGHLIGHT = "#007acc"
FONT = ("Segoe UI", 10)

window = tk.Tk()
window.title("AI Question Answer Helper")
window.geometry("400x400")
window.resizable(False, False)
window.configure(bg=BG_COLOR)
# --- Button Frame (Horizontal layout) ---
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=10)

tk.Button(button_frame, text="📷 Take Screenshot", command=handle_screenshot,
          bg=BTN_COLOR, fg=BTN_TEXT, font=FONT, activebackground=HIGHLIGHT,
          width=18, padx=10, pady=5).pack(side="left", padx=5)

tk.Button(button_frame, text="🧹 Clear All", command=clear_all,
          bg=BTN_COLOR, fg=BTN_TEXT, font=FONT, activebackground=HIGHLIGHT,
          width=12, padx=10, pady=5).pack(side="left", padx=5)

entry_label = tk.Label(window, text="📝 Ask a Question:", font=FONT, bg=BG_COLOR, fg=FG_COLOR)
entry_label.pack(anchor="w", padx=10)

entry_box = tk.Entry(window, font=FONT, bg="#2e2e2e", fg=FG_COLOR, insertbackground=FG_COLOR)
entry_box.pack(fill="x", padx=10, pady=(0, 10))
entry_box.bind("<Return>", lambda event: handle_enter_key())

tk.Label(window, text="📄 Question:", font=FONT, bg=BG_COLOR, fg=FG_COLOR).pack(anchor="w", padx=10)

question_box = scrolledtext.ScrolledText(window, height=6, wrap=tk.WORD,
                                         bg="#2e2e2e", fg=FG_COLOR, insertbackground=FG_COLOR,
                                         font=FONT)
question_box.pack(fill="both", padx=10, pady=(0, 10))

tk.Label(window, text="📄 Answer:", font=FONT, bg=BG_COLOR, fg=FG_COLOR).pack(anchor="w", padx=10)

answer_box = scrolledtext.ScrolledText(window, height=6, wrap=tk.WORD,
                                       bg="#2e2e2e", fg=FG_COLOR, insertbackground=FG_COLOR,
                                       font=FONT)
answer_box.pack(fill="both", padx=10, pady=(0, 10))


window.mainloop()
