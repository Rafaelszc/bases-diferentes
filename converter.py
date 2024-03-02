from random import randint

while True:
    numdec = randint(0, 200)
    numbin = bin(numdec)[2:]
    numhex = hex(numdec)[2:]
    numoct = oct(numdec)[2:]
    def convecao(tipo1, tipo2, num1, num2):   
        while True:
            converter = input(f'converta o {tipo1} {num1} para {tipo2}\n')
            if converter ==  num2:
                print('Acertou\n')
                break
            else:
                print('Errou\n')
                continue

    convecao('decimal', 'binario', numdec, numbin)
    convecao('binario', 'hexadecimal', numbin, numhex)
    convecao('decimal', 'octal', numdec, numoct)
    convecao('hexadecimal', 'decimal', numhex, str(numdec))
    convecao('octal', 'binario', numoct, numbin)
    convecao('binario', 'decimal', numbin, str(numdec))
    convecao('hexadecimal', 'binario', numhex, numbin)