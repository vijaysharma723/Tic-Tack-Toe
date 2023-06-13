from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk
import sqlite3
from PIL import Image, ImageTk
from tkinter import messagebox

def reset_board():
    for button in button2boardDict:
        buttontextDict[button]['image'] = ""

    player1_entry.delete(0, 'end')
    player2_entry.delete(0, 'end')

    # reset the board
    for i in range(3):
        for j in range(3):
            board[i][j] = 9
    count[0] = 0

def check_winner():
    p1 = player1_entry.get()
    p2 = player2_entry.get()

    rows = [0,0,0]
    cols = [0,0,0]
    dia1 = 0
    dia2 = 0
    end = False

    for j in range(3):
        rows[0] += board[0][j]
        rows[1] += board[1][j]
        rows[2] += board[2][j]

    for i in range(3):
        cols[0] += board[i][0]
        cols[1] += board[i][1]
        cols[2] += board[i][2]

    dia1 = board[0][0] + board[1][1] + board[2][2]
    dia2 = board[0][2] + board[1][1] + board[2][0]

    for row in rows:
        if row == 0:
            player_won = messagebox.showinfo("WON!", p2 + " won the match!")
            end = True
        elif row == 3:
            player_won = messagebox.showinfo("WON!", p1 + " won the match!")
            end = True

    for col in cols:
        if col == 0:
            player_won = messagebox.showinfo("WON!", p2 + " won the match!")
            end = True

        elif col == 3:
            player_won = messagebox.showinfo("WON!", p1 + " won the match!")
            end = True

    if dia1 == 0:
        player_won = messagebox.showinfo("WON!", p2 + " won the match!")
        end = True

    elif dia1 == 3:
        player_won = messagebox.showinfo("WON!", p1 + " won the match!")
        end = True

    if dia2 == 0:
        player_won = messagebox.showinfo("WON!", p2 + " won the match!")
        end = True

    elif dia2 == 3:
        player_won = messagebox.showinfo("WON!", p1 + " won the match!")
        end = True

    if count[0] == 9 and end == False:
        match_tied_message = messagebox.showinfo("Tied!", "The match was tied!")
        end = True

    if end == True:
        reset_board()



    # if turn[0] == 0:
    #     target = 3
    #     winner = player1_entry.get()
    # else:
    #     target = 0
    #     winner = player2_entry.get()
    #
    # end = False
    #
    # # center cell
    # if i == 1 and j == 1:
    #     dia1 = board[0][0] + board[1][1] + board[2][2]
    #     dia2 = board[0][2] + board[1][1] + board[2][0]
    #     row = board[i][0] + board[i][1] + board[i][2]
    #     col = board[0][j] + board[1][j] + board[2][j]
    #
    #     if dia1 == target or dia2 == target or row == target or col == target:
    #         player_won = messagebox.showinfo("WON!", winner + " won the match!")
    #         end = True
    #
    # else:
    #
    #     row = board[i][0] + board[i][1] + board[i][2]
    #     col = board[0][j] + board[1][j] + board[2][j]
    #
    #     if row == target or col == target:
    #         player_won = messagebox.showinfo("WON!", winner + " won the match!")
    #         end = True
    #
    # if count[0] == 9 and end == False:
    #     match_tied_message = messagebox.showinfo("Tied!", "The match was tied!")
    #     end = True
    #
    # if end == True:
    #     reset_board()

def button_click(buttonNumber):


    if turn[0] == -1:
        response_errror_playername = messagebox.showerror("Error", "Click the start button!")
        return

    index = button2boardDict[buttonNumber]
    i = index[0]
    j = index[1]

    if board[i][j] == 9:
        if turn[0] == 0:
            # buttontextDict[buttonNumber]['text'] = 'X'
            buttontextDict[buttonNumber]['image'] = x_new_img[0]
            board[i][j] = 1
            count[0] += 1
            check_winner()
            turn[0] = 1

        elif turn[0] == 1:
            buttontextDict[buttonNumber]['image'] = o_new_img[0]
            board[i][j] = 0
            check_winner()
            count[0] += 1
            turn[0] = 0



    # if board[i][j] == None:
    #     messagebox.showinfo(title="button clicked", message="Button clicked == " + str(buttonNumber))

def validate_initializeTurn():

    player1_name = player1_entry.get()
    player2_name = player2_entry.get()

    if len(player1_name) == 0 or len(player2_name) == 0:
        response_errror_playername = messagebox.showerror("Error", "Enter the both names")
    else:
        welcome_msg = messagebox.showinfo(title="Welcome", message="Wecome " + player1_name + " and " + player2_name)
        turn[0] = 0

        ###### call to start the game from here ######


root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x600")
root.iconbitmap("images/game-controller-b_icon-icons.com_50382.ico")
root.resizable(height = False, width = False)
root_back = ImageTk.PhotoImage(Image.open("images/main_window_background.png"))
root_back_label = Label(root,image=root_back)
root_back_label.place(x=0, y=0, relheight=1, relwidth=1)

# a variable turn to track whose turn is it and count counts the number of turns
turn = [-1]
count = [0]

# board to write on and to verify the winner
board = []
for x in range(3):
    list1 = []
    for y in range(3):
        list1.append(9)
    board.append(list1)

# button number to coordinates mapping
button2boardDict = {1:[0,0] , 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2] }

buttontextDict = {}

x_org = Image.open("images/X.png")
x_resized = x_org.resize((60, 60), Image.ANTIALIAS)
x_new_img = [ImageTk.PhotoImage(x_resized)]

o_org = Image.open("images/O.png")
o_resized = o_org.resize((60, 60), Image.ANTIALIAS)
o_new_img = [ImageTk.PhotoImage(o_resized)]


# X and O buttons are defined and placed below
# Row 1
button1 = ttk.Button(root ,command=lambda m=1: button_click(m),)
button1.place(x=50, y=203, height = 100, width = 120)
buttontextDict[1] = button1

button2 = ttk.Button(root,command=lambda m=2: button_click(m))
button2.place(x=190, y=203, height = 100, width = 120)
buttontextDict[2] = button2

button3 = ttk.Button(root,command=lambda m=3: button_click(m))
button3.place(x=330, y=203, height = 100, width = 120)
buttontextDict[3] = button3

# Row 2
button4 = ttk.Button(root,command=lambda m=4: button_click(m))
button4.place(x=50, y=313, height = 100, width = 120)
buttontextDict[4] = button4

button5 = ttk.Button(root,command=lambda m=5: button_click(m))
button5.place(x=190, y=313, height = 100, width = 120)
buttontextDict[5] = button5

button6 = ttk.Button(root,command=lambda m=6: button_click(m))
button6.place(x=330, y=313, height = 100, width = 120)
buttontextDict[6] = button6

# Row 3
button7 = ttk.Button(root,command=lambda m=7: button_click(m))
button7.place(x=50, y=423, height = 100, width = 120)
buttontextDict[7] = button7

button8 = ttk.Button(root,command=lambda m=8: button_click(m))
button8.place(x=190, y=423, height = 100, width = 120)
buttontextDict[8] = button8

button9 = ttk.Button(root,command=lambda m=9: button_click(m))
button9.place(x=330, y=423, height = 100, width = 120)
buttontextDict[9] = button9

# player 1 and player2 entry field
player1_entry = ttk.Entry(root,width = 30)
player1_entry.place(x = 220, y = 17)

player2_entry = ttk.Entry(root,width = 30)
player2_entry.place(x = 220, y = 54)

play_button_img = Image.open("images/start_game_image.png")
play_button_img_resized = play_button_img.resize((150,150), Image.ANTIALIAS)

play_button_img_new = ImageTk.PhotoImage(play_button_img_resized)
# play_button_img = PhotoImage(file="start_game_image.png")
# play_button_img = play_button_img.resize((100, 100))


play_button = Button(root, image = play_button_img_new, borderwidth = 0, command = validate_initializeTurn )
play_button.place(x=200, y=100, height = 34, width = 85)



root.mainloop()

