# import the necessary stuff from tkinter, the module used for the gui
from tkinter import Tk, Text, Label, Button, END

# the slang list. the pipe characters are used for only replacing the words when they are on their own.
slang = {
    "|fr|": "|for real|",
    "|ur|": "|your|",
    "|u|": "|you|",
    "|lol|": "|haha|",
    "|bouta|": "|about to|",
    "|w|": "|good|",
    "|l|": "|bad|",
    "|rizz|": "|charisma|",
    "|bruh|": "|why|",
    "|idk|": "|i don\'t know|",
    "|cap|": "|lies|",
    "|slay|": "|awesome|",
    "|imma|": "|i\'m going to|",
    "|aight|": "|alright|",
    "|alr|": "|alright|",
    "|capping|": "|lying|",
    "|cappin|": "|lying|",
    "|bussin|": "|awesome|",
    "|omg|": "|oh my gosh|",
    "|ig|": "|i guess|",
    "|goat|": "|greatest of all time|",
    "|bc|": "|because|",
    "|nvm|": "|nevermind|",
    "|sec|": "|second|",
    "|r|": "|are|"
}

# translate the function by replacing the slang words with their non-slang counterparts
def translate():
    out.delete("1.0", END)
    text = inp.get("1.0", END)
    output = "|" + text.replace("\n", "|")
    output = output.replace(" ", "||")
    for i in slang:
        output = output.replace(i, slang[i])
    output = output.replace("||", " ")
    output = output.replace("|", " ")
    out.insert("1.0", output[1:])

# create the window
root = Tk()
root.title("text slang translator by birdfour!")
root.resizable(False, False)

# the input label
l = Label(root, text="input text to translate:", font="Arial 15")
l.pack()

# the input text box
inp = Text(root, width=50, height=10, padx=5, pady=5)
inp.pack()

# the translate button
b = Button(root, width=25, text="translate!", padx=5, pady=5, bg="#CCCCCC", relief="flat", font="Arial 10", command=translate)
b.pack()

# the output label
l2 = Label(root, text="translated text:", font="Arial 13")
l2.pack()

# the output text box
out = Text(root, width=50, height=5, padx=5, pady=5)
out.pack()

# make the program work
root.mainloop()
