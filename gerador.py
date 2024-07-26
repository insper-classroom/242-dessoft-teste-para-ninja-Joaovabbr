import random
from pygame import time
import config
from sprites import Quadrado

def gera_numeros():
    """
    Gera os números aleatórios 
    """
    n1 = random.randint(1, 15)
    n2 = random.randint(1,15)
    result = n1+n2
    n3 = random.randint(1,15)

    return [n1,n2,n3,result]
        
def gera_quadrados(cores,nums, grupo):
    ultimo = nums[-1]
    del nums[-1]
    random.shuffle(nums)
    nums.append(ultimo)
    for n in nums:
        index = nums.index(n)
        if index <= 2:
            cor = cores[index]
            quadrado = Quadrado(cor, config.COMPRIMENTO_TELA/2 + 20, 450 - ((config.QUADRADO_LADO) *index), n, nums.copy())
            grupo.add(quadrado)
        