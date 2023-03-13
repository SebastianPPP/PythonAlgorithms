# insertion sorting - dosyc szybki algorytm
# szukający kolejnych wartości do wstawienia
# na listę i wstawia ją tylko raz

def sort_insert(list):
    # zaczynamy od elementu 1, bo pierwszy jest "posortowany"
    # każda część musi być ustawiona, więc iterujemy
    # po wszystkich elementach
    for sort_border in range(1, len(list)):
        # tu przerzucamy nowy element do podlisty posortowanych elementów
        curr_idx = sort_border - 1
        value = list[curr_idx + 1]  # kolejna wartość, ktora dodajemy do listy

        while list[curr_idx] > value and curr_idx >= 0:
            list[curr_idx + 1] = list[curr_idx]
            curr_idx = curr_idx - 1

        # kiedy dobra pozycja zostaje znaleziona przerzucamy wartość
        # do oryginalnej listy na jej właściwe miejsce
        list[curr_idx + 1] = value
        print(f'Debug {sort_border} - {list}')


list = [1, 2, 4, 2, 3, 6, 7, 4, 3, 2, 5, 1]
sort_insert(list)
