num: list[int] = [5, 8, 10, 12, 30]
result: list[int] = list(filter(lambda x: x >= 10, num))
print(result)
