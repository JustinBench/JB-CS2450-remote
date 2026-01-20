import random

def intro():
    print("Hello! I'm going to guess your age, and if I'm wrong, I'll give you a million dollars!")
    return

def getName():
    name = input("What's your name? ")
    return name

def guess():
    return random.randint(15, 31)

def getAnswer(age):
    answer = input("Are you " + str(age) + " years old? (y/n) ")
    return answer

def conclusion(name, age, answer):
    if answer == 'y':
        print(name + ' is ' + str(age) + ' years old.')
    else:
        print("Rats. Well, I'm broke, so you don't get a million dollars.")
    return

def main():
    intro()
    name = getName()
    age = guess()
    answer = getAnswer(age)
    conclusion(name, age, answer)

if __name__ == '__main__':
    main()

