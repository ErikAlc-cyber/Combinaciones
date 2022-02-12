def primo(numero):
    if numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True

for i in range(10):
    if(primo(i)):
        print(str(i)+" es primo")
    else:
        print(str(i)+" no es primo")