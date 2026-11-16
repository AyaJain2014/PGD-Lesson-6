Football = ("Doue", "Yamal", "Olise", "Diomande")
print(type(Football))

#packing - The process of assigning values to a tuple is known as packing.
address = (210, "Brickfield Apartment", "Banglore", "Karnataka", 564000)

for i in address:
    print(i)

#unpacking - Unpacking tuples assigns the objects in a tuple to multiple variables.
houseno, apartment, city, state, pin = address

print("House number: ", houseno)
print("apartment:", apartment)
print("city: ", city)
print("state: ", state)
print("pin: ", pin)

# A tuple can be created without parantheses

soccer = "Doue", "Neymar", "Ndiaye", "Messi", "Neymar", "Ronaldo"
print(type(soccer))

#Nested tuple
myTuple = ("mouse", (1, 2, 3), [10,45,60])

print(myTuple[0])
print(myTuple[0][3])

clubs = ("Real Madrid", "Barcelona", "Galatasuray", "PSG", "Bayern", "Red Star Belgrade")
#clubs[3] = "Liverpool" - tuple is immutable; you cannot change the value of tuple.

my_tuple1 = ("apple", "banana")
my_tuple2 = ("cherry", "orange")
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3)

print(my_tuple3 * 5)
print(len(my_tuple3))

food = ("Pizza", "Pasta", "Soup", "Sushi", "Salad", "Fondue", "Noodles")
if "burger" in food:
    print("Yes")
else:
    print("No")

print(food[0:4])
print(food[:4])
print(food[4: 7])
print(food[4:])