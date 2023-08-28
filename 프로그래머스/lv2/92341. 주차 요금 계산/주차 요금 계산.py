def solution(fees, records):
    answer = []
    cars = {}
    pay = {}
    for i in records:
        time, car, k = i.split()
        h, m = time.split(':')
        if k == 'IN':
            if car not in cars:
                cars[car] = int(h) * 60 + int(m)
        elif k == 'OUT':
            t = int(h) * 60 + int(m) - cars[car]
            if car not in pay:
                pay[car] = t
            else:
                pay[car] += t
            cars.pop(car) 
    if len(cars) > 0:
        for car, time in cars.items():
            if car not in pay:
                pay[car] = (1439 - time)
            else:
                pay[car] += (1439 - time)
    free_t, free_p, add_t, add_p = fees
    for car, time in sorted(list(pay.items())):
        if free_t > time:
            answer.append(free_p)
        else:
            if (time - free_t) % add_t:
                add_pay = ((time - free_t) // add_t + 1) * add_p
                answer.append(free_p + add_pay)
            else:
                answer.append(free_p + (time - free_t) // add_t * add_p)
            
    return answer