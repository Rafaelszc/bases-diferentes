from random import randint

class operacao:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.ordem = [self.n1, self.n2]
    def soma(self):
        ressoma = bin(self.n1+self.n2)[2:]
        while True:
            res1 = str(input(f'digite o resultado da operação {num1bin} + {num2bin} \n'))
            if res1 == ressoma:
                print('acertou!')
                break
            elif res1 == 'exit':
                exit()
            else:
                print('errou')
                continue
    def subtracao(self):
        self.ordem.sort()
        ressubtracao = bin(self.ordem[1]- self.ordem[0])[2:]
        while True:
            res2 = str(input(f'digite o resultado da operação {bin(self.ordem[1])[2:]} - {bin(self.ordem[0])[2:]} \n'))
            if res2 == ressubtracao:
                print('acertou!')
                break
            elif res2 == 'exit':
                exit()
            else:
                print('errou')
                continue
    def multiplicacao(self):
        n1menor = randint(0, 50)
        n2menor = randint(0, 50)
        resmultiplicacao = bin(n1menor*n2menor)[2:]
        while True:
            res3 = str(input(f'digite o resultado da operação {bin(n1menor)[2:]} * {bin(n2menor)[2:]} \n'))
            if res3 == resmultiplicacao:
                print('acertou!')
                break
            elif res3 == 'exit':
                exit()
            else:
                print('errou')
                continue

while True:
    num1 = randint(0, 200)
    num2 = randint(0, 200)
    num1bin = bin(num1)[2:]
    num2bin = bin(num2)[2:]

    operacao(num1, num2).soma()

    operacao(num1, num2).subtracao()

    operacao(num1, num2).multiplicacao()