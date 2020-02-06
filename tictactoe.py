import turtle
import ai

playMode = "2player"  # "1player" for human vs. AI OR "2player" for human vs. human
playing = False
windowSize = 600
boxSize = windowSize / 3
boxes = {
    "TopLeft": [],
    "TopMiddle": [],
    "TopRight": [],
    "MiddleLeft": [],
    "Middle": [],
    "MiddleRight": [],
    "BottomLeft": [],
    "BottomMiddle": [],
    "BottomRight": []
}
activePlayer = "x"
board = {
    "TopLeft": "",
    "TopMiddle": "",
    "TopRight": "",
    "MiddleLeft": "",
    "Middle": "",
    "MiddleRight": "",
    "BottomLeft": "",
    "BottomMiddle": "",
    "BottomRight": ""
}


def drawboard(t):
    t.pensize(1)
    t.color("black")
    for i in range(1, 3):
        t.penup()
        t.goto(i * windowSize / 3, 0)
        t.pendown()
        t.goto(i * windowSize / 3, windowSize)
    for i in range(1, 3):
        t.penup()
        t.goto(0, i * windowSize / 3)
        t.pendown()
        t.goto(windowSize, i * windowSize / 3)


def createboxes():
    y = 0
    x = 0
    for box in boxes:
        if x >= 3:
            x = 0
            y += 1
        minx = x * boxSize
        maxx = (x + 1) * boxSize
        miny = y * boxSize
        maxy = (y + 1) * boxSize
        boxes[box] = [minx, maxx, miny, maxy]
        x += 1


def play(x, y):
    global activePlayer
    global playing
    global playMode
    if playing:
        for box in boxes:
            if boxes[box][0] < x < boxes[box][1] and boxes[box][2] < y < boxes[box][3] and board[box] == "":
                if playMode == "2player":
                    if activePlayer == "x":
                        drawx(pen, box)
                        board[box] = "x"
                        activePlayer = "o"
                    else:
                        drawo(pen, box)
                        board[box] = "o"
                        activePlayer = "x"
                    checkwin()
                else:
                    if activePlayer == "x":
                        drawx(pen, box)
                        board[box] = "x"
                        checkwin()
                        activePlayer = "o"
                        computerplay()
    else:
        pen.clear()
        displaymenu()
        # check click and set playMode  pen.goto(windowSize/3 - 75, windowSize/2)

        if windowSize/3 - 75 < x < windowSize/3 + 75 and windowSize/2 - 25 < y < windowSize/2 + 25:
            playMode = "1player"
            setupgame()
        elif 2 * windowSize/3 - 75 < x < 2 * windowSize/3 + 75 and windowSize/2 - 25 < y < windowSize/2 + 25:
            playMode = "2player"
            setupgame()

        
        


def drawx(t, box):
    t.pensize(10)
    t.color("royal blue")
    t.penup()
    t.goto(boxes[box][0] + 20, boxes[box][2] + 20)
    t.pendown()
    t.goto(boxes[box][1] - 20, boxes[box][3] - 20)
    t.penup()
    t.goto(boxes[box][1] - 20, boxes[box][2] + 20)
    t.pendown()
    t.goto(boxes[box][0] + 20, boxes[box][3] - 20)


def drawo(t, box):
    t.pensize(10)
    t.color("tomato")
    t.penup()
    t.goto(boxes[box][0] + boxSize / 2, boxes[box][2] + 20)
    t.pendown()
    t.circle(80)


def checkwin():
    # "TopLeft" "TopMiddle" "TopRight" "MiddleLeft" "Middle" "MiddleRight" "BottomLeft"
    # "BottomMiddle" "BottomRight"
    global board
    # horizontal wins
    if (board["TopLeft"] == "x" or board["TopLeft"] == "o") and board["TopMiddle"] == board["TopLeft"] and \
            board["TopRight"] == board["TopLeft"]:
        drawwinner(board["TopLeft"], "TopLeft", "TopRight", pen)
    if (board["MiddleLeft"] == "x" or board["MiddleLeft"] == "o") and board["Middle"] == board["MiddleLeft"] and \
            board["MiddleRight"] == board["MiddleLeft"]:
        drawwinner(board["MiddleLeft"], "MiddleLeft", "MiddleRight", pen)
    if (board["BottomLeft"] == "x" or board["BottomLeft"] == "o") and board["BottomMiddle"] == board["BottomLeft"] and \
            board["BottomRight"] == board["BottomLeft"]:
        drawwinner(board["BottomLeft"], "BottomLeft", "BottomRight", pen)

    # vertical wins
    if (board["TopLeft"] == "x" or board["TopLeft"] == "o") and board["MiddleLeft"] == board["TopLeft"] and \
            board["BottomLeft"] == board["TopLeft"]:
        drawwinner(board["TopLeft"], "TopLeft", "BottomLeft", pen)
    if (board["TopMiddle"] == "x" or board["TopMiddle"] == "o") and board["Middle"] == board["TopMiddle"] and \
            board["BottomMiddle"] == board["TopMiddle"]:
        drawwinner(board["TopMiddle"], "TopMiddle", "BottomMiddle", pen)
    if (board["TopRight"] == "x" or board["TopRight"] == "o") and board["MiddleRight"] == board["TopRight"] and \
            board["BottomRight"] == board["TopRight"]:
        drawwinner(board["TopRight"], "TopRight", "BottomRight", pen)

    # diagonal wins
    if (board["TopLeft"] == "x" or board["TopLeft"] == "o") and board["Middle"] == board["TopLeft"] and \
            board["BottomRight"] == board["TopLeft"]:
        drawwinner(board["TopLeft"], "TopLeft", "BottomRight", pen)
    if (board["TopRight"] == "x" or board["TopRight"] == "o") and board["Middle"] == board["TopRight"] and \
            board["BottomLeft"] == board["TopRight"]:
        drawwinner(board["TopRight"], "TopRight", "BottomLeft", pen)

    if checkemptyspaces() == 0:
        drawwinner("draw", "TopLeft", "TopRight", pen)


def checkemptyspaces():
    emptyspaces = 0
    for space in board.values():
        if space == "":
            emptyspaces += 1

    return emptyspaces


def drawwinner(winner, box1, box2, t):
    global playing
    if winner == "draw":
        t.color("black")
        t.penup()
        t.goto(windowSize / 2, windowSize / 2)
        t.pendown()
        style = ('Courier', 70, 'bold')
        t.write(winner.capitalize() + "!!!", font=style, align='center')
        t.penup()
    else:
        t.pensize(40)
        if winner == "x":
            t.color("royal blue")
        else:
            t.color("tomato")
        t.penup()
        t.goto(boxes[box1][0] + boxSize/2, boxes[box1][2] + boxSize/2)
        t.pendown()
        t.goto(boxes[box2][0] + boxSize/2, boxes[box2][2] + boxSize/2)
        t.color('black')
        t.pensize(3)
        t.penup()
        t.goto(windowSize/2, windowSize/2)
        t.pendown()
        style = ('Courier', 70, 'bold')
        t.write(winner.capitalize() + "'s Win!!!", font=style, align='center')
        t.penup()
    playing = False


def computerplay():
    global activePlayer
    numberboard = convertboard()
    box = ai.getbestplay(numberboard)
    if box == "none":
        print("error")
    else:
        drawo(pen, box)
        board[box] = "o"
        checkwin()
        activePlayer = "x"


def convertboard():
    numberboard = board.copy()
    for box in board:
        if board[box] == "x":
            numberboard[box] = -1
        elif board[box] == "o":
            numberboard[box] = +1
    return numberboard


def setupgame():
    global boxes
    global activePlayer
    global board
    global playing

    playing = True
    boxes = {
        "TopLeft": [],
        "TopMiddle": [],
        "TopRight": [],
        "MiddleLeft": [],
        "Middle": [],
        "MiddleRight": [],
        "BottomLeft": [],
        "BottomMiddle": [],
        "BottomRight": []
    }
    activePlayer = "x"
    board = {
        "TopLeft": "",
        "TopMiddle": "",
        "TopRight": "",
        "MiddleLeft": "",
        "Middle": "",
        "MiddleRight": "",
        "BottomLeft": "",
        "BottomMiddle": "",
        "BottomRight": ""
    }

    pen.clear()
    drawboard(pen)

    createboxes()


def displaymenu():
    pen.penup()
    pen.goto(windowSize/2, 100)
    pen.pendown()
    pen.color("royal blue")
    style = ('Courier', 50, 'bold')
    pen.write("Tic Tac Toe AI", font=style, align='center')
    pen.penup()
    pen.goto(windowSize/3 - 75, windowSize/2)
    pen.down()
    pen.color("tomato")
    pen.fillcolor("tomato")
    pen.begin_fill()
    for i in range(0,2):
        pen.forward(150)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(2 * windowSize/3 - 75, windowSize/2)
    pen.down()
    pen.begin_fill()
    for i in range(0,2):
        pen.forward(150)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.color("white")
    pen.goto(windowSize/3, windowSize/2 - 10)
    pen.down()
    style = ('Courier', 20, 'bold')
    pen.write("1 Player", font=style, align='center')
    pen.penup()
    pen.goto(2 * windowSize/3, windowSize/2 - 10)
    pen.down()
    pen.write("2 Player", font=style, align='center')
    
    


    


screen = turtle.Screen()
screen.screensize(windowSize, windowSize)
screen.title("Tic Tac Toe AI")
screen.bgcolor("white")
screen.setworldcoordinates(0, windowSize, windowSize, 0)

pen = turtle.Turtle()
pen.speed("fastest")
pen.color("black")

displaymenu()

screen.onclick(play)

screen.mainloop()
