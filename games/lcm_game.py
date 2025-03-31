import random
import math


def lcm(a, b):
    """НОК"""
    return abs(a * b) // math.gcd(a, b)


def lcm_game_logic():
    """Логика генерации вопроса и правильного ответа"""
    nums = [random.randint(1, 100) for _ in range(3)]
    correct_answer = nums[0]
    for num in nums[1:]:
        correct_answer = lcm(correct_answer, num)

    return ' '.join(map(str, nums)), correct_answer
