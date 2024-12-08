
def watch_hello_common():
    print("disk of common{")
    file = open("hello common.txt", "r")
    common = file.readlines()
    for i in common:
        print(i)
    file.close()
    print("}")

def watch_hello_vip():
    print("disk of common{")
    file = open("hello vip.txt", "r")
    vip = file.readlines()
    for i in vip:
        print(i)
    file.close()
    print("}")

def rewrite_to_hello_vip(word=str(input())):
    file=open("hello vip.txt","w")
    file.write(word)
    file.close()
    print("successfully")

def rewrite_to_hello_common(word=str(input())):
    file=open("hello vip.txt","w")
    file.write(word)
    file.close()
    print("successfully")

rewrite_to_hello_vip()
rewrite_to_hello_common()
watch_hello_vip()
watch_hello_common()

name=str(input())

vip={
"Панов Алексей Денисович",
"Федорова Александра Егоровна",
"Белова Валерия Викторовна",
"Дмитриева Алиса Серафимовна",
}

common={
"Фролов Даниил Макарович",
"Лебедев Алексей Львович",
"Громов Александр Эмильевич",
"Воронцов Матвей Миронович",
}

for i in vip:
    if i == name:
        print(name)
        with open("hello vip.txt","r") as vip_persons:
            file = vip_persons.readlines()
            for i in vip_persons:
                print(i)
for i in common:
    if i == name:
        print(name)
        with open("hello common.txt","r") as common_persons:
            file= common_persons.readlines()
            for i in common_persons:
                print(i)



