import os
import operator
import random
import string
from unicodedata import normalize as norm

def lerNome():
    return input("Informe o nome: ")

def removerAcentos(txt):
    return norm('NFKD', txt).encode("ASCII" , "ignore").decode("ASCII")

def gerarPassword():
    pwd = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(8)]
    return "".join(pwd)

def gerarUserName(data, nome):
    usr = nome[0].lower() + nome.split(' ').pop().lower()
    usr = removerAcentos(usr)

    i = 1
    usr_temp = usr
    while(data.get(usr) != None):
        usr = usr_temp + str(i).zfill(2)
        i = i + 1

    data[usr] = [nome, gerarPassword()]

def exibirDados(data):
    cols = os.get_terminal_size().columns
    os.system('clear')
    print("="*cols)
    print("%-40s %-20s %-20s" %("Nome", "UserName", "Senha"))
    print("="*cols)

    for item in data:
        print("%-40s %-20s %-20s" %(item[1][0], item[0], item[1][1]))
    print("="*cols)

def main():
    data = {}
    os.system('clear')
    resp = ""

    while resp != "N":
        gerarUserName(data, lerNome())
        resp = input("Deseja continuar? [S] ou [N]: ").upper()

    data = sorted(data.items(), key=operator.itemgetter(0))

    exibirDados(data)

main()