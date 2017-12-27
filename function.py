def func1():
    print("Hello, this is my very first function\n")

def bitcoin_to_inr(btc):
    amount = btc*927000
    print(amount)

func1()
bitcoin_to_inr(13.8)
bitcoin_to_inr(1.2)

def allowed_dating_age(my_age):
    girls_age=my_age/2 +7
    return girls_age

print("You can date girls of age",allowed_dating_age(29),"or elder")

def soc_net(gender="unknown"):
    if gender is "m":
        gender="Male"
    elif gender is "f":
        gender="Female"
    print(gender)

soc_net("m")
soc_net("f")
soc_net()

def func2(name="Anjan",Occupation="Student",Hobby="Guitar"):
    print(name,Occupation,Hobby)

func2()
func2("Amrit","Student","None")
func2(Hobby="Flute",name="Lenny",Occupation="Student")

def coolfunc(*args):               #Can have any number of arguments
    total=0
    for a in args:
        total += a
    print(total)

coolfunc(2,3,4,4,5,6)
coolfunc(2,34,4)

def health(age,apples,ciggy):
    res = (110-age)+(apples*3.5)-(ciggy*2)
    print(res)

Anjan_stats = [27,30,0]

health(Anjan_stats[0],Anjan_stats[1],Anjan_stats[2])
health(*Anjan_stats)

