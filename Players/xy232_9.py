#        if  "import random" in c:
#            for i in range(len(lines)-1):
#                if not lines[i]:
#                    n = i
#                    break
#            if "random.seed(1000)" not in c:
#                for i in range(len(lines)-1):
#                    if "def strategy(" in lines[i]:
#                        pos_func = i
#                with open(f'{__main__.players_path.stem}/{opponent_name}.py', "w") as f:
#                    first = lines[pos_func+1]
#                    for i in range(len(first)-1):
#                        if first[i] not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
#                            pass
#                        else:
#                            space = first[0:i]
#                            break
#                    lines.insert(pos_func+1, '\n')
#                    lines.insert(pos_func+1, space+"random.seed(1000)")
#                    f.write("".join(lines))
#                    f.close()