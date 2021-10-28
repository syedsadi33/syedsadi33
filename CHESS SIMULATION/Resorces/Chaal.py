kamal = {"wP": [0, 0, 1, 0, 1, 0, 0, 1, True], "bR": [1, 1, 1, 1, 0, 0, 0, 0, False],
         "bB": [0, 0, 0, 0, 1, 1, 1, 1, False], "bN": [0, 0, 0, 0, 0, 0, 0, 0, False],
         "bQ": [1, 1, 1, 1, 1, 1, 1, 1, False], "bK": [1, 1, 1, 1, 1, 1, 1, 1, True],
         "bP": [0, 0, 0, 1, 0, 1, 1, 0, True],  "wR": [1, 1, 1, 1, 0, 0, 0, 0, False],
         "wB": [0, 0, 0, 0, 1, 1, 1, 1, False], "wN": [0, 0, 0, 0, 0, 0, 0, 0, False],
         "wQ": [1, 1, 1, 1, 1, 1, 1, 1, False],  "wK": [1, 1, 1, 1, 1, 1, 1, 1, True]}
gather={"wP": [False,"wP"], "bR": [ False,"bR"],
         "bB": [False,"bB"], "bN": [True,"bN"],
         "bQ": [False,"bQ"], "bK": [True,"bK"],
         "bP": [False,"bP"],  "wR": [False,"wR"],
         "wB": [False,"wB"], "wN": [True,"wN"],
         "wQ": [False,"wQ"],  "wK": [False,"wK"]}
team={"--":"joker","bR":"team1","bN":"team1","bB":"team1","bQ":"team1","bK":"team1","bP":"team1","wR":"team2","wN":"team2","wB":"team2","wK":"team2","wQ":"team2","wP":"team2"}
def andaza(Ghoda, kidarx, kidary, kon,In,insp,kingpos)->list:
    r = []
    if not Ghoda:
        if kamal[kon][0] == 1:
            for i in range(1, kidary + 1):  # 1
                if In.brd[kidarx][kidary-i]=="--":r.append([kidarx, kidary - i])
                elif team[In.brd[kidarx][kidary-i]]==team[kon]:break
                else:
                    r.append([kidarx,kidary-i])
                    break
                if kamal[kon][8] == True: break

            if insp==1:
                if kingpos in r:return r
                else:r=[]


        if kamal[kon][1] == 1:
            for i in range(kidary + 1, 8):  # 2
                if In.brd[kidarx][i]=="--":r.append([kidarx, i])
                elif team[In.brd[kidarx][i]]==team[kon]:break
                else:
                    r.append([kidarx,i])
                    break
                if kamal[kon][8] == True: break

            if insp == 1:
                if kingpos in r:return r
                else:r = []

        if kamal[kon][2] == 1:
            for i in range(1, kidarx + 1):  # 3
                if kon =="wP":
                    if In.brd[kidarx - i][kidary] == "--" and In.brd[kidarx-i-1][kidary] == "--" and kidarx == 6:
                        r.append([kidarx-i-1,kidary])
                    if In.brd[kidarx-i][kidary] == "--":
                        r.append([kidarx-i,kidary])
                    break
                if In.brd[kidarx-i][kidary]=="--":r.append([kidarx - i, kidary])
                elif team[In.brd[kidarx-i][kidary]]==team[kon]:break
                else:
                    r.append([kidarx-i,kidary])
                    break
                if kamal[kon][8] == True: break

            if insp==1:
                if kingpos in r:return r
                else:r=[]

        if kamal[kon][3] == 1:
            for i in range(kidarx + 1, 8):  # 4
                if kon =="bP":
                    if In.brd[i][kidary] == "--" and In.brd[i+1][kidary] == "--" and kidarx == 1:
                        r.append([i+1,kidary])
                    if In.brd[i][kidary] == "--":
                        r.append([i,kidary])
                    break
                if In.brd[i][kidary]=="--":r.append([i, kidary])
                elif team[In.brd[i][kidary]]==team[kon]:break
                else:
                    r.append([i,kidary])
                    break
                if kamal[kon][8] == True: break

            if insp==1:
                if kingpos in r:return r
                else:r=[]

        if kamal[kon][4] == 1:
            for i in range(1, 8):  # 5
                if kidarx - i < 0 or kidary + i == 8:break
                if kon=="wP":
                    if team[In.brd[kidarx - i][kidary + i]] == "team1":
                        r.append([kidarx - i,kidary + i])
                    break
                elif In.brd[kidarx-i][kidary+i]=="--":
                    r.append([kidarx - i, kidary + i])
                elif team[In.brd[kidarx-i][kidary+i]]==team[kon]:
                    break
                else:
                    r.append([kidarx-i,kidary+i])
                    break
                if kamal[kon][8] == True:
                    break

            if insp==1:
                if kingpos in r:return r
                else:r=[]

        if kamal[kon][5] == 1:
            for i in range(1, 8):  # 6
                if kidarx + i == 8 or kidary + i == 8:break
                if kon=="bP":
                    if team[In.brd[kidarx + i][kidary + i]] == "team2":
                      r.append([kidarx + i,kidary + i])
                    break
                elif In.brd[kidarx+i][kidary+i]=="--":r.append([kidarx + i, kidary + i])
                elif team[In.brd[kidarx+i][kidary+i]]==team[kon]:break
                else:
                    r.append([kidarx+i,kidary+i])
                    break
                if kamal[kon][8] == True: break

            if insp==1:
                if kingpos in r:return r
                else:r=[]


        if kamal[kon][6] == 1:
            for i in range(1, 8):  # 7
                if kidarx + i == 8 or kidary - i < 0:break
                if kon=="bP":
                    if team[In.brd[kidarx + i][kidary - i]] == "team2":
                      r.append([kidarx + i,kidary - i])
                    break
                elif In.brd[kidarx+i][kidary-i]=="--":r.append([kidarx + i, kidary - i])
                elif team[In.brd[kidarx+i][kidary-i]]==team[kon]:break
                else:
                    r.append([kidarx+i,kidary-i])
                    break
                if kamal[kon][8] == True: break

            if insp==1:
                if kingpos in r:return r
                else:r=[]

        if kamal[kon][7] == 1:
            for i in range(1, 8):  # 8
                if kidarx - i < 0 or kidary - i < 0:
                    break
                if kon=="wP":
                    if team[In.brd[kidarx - i][kidary - i]] == "team1":
                      r.append([kidarx - i,kidary - i])
                    break
                elif In.brd[kidarx-i][kidary-i]=="--":
                    r.append([kidarx - i, kidary - i])
                elif team[In.brd[kidarx-i][kidary-i]]==team[kon]:
                    break
                else:
                    r.append([kidarx-i,kidary-i])
                    break
                if kamal[kon][8] == True: break

            if insp==1:
                if kingpos in r:return r
                else:r=[]


    else:
        h1 = [2, -2]
        h2 = [1, -1]
        for i in h1:
            for j in h2:
                a = kidarx + i
                b = kidary + j
                if (not 0 <= a <= 7) or (not 0 <= b <= 7):
                    pass
                else:
                    if In.brd[a][b] == "--":pass
                    elif team[In.brd[a][b]] == team[kon]:
                       continue
                    r.append([a,b])
        for i in h2:
            for j in h1:
                a = kidarx + i
                b = kidary + j
                if (not 0 <= a <= 7) or (not 0 <= b <= 7):
                    pass
                else:
                    if In.brd[a][b]=="--":pass
                    elif team[In.brd[a][b]] == team[kon]:
                        continue
                    r.append([a,b])
        if insp == 1:
            if kingpos in r:
                return [kidarx,kidary]
    return r


