# coin.py
# author: vishalpaudel

from enum import Enum
from collections import Counter

class Coin:
    def __init__(self, p):
        self.p = p

    def __repr__(self):
        return f'Coin(p={self.p})'

    def sample(self):
        return toss(self)

class CoinToss(Enum):
    head = 1
    tail = 2
    
    def __repr__(self):
        if self == CoinToss.head: return 'head'
        elif self == CoinToss.tail: return 'tail'
        else: return "Unknown coin-toss"


import random

# fn toss: tosses a `Coin`, returns a `CoinToss`
def toss(coin: Coin) -> CoinToss:
    p_hat = random.uniform(0, 1)

    if  ( coin.p >= p_hat ): return CoinToss.head
    elif( coin.p <  p_hat ): return CoinToss.tail
    else                   : sys.exit(-1)