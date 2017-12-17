import sys, time

def generate_password(length):
    alphabet = list('0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
    psw = []

    for i in range(length):
        r = ''.join(str(int(str(time.time() % 1)[9:11]) % 2) for x in range(6))
        r_int = int(r,2)
        psw.append(alphabet[r_int % len(alphabet)])

    passw = ''.join(psw)

    return passw


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('please, enter params')
        sys.exit()

    if sys.argv[1] == '--help':
        print('''Input params:
        length of password''')
        sys.exit()

    try:
        length = int(sys.argv[1])
        if length <= 0:
            raise ValueError
    except(ValueError):
        print('bad password length format')
        sys.exit()

    print(generate_password(length))