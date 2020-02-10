import os 
import itertools
import importlib
import random

def write_file(counter, mode):
    #Writes a .txt with the value of counter to the directory
    f = open('counter.txt',mode)
    f.write(str(counter))
    f.close()

def find_opponents(matches):
    #Returns a list of the IDs of each opponent in the order that this agent will play them
    opponents = []
    for p1, p2, in matches:
        if 'mn629' in p1.name:
            opponents.append(p2.name)
        if 'mn629' in p2.name:
            opponents.append(p1.name)
    return opponents

def find_strategy(__main__, opponent_name, opponent_history):
    #Runs opponent_name's strategy function with opponent_history as the argument, and returns the counter to that functions
    #output, unless their strategy function is determined to be running a proportional strategy, in which case it will return
    #the counter the last item in opponent_history (i.e. the counter to the last option the opponnent played)
    if opponent_name[-2] ==  '-':
        opponent_name = opponent_name[0:len(opponent_name)-2]
    beat = {'R':'P','P':'S','S':'R'}          
    f = open(f'{__main__.players_path.stem}/{opponent_name}.py')
    lines = f.readlines()
    f.close()
    c = ''.join(lines)
    if opponent_history and' mn629' not in opponent_name:
        if "return random.choices(['R', 'P', 'S']" in c:
            return beat[opponent_history[-1][0]]
        else:
            opponent = importlib.import_module(f'{__main__.players_path.stem}.{opponent_name}')
            return beat[opponent.strategy(opponent_history)]
    else:
        return 'R'
    
def strategy(history):
    #main
    try:
        import __main__
        
        matches = itertools.combinations(__main__.players, 2)
        opponents = find_opponents(matches)
        
        f = open('counter.txt','r')
        counter = int(f.read())
        f.close()
        if not history: 
            counter += 1
            write_file(counter, 'w')
        if counter == len(opponents) - 1 and __main__.rounds - 1 == len(history):
            os.remove('counter.txt')
        
        opponent_history = []
        for play in history:
            opponent_history.append(play[::-1])
        opponent_name = opponents[counter]
        
        return find_strategy(__main__, opponent_name, opponent_history)
    except Exception:
        return random.choice(['R','P','S'])
    
write_file(-1, 'w+') #Only runs when main imports this file; initiates counter.txt at -1