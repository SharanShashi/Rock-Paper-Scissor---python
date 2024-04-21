from tkinter import *
from PIL import Image, ImageTk
from random import randint 

window = Tk()
window.title("Game Rock paper and scissor")
window.configure(background="black")
window.geometry("1400x500")  # Fixed window size

# Load and resize images
image_size = (150, 150)  # Set the size for all images
image_rock1 = ImageTk.PhotoImage(Image.open("rock 1.png").resize(image_size))
image_paper1 = ImageTk.PhotoImage(Image.open("paper 1.png").resize(image_size))
image_scissor1 = ImageTk.PhotoImage(Image.open("scissor1.png").resize(image_size))
image_rock2 = ImageTk.PhotoImage(Image.open("rock 2.png").resize(image_size))
image_paper2 = ImageTk.PhotoImage(Image.open("paper 2.png").resize(image_size))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor2.png").resize(image_size))

# Create labels for images
label_player = Label(window, image=image_scissor1)
label_computer = Label(window, image=image_scissor2)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

# Create labels for scores
computer_score = Label(window,text=0,font=('arial',60,"bold"),fg="red")
player_score = Label(window,text=0,font=('arial',60,"bold"),fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)

# Create labels for indicators
player_indicator = Label(window,font=("arial",40,"bold"),text="PLAYER",bg="orange",fg="blue")
computer_indicator = Label(window,font=("arial",40,"bold"),text="COMPUTER",bg="orange",fg="blue")
computer_indicator.grid(row=0,column=1)
player_indicator.grid(row=0,column=3)

# Function to update message
def updateMessage(a):
    final_message['text'] = a

# Function to update computer score
def Computer_Update():
    final = int(computer_score['text'])
    final += 1
    computer_score["text"] = str(final)

# Function to update player score
def player_Update():
    final = int(player_score['text'])
    final += 1
    player_score["text"] = str(final)

# Function to check the winner
def winner_check(p, c):
    if p == c:
        updateMessage("It's a tie")
    elif p == "rock":
        if c == "paper":
            updateMessage("Computer Wins !!")
            Computer_Update()
        else:
            updateMessage("Player Wins !!")
            player_Update()
    elif p == "paper":
        if c == "scissor":
            updateMessage("Computer Wins !!")
            Computer_Update()
        else:
            updateMessage(" PLAYER WINS !!")
            player_Update()
    elif p == "scissor":
        if c == "rock":
            updateMessage("Computer Wins !!")
            Computer_Update()
        else:
            updateMessage("Player Wins !!")
            player_Update()
    else:
        pass

To_select = ["rock", "paper", "scissor"]

# Function to update choice and check the winner
def choice_update(a):
    choice_computer = To_select[randint(0, 2)]
    if choice_computer == "rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)

    if a == "rock":
        label_player.configure(image=image_rock1)
    elif a == "paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)

    winner_check(a, choice_computer)

# Create label for final message
final_message = Label(window,font=("arial",40,"bold"),bg="red",fg="white")
final_message.grid(row=3,column=2)

# Create buttons for choices with fixed width
button_rock = Button(window,width=16,height=3,text="Rock",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock"))
button_rock.grid(row=2,column=1)

button_paper = Button(window,width=16,height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper"))
button_paper.grid(row=2,column=2)

button_scissor = Button(window,width=16,height=3,text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissor"))
button_scissor.grid(row=2,column=3)

window.mainloop()
