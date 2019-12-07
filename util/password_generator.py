from random import randint


def get_good_password():
    with open('good-passwords.txt', 'r') as f:
        temp = f.read()
        good_passwords = [line for line in temp.split("\n")]

    # print(good_passwords[len(good_passwords)-1])
    return good_passwords[randint(0, len(good_passwords)-1)]


def get_bad_password():
    with open('bad-passwords.txt', 'r') as f:
        temp = f.read()
        bad_passwords = [line for line in temp.split("\n")]

    # print(bad_passwords)
    return bad_passwords[randint(0, len(bad_passwords)-1)]
