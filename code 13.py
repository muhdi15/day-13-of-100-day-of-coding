import tkinter

root = tkinter.Tk()
root.config(bg="light blue")
root.title("INI ADALAH PROGRAM SEDERHANA PYTHON")
# root bagian window dari TK inter

label = tkinter.Label(text="PLEAS CLICK BUTTON TO RUN THE APP", font="Normal 25", bg = "light blue")
label.grid(row=1 , column=3 )
def youtube():
    import os
    os.system("start www.Youtube.com")
    os.system("msg * Youtube akan terbuka")
def whatsapp():
    import os

    os.system("Start https://web.whatsapp.com")
    os.system("msg * What'sapp akan terbuka")
    

tombol1 = tkinter.Button(font="normal 20" , text="Youtube", activebackground="light blue", command = youtube)
tombol2 = tkinter.Button(font="normal 20" , text="What'sapp", activebackground="light blue", command =whatsapp)
tombol2.grid(row=1 , column=1)
tombol1.grid(row=1 , column=2)
root.mainloop()
