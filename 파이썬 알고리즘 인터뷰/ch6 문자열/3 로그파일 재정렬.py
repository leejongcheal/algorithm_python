logs = ["dig1 8 1 5 1","let2 art can","dig2 3 6","let1 art can","let3 art zero"]
letter, digits = [], []
for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letter.append(log)
letter.sort(key=lambda x : (x.split()[1:], x.split()[0]))
print(letter + digits)