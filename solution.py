import pandas as pd
import numpy as np

chat_id = 1182463770 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    semianswer = 0
    for i in range(len(x)):
      semianswer += x[i]
    semianswer /= len(x)
    answer = semianswer/36
    return answer # Ваш ответ
