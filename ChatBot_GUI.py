
#Description : This is a python program GUI for a chat bot

#Library
from tkinter import *

#Create the tkinter object (this represents the parent window)
root = Tk()

#A title for the parent window
root.title('Chat Bot')

#Give the parent window some dimensions/geometry
root.geometry('400x500')

#Create a main menu
main_menu = Menu(root)

#Create teh submenu
file_menu = Menu(root)

#Add commands to the submenu
file_menu.add_command(label='New..')
file_menu.add_command(label='Save As..')
file_menu.add_command(label='Exit')

# Add the File drop down sub menus and other menus to the main menu
main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu = main_menu)

#Create a window for the chat  ** CHAT WINDOW**
chatWindow = Text(root, bd=1, bg = 'black', width='50', height='8')
chatWindow.place(x=6, y=6, height= 385, width=370)

#Create the text area to enter a message   **MESSAGE WINDOW***
messageWindow = Text(root , bg = 'black', width ='30', height='4', font=('Arial', 23), foreground= 'blue')
messageWindow.place(x = 128, y= 400, height= 88, width = 260)

#Create the button    ***BUTTON ***
Button = Button(root,text= 'Send', bg= 'blue', activebackground = 'green', font=('Arial', 12), width='12', height='5')
Button.place(x=6, y=400, height = 88, width = 120)

#Create scrollbar         **SCROLL BAR ***
scrollbar = Scrollbar(root, command = chatWindow.yview)
scrollbar.place(x=375, y=5, height = 385)

root.mainloop()
