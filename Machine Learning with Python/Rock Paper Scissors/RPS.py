# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[],player_history=[],counter=[0], quincyswitch=[False],
           play_order=[{
               "RR": 0,
               "RP": 0,
               "RS": 1,
               "PR": 0,
               "PP": 0,
               "PS": 0,
               "SR": 0,
               "SP": 0,
               "SS": 0,
           }]):
    
    opponent_history.append(prev_play)
    if not prev_play:
        player_history.append(prev_play)
        counter[0] = 0
        quincyswitch[0] = False
        
    abbey_prevchoice = "P"
        
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    thisswitch = False
    
    
    # abbey choice
    if len(list(filter(lambda x: not x, player_history[-3:]))) == 0:    
        thisswitch = True
        last_twoPrevious = "".join(player_history[-3:-1])
        play_orderPrevious=play_order[0].copy()
        play_orderPrevious[last_twoPrevious] -= 1
        potential_plays = [
            player_history[-2] + "R",
            player_history[-2] + "P",
            player_history[-2] + "S",
            ]
        sub_order = {
            k: play_orderPrevious[k]
            for k in potential_plays if k in play_orderPrevious
            }

        abbey_prevchoice1 = ideal_response[max(sub_order, key=sub_order.get)[-1]]
        abbey_prevchoice2 = ideal_response[max(sub_order, key=sub_order.get)[0]]
        

   
    last_two = "".join(player_history[-2:])
    if len(last_two) == 2:
       play_order[0][last_two] += 1


    quincy_choices = ["R", "R", "P", "P", "S"]

    if opponent_history[-5:] == quincy_choices: # strategy for Quincy
       quincyswitch[0] = True
        
    if quincyswitch[0]:
        guess = quincy_choices[counter[0] % len(quincy_choices)]
        counter[0] +=1      

    else:
        guess = "P"
        if thisswitch:
        
            last_ten = player_history[-11:-1]
            most_frequent =  max(set(last_ten), key=last_ten.count)
            
            if most_frequent == '':
                most_frequent = "S"
                guess = ideal_response[most_frequent]

            elif prev_play == ideal_response[most_frequent]: #mrugesh strategy
                last_ten = player_history[-10:]
                most_frequent =  max(set(last_ten), key=last_ten.count)
        
                guess = ideal_response[most_frequent] 
            
            if ''.join(opponent_history[-2:])== abbey_prevchoice1 + abbey_prevchoice2: #abbey strategy
             
                potential_plays = [
                    player_history[-1] + "R",
                    player_history[-1] + "P",
                    player_history[-1] + "S",
                    ]
                sub_order = {
                    k: play_order[0][k]
                    for k in potential_plays if k in play_order[0]
                    }

                guess = ideal_response[max(sub_order, key=sub_order.get)[-1:]]
             
            elif player_history[-2]: # kris strategy
                if prev_play == ideal_response[player_history[-2]]:  # strategy for kris
             # kris spielt immer das was in der letzten runde gespielt wurde,
                 guess =  ideal_response[player_history[-1]]                
                    
    player_history.append(ideal_response[guess])
    return ideal_response[guess]