# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random;
def player(prev_play, opponent_history=[],my_plays=[]):
    opponent_history.append(prev_play)
    key={'R':'P','S':'R','P':'S'};
    '''
    if opponent_history[-3:]==['R','P','S'] and my_plays[-3:]==['S','R','P']:
        guess=prev_play;
        return guess;
    if len(opponent_history)<=1:
        guess='S';
    elif len(opponent_history)>2000 and len(opponent_history)<3000:
        guess='R';
        
        if len(opponent_history)>2010:
            guess=key[prev_play];
            if len(opponent_history)>2011:
                guess=prev_play;
    elif len(opponent_history)>3000 or len(opponent_history)<1300:
        if len(opponent_history)>3 and prev_play==opponent_history[-1] and prev_play==opponent_history[-2]:
            match prev_play:
                case 'R':
                    guess='P';
                case 'P':
                    guess='S';
                case 'S':
                    guess='R';
        else:
            if (len(opponent_history)//2)%3==0:
                guess='P';
                if prev_play=='P':
                    guess='S';
            elif (len(opponent_history)//2)%3==1:
                guess='R';
                if prev_play=='R':
                    guess='P'
            else:
                guess='S';

                if prev_play=='S':
                    guess='R';
    '''
    #else:
    opponent_history1=opponent_history;
    guess='R';
    a=400;
    n=3;
    if len(opponent_history)>a:
        opponent_history1=opponent_history1[1000+a:];
        n=4;
    if len(opponent_history)>2*a:
        opponent_history1=opponent_history1[1000+2*a:];
    ## Creating a list of all the different combinations of last i plays. Then going to edit i. 
    
    combos={};
    combos["".join(opponent_history1[-n:])]=0;
    for i in range(1,len(opponent_history1)-n+1):
        combo="".join(opponent_history1[-n-i:-i]);
    ### If that combination is already in the list, add on to it
        if combo in combos:
            combos[combo]+=1;
        else:
            combos[combo]=0;

    current_combo="".join(opponent_history1[-n+1:]);
    possible_combos=[current_combo+"R",current_combo+"P",current_combo+'S'];
    prev_played={key: value for key, value in combos.items() if key in possible_combos};
    ## Now get all the combos from the dictionary that start with the same n-1 characters as the current setup
    if prev_played:
        guess=max(prev_played,key=prev_played.get)[-1];
        guess=key[guess];
    elif prev_play:
        guess=key[prev_play];

    my_plays.append(guess);
    return guess;
