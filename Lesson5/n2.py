name = ["Владимир", "Андрей", "Анна"]
salary = [100000, 200000, 300000]
bonus = ["5%", "7.5%", "10%"]

generate_salary_dict = {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(name, salary, bonus)}

print(generate_salary_dict)
