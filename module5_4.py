class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(self.name, 'снесён, но он останется в истории')

    #def go_to(self, new_floor):
        #for i in range(1, new_floor + 1):
            #if i <= new_floor <=self.number_of_floors:
                #print(i)
            #else:
                #print('Такого этажа не существует')
                #break

    #def __len__(self):
       # return self.number_of_floors


    #def __str__(self):
        #return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


    #def __eq__(self, other):
        #if isinstance(other, House):
            #return self.number_of_floors == other.number_of_floors

    #def __add__(self, value):
        #if isinstance(value, int):
            #return House(self.name, self.number_of_floors + value)

    #def __gt__(self, other):
        #return self.number_of_floors > other.number_of_floors

    #def __ge__(self, other):
        #return self.number_of_floors >= other.number_of_floors

    #def __lt__(self, other):
        #return self.number_of_floors < other.number_of_floors

    #def __le__(self, other):
        #return self.number_of_floors <= other.number_of_floors

    #def __ne__(self, other):
        #return self.number_of_floors != other.number_of_floors






h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

#print(h1)
#print(h2)

#print(len(h1))
#print(len(h2))

#print(h1 == h2)

#h1 = h1 + 10
#print(h1)
#print(h1 ==h2)

#h1 += 10
#print(h1)

#h2 = h2 + 10
#print(h2)

#print(h1 > h2)
#print(h1 >= h2)
#print(h1 < h2)
##print(h1 <= h2)
#print(h1 != h2)
