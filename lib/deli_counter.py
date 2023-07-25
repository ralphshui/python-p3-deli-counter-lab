def line(customers):
    if len(customers) > 0:
        total_queue = []
        for person in customers:
            current_queue = customers.index(person)
            message = f" {current_queue+1}. {person}"
            total_queue.append(message)
        print(f"The line is currently:{ ''.join(total_queue)}")
    else:
        print("The line is currently empty.")

def take_a_number(queue, name):
    queue.append(name)
    print(f"Welcome, {name}. You are number {queue.index(name)+1} in line.")

def now_serving(queue):
    if len(queue) > 0:
        name = queue[0]
        queue.pop(0)
        print(f"Currently serving {name}.")
    else:
        print("There is nobody waiting to be served!")
