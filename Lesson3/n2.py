digit_list = [1,2,2,3,3,4]
new_list = []

for i in digit_list:
    if digit_list.count(i) > 1:
        new_list.append(i)
final_list = set(new_list)
print(final_list)