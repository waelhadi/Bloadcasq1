from termcolor import colored
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(colored("[1]  سحب بروكسي قوي", "cyan"))
print(colored("[2]  سحب بروكسي ضعيف", "cyan"))
print(colored("[3]  أبدء البلاغ", "cyan"))

Get_aobsh = input(colored("[×] اختار : ", "cyan"))
