# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[],counter=[0],player_history=[],isquincy=[False]):
    
    opponent_history.append(prev_play)
    if not prev_play:
        player_history.append(prev_play)
                          
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    if opponent_history[-5:] == ["R","R","P","P","S"]: # strategy for Quincy (100% win)
        isquincy[0] = [True]
        
    if isquincy[0]:
        
        choices = ["R", "R", "P", "P", "S"]
        guess = choices[counter[0] % len(choices)]
        counter[0] += 1
    else:
        last_ten = player_history[-10:]
        most_frequent =  max(set(last_ten), key=last_ten.count)
        
        if most_frequent == '':
            most_frequent = "S"
            guess = ideal_response[most_frequent]

        elif prev_play == ideal_response[most_frequent]: #mrugesh strategy
            guess = ideal_response[most_frequent]
       
        elif len(player_history)>1:
            
            if player_history[-1]:
                if prev_play == ideal_response[player_history[-1]]:  # strategy for kris
                # kris spielt immer das was in der letzten runde gespielt wurde,
                    guess =  player_history[-1]
                else:
                    guess = "R"
            else:
                guess="R"
                    
        else:
            guess = "R"
        
    player_history.append(ideal_response[guess])
    #print('player',ideal_response[guess])
    return ideal_response[guess]



