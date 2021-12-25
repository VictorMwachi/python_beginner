import random

def play():
    computer=random.choice(['R','P','S'])
    print(computer)
    user=input('Lets play rock (R) paper(P) and scissors(S).. input your outcome: ').upper()
   
    

    if user==computer: 
        print( 'It is a tie')

    elif is_win(user,computer):
        print( 'You won')
    
    else:
        print( 'you lost')
        
    
def is_win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='s'and opponent=='p')or(player=='p'and opponent=='r'):
        return True


play()

