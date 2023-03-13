#ten algorytm dostarcza szybkie rozwiazanie
#jednak nie zawsze bedzie ono optymalne

#przyk³ad pakowania plecaka - wcielamy sie w zlodzieja
#i chcemy ukrasc jak najwiecej rzeczy
#limitem jest pojemnosc naszego plecaka

#pierwszy pomysl polega na wpakowaniu najcenniejszych rzeczy
#drugi to pakowanie najlzejszych przedmiotow
#trzeci - wskaznik oplacalnosci = wartosc/waga


def backback_greedy(weights, values, total_weight):

    data = []
    for i in range(len(weights)):
        data.append({
            "v": values[i],
            "w": weights[i],
            "cost": float(values[i])/float(weights[i])
            })
        
    data = sorted(data, key = lambda x: x['cost'], reverse = True)
    print(f'DEBUG: {data}')

    remain = total_weight
    result = 0
    result_list = []
    i = 0

    while i < len(data):
        if(data[i]['w']) <= remain:
            remain -= data[i]['w']
            result += data[i]['v']
            result_list.append(data[i])
            print(f"DEBUG: addind {data[i]} - total value = {result} remaining space = {remain}")
        i+=1
    return result, result_list

backback_greedy([5, 10, 20, 15, 10],[100, 20, 50, 300, 200], 50)