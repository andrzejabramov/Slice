def all_variants(text):
    for i in range(1, len(text)+1):
        for j in range(len(text)):
            if len(text[j:j+i]) == i:
                yield text[j:j+i]


a = all_variants("abc")
for t in a:
    print(t)
