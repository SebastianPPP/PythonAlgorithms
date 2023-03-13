#Aby skorzystaæ z tego, nasza lista musi byæ
#uprzednio posortowana. Zaczynamy poszukiwanie od œrodka
#a nastêpnie pytamy, czy jest ona mniejsza lub wiêksza.

#Je¿eli w mid nie ma szukanej wartoœci i jest ona wiêksza od mid,
#to start przenosimy na kolejny indeks i ponownie
#odpalamy szukanie mid.

#Je¿eli szukana jest na lewo, to przenosimy end.
#Koniec gdy mid = szukana

#Jeœli nie ma szukanej w liœcie to start wyprzedzi
#w pewnej chwili end i to konczy pêtle mówi¹c, ¿e
#szukanej brak

def search_binary(value, list):
    
    start = 0
    end = len(list)-1
    found = False
    
    while start <= end and not found:
        print(f'DEBUG {start} - {end}')
        mid = (start+end)//2
        if list[mid] == value:
            found = True
        else:
            if value < list[mid]:
                end=mid-1
            else:
                start = mid + 1

    if found:
        return mid
    else: 
        return None

list = [0,1,2,3,4,5,6,7,8,9]
value = 5
idx = search_binary(value, list)
print(f'{value} is on the {list} on position {idx}')