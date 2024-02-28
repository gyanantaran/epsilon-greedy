# bandit.py
# author: vishalpaudel

from multiarm_bandit.arm import Arm, pull
from utils.display_utils import display_info

from typing import List


# basically a List of parametrized distributions List[Arm]
class Bandit:
    def __init__(
        self, 
        prob_dists_params: List, 
        prob_dists: List 
    ):
        assert len(prob_dists) == len(prob_dists_params)  # has to be equal number of parameter sets and distributions
        self.arms = [ Arm( prob_dists_params[i], prob_dists[i] ) for i in range( len(prob_dists) ) ]


def run(bandit, N_tries):
    history: List[Tuple] = []  # empty total history
    

    arms_history = {arm: [] for arm in bandit.arms}  # empty history
    
    while( N_tries > 0 ):
        N_tries -= 1
        
        arm_choice_index	= int(input("Enter an integer choice: "))
        arm_choice  		= bandit.arms[ arm_choice_index ]			# expects index of the arm from the User
        pull_result      	= pull( arm_choice )						# rewards/returns/result

        history.append( (arm_choice, pull_result) )  # updating total history

        arms_history[ arm_choice ].append( pull_result ) # updating coin history

        display_info(remaining_tries=N_tries, arms_history=arms_history)  # !passing the WHOLE history in
        

    return history
