from calendar import c
from ctypes import pythonapi
from tracemalloc import start


a=5
rez=a/2
print(rez)
rez1=a//2
print(rez1)

#b=input()
#b+5 #nu merge pt ca e de type string, string e imutabil

s="python"
#[start:stop:step]
print(s[0:1:2])

print(s[0:2:])
print(s[:2:])
print(s[::-1]) #afiseaza invers

user=input("Introduceti user: ")
password=input("Introduceti parola: ")
print("Userul este: ", user)
for i in range(len(password)):
    print("*", end="")
    
print()

print("Help me".replace("Help", "Assist"))
print()

#LISTE
my_list=[1,2,3,4]
print(my_list[0:2:3])

my_list.sort #chiar modifica lista, nu returneaza o copie sortata, ci chiar modifica lista originala
print(my_list) 
print()
sorted(my_list) #returneaza o copie sortata, nu modifica lista originala
print("Lista este", my_list)

print()

#TUPLURI
my_tuple=("a", "b", "c") #elementele unui tuple nu pot fi modificate, dar putem face slicing
print("Lungime tuplu:", len(my_tuple))
print()

a, b, c = my_tuple #unpacking
#se foloseste *d pentru a desemna restul elementelor


#SETURI- colectie neordonata de elemente unice, nu accepta duplicate, nu are indexare, nu se poate face slicing
my_set=set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(3) #nu se adauga pentru ca e deja in set
print("Setul este:", my_set)

new_list=[1,2,3,4,5, 5, 2]
print("Lista initiala este:", new_list)
set(new_list) #convertim lista in set, eliminand duplicatele daca exista)
print("Lista dupa transformarea in set este:", set(new_list))
print()

#DICTIONARE- colectie de perechi cheie-valoare, nu accepta duplicate la chei, are indexare prin chei
my_dict={"nume": "John", "varsta": 30, "oras": "New York"}
print("Numele este:", my_dict["nume"])
my_dict["varsta"]=31 #modificam valoarea pentru cheia "varsta"
my_dict["profesie"]="Programator" #adaugam o noua pereche cheie-valoare
print("Dictionarul este:", my_dict)