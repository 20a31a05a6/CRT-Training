#rock,paper,scissor GAME
from random import random, randint

choice=['rock','paper','scissor']
p_score=0
c_score=0
limit=5
while p_score!=limit and c_score!=limit:
    print(f"choose among the following:",choice)
    my_ch=input("Player choice:").lower()
    if my_ch not in choice:
        print("---Invalid Choice---")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f"System choice : {sys_ch}")
    if my_ch=='rock' and sys_ch=='scissor':
        p_score+=1
    elif my_ch=='scissor' and sys_ch=='paper':
        p_score+=1
    elif my_ch=='paper' and sys_ch=='rock':
        p_score+=1
    elif my_ch== sys_ch:
        print("***** DRAW ******")
    else:
        c_score+=1
    print(f"your score:{p_score} system_score:{c_score}")

if p_score > c_score:
    print("You wins the Game")
else:
    print("System wins the Game")
