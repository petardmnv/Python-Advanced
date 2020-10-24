from collections import deque
customers = deque(map(int, input().split(", ")))
taxi = list(map(int, input().split(", ")))

time = 0
is_driven = True

while len(customers) > 0:
    if len(taxi) == 0:
        is_driven = False
        break
    customer_num = customers.popleft()
    taxi_num = taxi.pop()
    if customer_num <= taxi_num:
        time += customer_num
    else:
        customers.appendleft(customer_num)

if is_driven:
    print('All customers were driven to their destinations')
    print(f'Total time: {time} minutes')
else:
    print("Not all customers were driven to their destinations")
    print(f"Customers left:", format(", ".join(map(str, customers))))
