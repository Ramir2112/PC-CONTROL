print("Start install PC Control")
import random
from time import sleep
from rich.progress import track

token = input("Send you token: ")
print()
print("Начинается установка. Не закрывайте приложение!")
file = open('token.txt', 'w', encoding='utf-8')
file.write(token)
print()
def do_step(step):
    sleep(random.uniform(0.01, 0.1))

for step in track(range(50), description="Изменение значения Token"):
    do_step(step)
