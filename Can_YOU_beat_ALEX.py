#Import Modules
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
from random import randint
from PIL import Image, ImageTk
import pyautogui
import threading 
import random, playsound

#Functions for Main_menu
def save():
    try:
        myScreenshot = pyautogui.screenshot()
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        myScreenshot.save(file_path)
        quitApp()
    except:
        pass

def history():
    filepath = filedialog.askopenfilename(title="Open file okay?",filetypes= (("png files","*.png"),("all files","*.*")))
    img = Image.open(filepath)
    print(img)
    img.show()

def help():
    showinfo("Contact me", "upendra.gupta.7543@gmail.com")

def rules():
    showinfo("Rules", "You have to select Snake, Water or Gun \n\nIf you choose Snake and computer choose Water than Snake will drink the water and you will loose\nIf you choose Snake and computer choose Gun than Gun will kill the snake and you will loose\nIf you choose Water and computer choose Gun than Gun will drown in the water and you will win\n\nThis game have 5 rounds, after 5 rounds the winner will be declared")

def about():
    showinfo("Can YOU beat ALEX?", "Developed by Upendra Gupta")

def quitApp():
    root.destroy()

# main window
root = Tk()
root.title("Can YOU beat ALEX?")
root.configure(background="#9b59b6")
root.geometry("1660x960")
root.minsize(1660, 960)
root.maxsize(1660, 960)

#Icon
root.wm_iconbitmap("favicon.ico")

# root.wm_iconbitmap("img.ico")

# Menubar
MenuBar = Menu(root)

#Main_menu 
Main_menu = Menu(MenuBar, tearoff=0)
Main_menu.add_command(label="Rules", command=rules)
Main_menu.add_command(label="Save", command=save)
Main_menu.add_command(label="History", command=history)
Main_menu.add_command(label="Help", command=help)
Main_menu.add_command(label="About Developer", command=about)
Main_menu.add_command(label = "Exit", command = quitApp)
MenuBar.add_cascade(label="Menu", menu=Main_menu)

#Exit Menu

root.config(menu=MenuBar)

#Music

def winning_music():
    """
    Plays the winning music.
    """
    win_music  = ["anime wow.mp3", "bruhh.mp3"]
    try:
        playsound.playsound(random.choice(win_music))
    except Exception as e:
        print(e)

def losing_music():
    """
    Plays the losing music.
    """
    lose_music  = ["Nope.mp3", "Fart.mp3"]
    try:
       playsound.playsound(random.choice(lose_music))
    except Exception as e:
        print(e)

def tie_music():
    """
    Plays the tie music.
    """
    try:
        playsound.playsound("Awkward Cricket.mp3")
    except Exception as e:
        print(e)

# picture
snake_img = ImageTk.PhotoImage(Image.open("snake-user.png"))
gun_img = ImageTk.PhotoImage(Image.open("gun-user.png"))
water_img = ImageTk.PhotoImage(Image.open("water-user.png"))
snake_img_comp = ImageTk.PhotoImage(Image.open("snake.png"))
gun_img_comp = ImageTk.PhotoImage(Image.open("gun.png"))
water_img_comp = ImageTk.PhotoImage(Image.open("water.png"))
start_img_comp = ImageTk.PhotoImage(Image.open("start.png"))
won_img_comp = ImageTk.PhotoImage(Image.open("won.png"))
loss_img_comp = ImageTk.PhotoImage(Image.open("loss.png"))

#Result Gun shrink gif 
file1="gun_shrink.gif"
info1 = Image.open(file1)
# gives total number of frames that gif contains
frames1 = info1.n_frames  
# creating list of PhotoImage objects for each frames
im1 = [PhotoImage(file=file1,format=f"gif -index {i}") for i in range(frames1)]
count1 = 0
anim1 = None
def animation1(count1):
    try:
        global anim1
        im2 = im1[count1]

        gif_label.configure(image=im2)
        count1 += 1
        # if count == frames:
        #     count = 0
        anim1 = root.after(500,lambda :animation1(count1))
    except:
        pass
gif_label = Label(root,image="")
gif_label.grid(row=1, column=2)


#Result Gun killing snake gif 
file2="gun_killing_snake.gif"
info2 = Image.open(file2)
# gives total number of frames that gif contains
frames2 = info2.n_frames  
# creating list of PhotoImage objects for each frames
im2 = [PhotoImage(file=file2,format=f"gif -index {i}") for i in range(frames2)]
count2 = 0
anim2 = None
def animation2(count2):
    try:
        global anim2
        im3 = im2[count2]

        gif_label.configure(image=im3)
        count2 += 1
        # if count == frames:
        #     count = 0
        anim2 = root.after(500,lambda :animation2(count2))
    except:
        pass
gif_label = Label(root,image="")
gif_label.grid(row=1, column=2)



#Result Snake drinking water gif 
file3="snake_drinking_water.gif"
info3 = Image.open(file3)
# gives total number of frames that gif contains
frames3 = info3.n_frames  
# creating list of PhotoImage objects for each frames
im3 = [PhotoImage(file=file3,format=f"gif -index {i}") for i in range(frames3)]
count3 = 0
anim3 = None
def animation3(count3):
    try:
        global anim3
        im4 = im3[count3]

        gif_label.configure(image=im4)
        count3 += 1
        # if count == frames:
        #     count = 0
        anim3 = root.after(500,lambda :animation3(count3))
    except:
        pass
gif_label = Label(root,image="")
gif_label.grid(row=1, column=2)




#Result draw gif 
file4="draw.gif"
info4 = Image.open(file4)
# gives total number of frames that gif contains
frames4 = info4.n_frames  
# creating list of PhotoImage objects for each frames
im4 = [PhotoImage(file=file4,format=f"gif -index {i}") for i in range(frames4)]
count4 = 0
anim4 = None
def animation4(count4):
    try:
        global anim4
        im5 = im4[count4]

        gif_label.configure(image=im5)
        count4 += 1
        # if count == frames:
        #     count = 0
        anim4 = root.after(500,lambda :animation4(count4))
    except:
        pass
gif_label = Label(root,image="")
gif_label.grid(row=1, column=2)

# insert picture
user_label = Label(root, image=start_img_comp, bg="#9b59b6")
comp_label = Label(root, image=start_img_comp, bg="#9b59b6")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=4)

# scores
computerScore = Label(root, text=0, font="lucida 60 bold", bg="#9b59b6", fg="white")
playerScore = Label(root, text=0, font="lucida 60 bold", bg="#9b59b6", fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# indicators
comp_indicator = Label(root, font="lucida 50 bold", text="ALEX", bg="#9b59b6", fg="white")
vs = Label(root, font="lucida 60 bold", text=" VS ", bg="#9b59b6", fg="white")
user_indicator = Label(root, font="lucida 50 bold", text=" YOU", bg="#9b59b6", fg="white")
comp_indicator.grid(row=0, column=1)
vs.grid(row=0, column=2)
user_indicator.grid(row=0, column=3)

#empty line
l1 = Label(root, text='\n', bg='#9b59b6')
l1.grid(row=4, column=2)

# messages
msg = Label(root, font="lucida 20 bold", bg="#9b59b6", fg="white")
msg.grid(row=3, column=2)


# update message
def updateMessage(x):
    msg['text'] = x

# update user score


def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score


def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

def winner():
    if int(playerScore["text"])+int(computerScore["text"])==5:
        comp_indicator = Label(root, font="lucida 20 bold", text="Game Over", bg="#9b59b6", fg="white")
        comp_indicator.grid(row=8, column=2)
        if int(playerScore["text"])>int(computerScore["text"]):
            comp_indicator = Label(root, font="lucida 20 bold", text="You Won the Match", bg="#9b59b6", fg="white")
            comp_indicator.grid(row=8, column=2)
            comp_label = Label(root, image=won_img_comp, bg="#9b59b6")
            comp_label.grid(row=11, column=2)
            start_time = threading.Timer(5,save)
            start_time.start()
            

        elif int(playerScore["text"])<int(computerScore["text"]):
            comp_indicator = Label(root, font="lucida 20 bold", text="You Loose the Match", bg="#9b59b6", fg="white")
            comp_indicator.grid(row=8, column=2)
            comp_label = Label(root, image=loss_img_comp, bg="#9b59b6")
            comp_label.grid(row=11, column=2)
            start_time = threading.Timer(5,save)
            start_time.start()
                      
        elif int(playerScore["text"])==int(computerScore["text"]):
            comp_indicator = Label(root, font="lucida 20 bold", text="Match Draw", bg="#9b59b6", fg="white")
            comp_indicator.grid(row=8, column=2)
            comp_label = Label(root, image=loss_img_comp, bg="#9b59b6")
            comp_label.grid(row=11, column=2)
            start_time = threading.Timer(5,save)
            start_time.start()
            
    else:
        pass

    
# check winner

def checkWin(player, computer):
    if player == computer:
        updateMessage("Its a tie\n !Alex and you selected same!")
        animation4(count4)
        winner()
        start_time = threading.Timer(0.5,tie_music)
        start_time.start()
        
    elif player == "snake":
        if computer == "gun":
            updateMessage("You loose\n Snake was killed by the gun")
            updateCompScore()
            animation2(count2)
            winner()
            start_time = threading.Timer(0.5,losing_music)
            start_time.start()
        
        else:
            updateMessage("!You Win!\n Snake drinks the whole water")
            updateUserScore()
            animation3(count3)
            winner()
            start_time = threading.Timer(0.5,winning_music)
            start_time.start()
    elif player == "gun":
        if computer == "water":
            updateMessage("You loose\n Gun was drowned in the water")
            updateCompScore()
            animation1(count1)
            winner()
            start_time = threading.Timer(0.5,losing_music)
            start_time.start()
        
        else:
            updateMessage("You Win\n Snake was killed by the Gun")
            updateUserScore()
            animation2(count2)
            winner()
            start_time = threading.Timer(0.5,winning_music)
            start_time.start()
    elif player == "water":
        if computer == "snake":
            updateMessage("!You loose!\n Snake drinks the whole water")
            updateCompScore()
            animation3(count3)
            winner()
            start_time = threading.Timer(0.5,losing_music)
            start_time.start()
        
        else:
            updateMessage("You win\n Gun was drowned in the water")
            updateUserScore()
            animation1(count1)
            winner()
            start_time = threading.Timer(0.5,winning_music)
            start_time.start()

    else:
        pass


# update choices

choices = ["snake", "gun", "water"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "snake":
        comp_label.configure(image=snake_img_comp)
    elif compChoice == "gun":
        comp_label.configure(image=gun_img_comp)
    else:
        comp_label.configure(image=water_img_comp)


# for user
    if x == "snake":
        user_label.configure(image=snake_img)
    elif x == "gun":
        user_label.configure(image=gun_img)
    else:
        user_label.configure(image=water_img)

    checkWin(x, compChoice)

# buttons
snake = Button(root, width=20, height=2, font="lucida 14 bold", text="SNAKE",
              bg="#00ff00", fg="white", command=lambda: updateChoice("snake")).grid(row=6, column=1)
water = Button(root, width=20, height=2, font="lucida 14 bold", text="WATER",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoice("water")).grid(row=6, column=2)
gun = Button(root, width=20, height=2, font="lucida 14 bold", text="GUN",
               bg="#FAD02E", fg="white", command=lambda: updateChoice("gun")).grid(row=6, column=3)

root.mainloop()
