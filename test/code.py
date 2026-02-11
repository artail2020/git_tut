def question_exclamation_text(text1: str, text2: str):
    result1 = text1 + "?"
    result2 = text2 + "!"
    return result1, result2

r1, r2 = question_exclamation_text("apple", "banana")
print(r1 + " " + r2)
