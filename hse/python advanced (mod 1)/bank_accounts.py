import sys
from math import floor

bank = {}
def deposit(name: str, value: str):
    value = int(value)
    if bank.get(name, 0):
        bank[name] += value
    else:
        bank[name] = value

def withdraw(name: str, value: str):
    value = int(value)
    account = bank.setdefault(name, 0)
    bank[name] = account - value

def balance(name: str):
    print(bank.get(name, 'ERROR'))

def transfer(name1: str, name2: str, value):
    value = int(value)
    bank.setdefault(name1, 0)
    bank.setdefault(name2, 0)
    bank[name1] -= value
    bank[name2] += value

def income(percent: int):
    for name in bank:
        if bank[name] > 0:
            bank[name] += floor(bank[name] / 100 * int(percent))

COMMANDS = {'DEPOSIT': deposit,
            'WITHDRAW': withdraw,
            'BALANCE': balance,
            'TRANSFER': transfer,
            'INCOME': income}

def call_a_commands(command, info):
    COMMANDS[command](*info)

for command in sys.stdin:
    if command == '\n':
        break
    command = command.rstrip('\n').split()
    call_a_commands(command[0], command[1:])

# 92fcf649f2f897b8c307ebe7d57b2704