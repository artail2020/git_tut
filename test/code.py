x_list: list[str] = ["apple", "orange", "banana"]
s: str = "\n".join(x_list)

with open("./foo3.txt", "w", encoding="utf-8") as f:
    f.write(s)
