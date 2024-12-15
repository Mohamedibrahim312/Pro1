import tkinter as tk
from tkinter import *
from tkinter import messagebox
from gtts import gTTS
import os

def play_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text,lang='en')
            tts.save("output.mp3")
            os.system("start output.mp3" if os.name == "nt" else "open output.mp3")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        else:
            messagebox.showwarning("Warning", "Please enter some text to play.")
           
def clear_text():
    text_entry.delete("1.0", tk.END)
    
def exit_app():
    root.destroy()
    
 #creat the main windows
root =tk.Tk()
root.title("Text to Speech") 
root.geometry("400x350")  
root.configure(bg= "#EEDFCC")


mylabel=Label(root,text="Enter Your Text ",font="blod",fg="gray")
mylabel.place(x=120, y=10)    
                     
#create a text entry widget
text_entry = tk.Text(root, wrap=tk.WORD,height=5, width=40)
text_entry.place(x=35,y=50)


#create buttons
#mybutton = ttk.Button(root,text="Play",command=play_text).pack(padx=100,pady=160)

play_button = tk.Button(root,text="Play",padx=10,pady=3,font="blod",fg="#EEDFCC",bg="white",command=play_text)
play_button.place(x=70,y=200)


set_button = tk.Button(root,text="Set",padx=10,pady=3,font="blod",fg="#EEDFCC",bg="white",command=clear_text)
set_button.place(x=170,y=200)


exit_button = tk.Button(root,text="exit",padx=10,pady=3,font="blod",fg="#EEDFCC",bg="white",command=exit_app)
exit_button.place(x=270,y=200)


#Run the app
root.mainloop()