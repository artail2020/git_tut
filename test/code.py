kanto: list[str] = ["千葉", "栃木", "東京", "埼玉", "茨城", "群馬", "神奈川"]
x: list[str] = [f"{i}都" if (i == "東京") else f"{i}県" for i in kanto]
print(x)
