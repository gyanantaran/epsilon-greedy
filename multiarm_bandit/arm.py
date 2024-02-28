# arm.py
# author: vishalpaudel

from models.coin import Coin

import sys
from typing import List

# basically a parametrized distribution
class Arm:
    def __init__(
        self, 
        prob_dist_param,
        prob_dist
    ):
        self.prob_dist_param = prob_dist_param
        self.prob_dist = prob_dist

        self.model = prob_dist( prob_dist_param )

    def __repr__(self):
        return self.model.__repr__()

def pull( arm ):
    return ( arm.model ).sample()            # samples the arm once
