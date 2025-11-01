import random

def gen_pass(pass_length):
    # Символы, из которых будет составляться пароль
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    # Переменная для хранения пароля
    password = ""
    
    # Цикл для генерации пароля нужной длины
    for i in range(pass_length):
        password += random.choice(elements)
    
    # Возвращаем готовый пароль
    return password

def ran_em():
    emojis = ["😶", "😂", "💔" ,"💀" ,"🥭" ,"😺" ,"🎩" ,"😶‍🌫️" ,"🥸" ,"🤠" ,"👿" ,"👽" ,"👹" ,"🐵" ,"👀"]
    result = ""

    for i in range(1):
        result += random.choice(emojis)

    return result

def cflip():
    sides = ["Орёл", "Решка"]
    side = ""

    for i in range(1):
        side += random.choice(sides)

    return side