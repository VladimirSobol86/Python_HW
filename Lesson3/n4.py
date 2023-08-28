items = {'палатка': 4, 'вода': 1, 'топор': 2, 'дрова': 5, 'удочка': 3}
max_weight = 10
backback = []
for item, weight in items.items():
    if weight <= max_weight:
        backback.append(item)
        max_weight -= weight
print(backback) 