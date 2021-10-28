import pygame as p
import initializer
import Chaal
Dimensions=8
sq_size=560/Dimensions
iin=initializer.Board()
Images={}
clk=check_count=0
queening=check_mate=0
rec=[]
white_all_moves=black_all_moves=[]
kblack_in_check=kwhite_in_check=False
raider=""
blacks=[]
whites=[]
wk=[[7,3]]
bk=[[0,4]]
special_moves=[]
w_l_rock=w_r_rock=w_k_c=b_l_rock=b_r_rock=b_k_c=c_w_check=c_b_check=True
pos=[]
team={"bR":"team1","bN":"team1","bB":"team1","bQ":"team1","bK":"team1","bP":"team1","wR":"team2","wN":"team2","wB":"team2","wK":"team2","wQ":"team2","wP":"team2"}
turn=team["wR"]
legal_moves=[]
gather={"wP": [False,"wP"], "bR": [ False,"bR"],
         "bB": [False,"bB"], "bN": [True,"bN"],
         "bQ": [False,"bQ"], "bK": [False,"bK"],
         "bP": [False,"bP"],  "wR": [False,"wR"],
         "wB": [False,"wB"], "wN": [True,"wN"],
         "wQ": [False,"wQ"],  "wK": [False,"wK"]}


def loading_images():
    pieces = ["bP","bR","bB","bN","bQ","bK","wP","wR","wB","wN","wQ","wK","prompt","chess_board","q_stool","frame"]
    for pices in pieces:
        Images[pices]=p.image.load(pices+".png")

def inform_check(screen):
    global kblack_in_check,kwhite_in_check
    font = p.font.Font('freesansbold.ttf', 32)
    text = font.render('Check..!!', True, p.Color("red"))
    textRect = text.get_rect()
    textRect.center = (350, 40)
    if kblack_in_check:
        screen.blit(text, textRect)
        screen.blit(Images["bK"], p.Rect(420, -5, 140, 140))
    if kwhite_in_check:
        screen.blit(text, textRect)
        screen.blit(Images["wK"], p.Rect(420, -5, 140, 140))
def Checkmate(white,black,count):
    global  blacks,whites,check_mate
    np=ek=do=0

    if white==1:
        if count==1:
            q = Chaal.andaza(False, wk[-1][0], wk[-1][1], "wK", iin, 0, [])
            for i in q:
                if i not in blacks:
                    ek = 1
                    if i in blacks:
                        ek=0
            try:
                blacks.remove([wk[-1][0], wk[-1][1]])
            except ValueError:
                pass
            for i in blacks:
                if i in white_all_moves:
                    do+=1
            print(ek,do)
            if ek == 0 and do == 0:
                check_mate=1

        else:
            q = Chaal.andaza(False, wk[-1][0], wk[-1][1], "wK", iin, 0, [])
            for i in q:
                if i not in blacks:
                    np = 1
            if np!= 1:
                check_mate=1
    else:
        if count==1:
            q = Chaal.andaza(False, bk[-1][0], bk[-1][1], "bK", iin, 0, [])
            for i in q:
                if i not in whites:
                    ek = 1
            try:
                whites.remove([wk[-1][0], wk[-1][1]])
            except ValueError:
                pass
            for i in blacks:
                if i not in black_all_moves:
                    do += 1
            print(ek,do)
            if ek == 0 and do == 0:
                check_mate=1
        else:
            q = Chaal.andaza(False, bk[-1][0], bk[-1][1], "bK", iin, 0, [])
            for i in q:
                if i not in whites:
                    np = 1
                    print(i)
            if np != 1:
                check_mate=1

def drawing_board(screen):
    global queening
    font = p.font.Font('freesansbold.ttf', 60)
    text = font.render('Checkmate', True, p.Color("red"))
    textRect = text.get_rect()
    textRect.center = (500,500)
    screen.fill(p.Color("darkgrey"))
    screen.blit(Images["chess_board"], p.Rect(70,70,400,400))
    inform_check(screen)
    if check_mate == 1:
        screen.fill(p.Color("white"))
        screen.blit(text, textRect)
        turning=True
        while turning:
            for eve in p.event.get():
                if eve.type == p.KEYDOWN:
                    turning=False
            p.display.flip()
        exit(1)



def drawing_pieces(screen,board):
    for r in range(Dimensions):
        for c in range(Dimensions):
            piece = board[c][r]
            prmt=iin.prpmt[c][r]
            if piece != "--":
                screen.blit(Images[piece],p.Rect(((r + 2) * sq_size)-4, ((c + 2) * sq_size) - 6, sq_size - 10, sq_size - 10))
            if prmt == "prompt":
                screen.blit(Images[prmt],
                            p.Rect(((r + 2) * sq_size) + 22, ((c + 2) * sq_size) +22, sq_size - 10, sq_size - 10))
            elif prmt == "frame":
                screen.blit(Images[prmt],
                            p.Rect(((r + 2) * sq_size) -13, ((c + 2) * sq_size)-13 ,82,82))


def Queening(screen,row,col,peice):
    if team[peice]=="team1":
        screen.blit(Images["q_stool"], p.Rect(925, 240, 70, 70))
        screen.blit(Images["bQ"], p.Rect(930, 270, 70, 70))
        screen.blit(Images["bR"], p.Rect(930, 340, 70, 70))
        screen.blit(Images["bN"], p.Rect(930, 410, 70, 70))
        screen.blit(Images["bB"], p.Rect(930, 480, 70, 70))
    else:
        screen.blit(Images["q_stool"], p.Rect(925, 240, 70, 70))
        screen.blit(Images["frame"], p.Rect(920, 260, 70, 70))
        screen.blit(Images["wQ"], p.Rect(930, 270, 70, 70))
        screen.blit(Images["frame"], p.Rect(920, 340, 70, 70))
        screen.blit(Images["wR"], p.Rect(930, 345, 70, 70))
        screen.blit(Images["frame"], p.Rect(920, 420, 70, 70))
        screen.blit(Images["wN"], p.Rect(930, 425, 70, 70))
        screen.blit(Images["frame"], p.Rect(920, 500, 70, 70))
        screen.blit(Images["wB"], p.Rect(930, 505, 70, 70))
    move_queening = True
    while move_queening:
        for event in p.event.get():
            if event.type == p.MOUSEBUTTONDOWN:
                loc = p.mouse.get_pos()
                x = loc[0]
                y = loc[1]
                if 920 <= x <= 990 and 260 <= y <= 330:
                    move_queening = False
                    if peice == "wP":
                        iin.brd[row][col]="wQ"
                    else:
                        iin.brd[row][col]="bQ"
                    queening = 0
                elif 920 <= x <= 990 and 340 <= y <= 410:
                    move_queening = False
                    if peice == "wP":
                        iin.brd[row][col]="wR"
                    else:
                        iin.brd[row][col]="bR"
                    queening = 0
                elif 920 <= x <= 990 and 420 <= y <= 490:
                    move_queening = False
                    if peice == "wP":
                        iin.brd[row][col]="wN"
                    else:
                        iin.brd[row][col]="bN"
                    queening = 0
                elif 920 <= x <= 990 and 500 <= y <= 570:
                    move_queening = False
                    if peice == "wP":
                        iin.brd[row][col]="wB"
                    else:
                        iin.brd[row][col]="bB"
                    queening = 0
                else:
                    continue
        p.display.flip()


def event_manger(piece,row,col,screen):
    global clk,turn,castle,legal_moves,raider,pos,rec,wk,w_l_rock,w_r_rock,w_k_c,b_k_c,c_w_check,c_b_check,b_l_rock,b_r_rock,special_moves,queening

    if (clk==1 and piece == "--") or (clk == 1 and team[piece]!=turn):
        clk=0
    elif clk==1:
        rec=[piece,[row,col]]
        raider=piece
        pos=[row,col]
        legal_moves = Chaal.andaza(gather[piece][0], row, col, gather[piece][1],iin,0,[])
        if raider=="wK":
            if w_k_c and w_l_rock and iin.brd[row][col-1] =="--" and iin.brd[row][col-2] == "--" and c_w_check:
                legal_moves.append([row,col-2])
                special_moves=[[row,col-2]]
            if w_k_c and w_r_rock and iin.brd[row][col+1]=="--" and iin.brd[row][col+2]=="--" and iin.brd[row][col+3] =="--" and c_w_check:
                legal_moves.append([row,col+2])
                special_moves.append([row,col+2])
        if raider=="bK":
            if b_k_c and b_l_rock and iin.brd[row][col-1] =="--" and iin.brd[row][col-2] == "--"and iin.brd[row][col-3]=="--" and c_b_check:
                legal_moves.append([row,col-2])
                special_moves=[[row,col-2]]
            if b_k_c and b_r_rock and iin.brd[row][col+1]=="--" and iin.brd[row][col+2]=="--"  and c_b_check:
                legal_moves.append([row,col+2])
                special_moves.append([row,col+2])
        iin.prpmt[row][ col] = "frame"
        for i in legal_moves:
            iin.prpmt[i[0]][i[1]]="prompt"
        for i in special_moves:
            iin.prpmt[i[0]][i[1]]="prompt"
    else:
        clk=0
        if [row, col] in special_moves:
            if [row, col] == [7, 1]:
                iin.brd[7][0] = "--"
                iin.brd[7][1] = "wK"
                iin.brd[7][2] = "wR"
                iin.brd[7][3] = "--"
                iin.log.append(["wR",[7,0],"--",[7,2]])
                iin.log.append(["wK", [7, 3], "--", [7, 1]])
            elif [row, col] == [7, 5]:
                iin.brd[7][3] = "--"
                iin.brd[7][5] = "wK"
                iin.brd[7][4] = "wR"
                iin.brd[7][7] = "--"
                iin.brd[7][6] = "--"
                iin.log.append(["wR", [7, 7], "--", [7, 4]])
                iin.log.append(["wK", [7, 3], "--", [7, 5]])
            elif [row, col] == [0, 2]:
                iin.brd[0][0] = "--"
                iin.brd[0][1] = "--"
                iin.brd[0][2] = "bK"
                iin.brd[0][3] = "bR"
                iin.brd[0][4] = "--"
                iin.log.append(["bR", [0, 0], "--", [0, 3]])
                iin.log.append(["bK", [0, 4], "--", [0, 2]])

            else:
                iin.brd[0][7] = "--"
                iin.brd[0][6] = "bK"
                iin.brd[0][5] = "bR"
                iin.brd[0][4] = "--"
                iin.log.append(["bR", [0, 7], "--", [0, 5]])
                iin.log.append(["bK",[0,4],"--",[0,6]])
            for i in special_moves:
                iin.prpmt[i[0]][i[1]] = "--"
            for i in legal_moves:
                iin.prpmt[i[0]][i[1]] = "--"
            special_moves = []
            if turn == team["wR"]:
                turn = team["bR"]
            else:
                turn = team["wR"]
        elif[row,col] in legal_moves:
            rec.extend([iin.brd[row][col], [row, col]])
            iin.log.append(rec)
            iin.brd[row][col]=raider
            iin.brd[pos[0]][pos[1]]="--"
            if (raider == "wP" and row == 0) or (raider == "bP" and row == 7):
                Queening(screen,row,col,raider)
            if raider == "wK":
                wk.append([row, col])
                w_k_c=False
            if raider== "bK":
                bk.append([row, col])
                b_k_c=False
            if raider == "wR":
                if pos[0]==7 and pos[1]==7:
                    w_r_rock =False
                else:
                    w_l_rock=False
            if raider == "bR":
                if pos[0]==0 and pos[1]==7:
                    b_r_rock =False
                else:
                    b_l_rock=False
            for i in legal_moves:
                iin.prpmt[i[0]][i[1]] = "--"
            iin.prpmt[pos[0]][pos[1]] = "--"
            if turn == team["wR"]:
                turn = team["bR"]
            else:
                turn = team["wR"]
        else:
            for i in legal_moves:
                iin.prpmt[i[0]][i[1]] = "--"
            iin.prpmt[pos[0]][pos[1]]="--"




def undo():
    global turn
    try:
        step = iin.log.pop()
        if step[0]=="wK" or step[0]=="bK":
            if abs(step[1][1]-step[3][1])>1:
                undo()
                if turn == team["wR"]:
                    turn = team["bR"]
                else:
                    turn = team["wR"]
        iin.brd[step[1][0]][step[1][1]] = step[0]
        iin.brd[step[3][0]][step[3][1]] = step[2]
        if turn == team["wR"]:
            turn = team["bR"]
        else:
            turn = team["wR"]
    except IndexError:
        print("YOU HAVE REACHED THE END")


def tracking_moves(screen):
    global blacks,whites,turn,c_w_check,c_b_check,kblack_in_check,kwhite_in_check,white_all_moves,black_all_moves
    blacks=[]
    whites=[]
    check_count=0
    bach_ga=0
    white_all_moves=[]
    black_all_moves=[]
    for r in range(Dimensions):
        for c in range(Dimensions):
            if iin.brd[r][c]=="--" or iin.brd[r][c]=="wK" or iin.brd[r][c]=="bK":
                continue
            else:
                if team[iin.brd[r][c]]=="team1":
                    q=Chaal.andaza(gather[iin.brd[r][c]][0], r, c, gather[iin.brd[r][c]][1],iin,0,[])
                    black_all_moves.extend(q)

                else:
                    q = Chaal.andaza(gather[iin.brd[r][c]][0], r, c, gather[iin.brd[r][c]][1],iin,0,[])
                    white_all_moves.extend(q)
    for r in range(Dimensions):
        for c in range(Dimensions):
            if iin.brd[r][c]=="--":
                continue
            else:
                if team[iin.brd[r][c]]=="team1":
                    q=Chaal.andaza(gather[iin.brd[r][c]][0], r, c, gather[iin.brd[r][c]][1],iin,1,[wk[-1][0],wk[-1][1]])
                    if q != None:
                        blacks.extend(q)
                else:
                    q = Chaal.andaza(gather[iin.brd[r][c]][0], r, c, gather[iin.brd[r][c]][1],iin,1,[bk[-1][0],bk[-1][1]])
                    if q != None:
                        whites.extend(q)
    if bk[-1] in whites:
        kblack_in_check = True
        check_count+=1
        Checkmate(0,1,check_count)
        c_w_check = False
    elif wk[-1] in blacks:
        kwhite_in_check=True
        check_count+=1
        Checkmate(1, 0, check_count)
        c_b_check = False
    else:
        kwhite_in_check=kblack_in_check=False
    print("End of Session")

def main():
    global clk
    p.init()
    screen = p.display.set_mode([1500, 800])
    screen.fill(p.Color("white"))
    loading_images()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running=False
            elif e.type == p.MOUSEBUTTONDOWN:
                clk+=1
                location = p.mouse.get_pos()
                col = int((location[0] // (sq_size)) - 2)
                row = int((location[1] // (sq_size)) - 2)
                if 0<=row<=7 and 0<=col<=7:
                    potta=iin.brd[row][col]
                    event_manger(potta,row,col,screen)
                    tracking_moves(screen)
            elif e.type == p.KEYDOWN :
                undo()
                clk=0
        drawing_board(screen)
        drawing_pieces(screen,iin.brd)
        p.display.flip()


if __name__ == "__main__":
    main()
