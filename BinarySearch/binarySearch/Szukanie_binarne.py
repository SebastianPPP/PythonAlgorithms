#Aby skorzysta� z tego, nasza lista musi by�
#uprzednio posortowana. Zaczynamy poszukiwanie od �rodka
#a nast�pnie pytamy, czy jest ona mniejsza lub wi�ksza.

#Je�eli w mid nie ma szukanej warto�ci i jest ona wi�ksza od mid,
#to start przenosimy na kolejny indeks i ponownie
#odpalamy szukanie mid.

#Je�eli szukana jest na lewo, to przenosimy end.
#Koniec gdy mid = szukana

#Je�li nie ma szukanej w li�cie to start wyprzedzi
#w pewnej chwili end i to konczy p�tle m�wi�c, �e
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