import random

def strategy(history):
    if not history:
        return random.choice(['R','P','S'])
    else:
        opp = [game[1] for game in history]
        #print(len(opp))
        if len(opp) <=18:
            nR, nP, nS = opp.count('R'),  opp.count('P'), opp.count('S')
            fR, fP, fS = nR/len(opp), nP/len(opp), nS/len(opp)
            return random.choices(['R', 'P', 'S'], weights=[fS, fR, fP])[0]
        else:
            #Markov Chain
            #Initialize 3 empty lists
            opp_R = []  # #Plays after a Rock was played
            opp_P = []  # #Plays after a Paper was played
            opp_S = []  # #Plays after a Scissors was played

            for i in range(len(opp)-2):
                if opp[i] == 'R':
                    opp_R.append(opp[i+1])  # #i is R, the next play is i+1
                    nRR, nRP, nRS = opp_R.count('R'), opp_R.count('P'), opp_R.count('S')
                    fRR, fRP, fRS = nRR / len(opp_R), nRP / len(opp_R), nRS / len(opp_R)  # # Prob to jump to other plays
                elif opp[i] == 'P':
                    opp_P.append(opp[i+1])  # #i is P, the next play is i+1
                    nPR, nPP, nPS = opp_P.count('R'), opp_P.count('P'), opp_P.count('S')
                    fPR, fPP, fPS = nPR / len(opp_P), nPP / len(opp_P), nPS / len(opp_P)  # # Prob to jump to other plays
                else:
                    opp_S.append(opp[i+1])  # #i is S, the next play is i+1
                    nSR, nSP, nSS = opp_S.count('R'), opp_S.count('P'), opp_S.count('S')
                    fSR, fSP, fSS = nSR / len(opp_S), nSP / len(opp_S), nSS / len(opp_S)  # # Prob to jump to other plays

            if opp[-1] == 'R':
                a = random.choices(['R', 'P', 'S'], weights=[fRS, fRR, fRP])[0]
                #print('a',a, opp[-1],fRR,fRP,fRS)
                return a
            elif opp[-1] == 'S':
                b = random.choices(['R', 'P', 'S'], weights=[fSS, fSR, fSP])[0]
                #print('b',b,opp[-1],fSR,fSP,fSS)
                return b
            else:
                c = random.choices(['R', 'P', 'S'], weights=[fPS, fPR, fPP])[0]
                #print('c',c, opp[-1],fPR,fPP,fPS)
                return c
