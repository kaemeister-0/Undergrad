desc="my favourite animal id dog. a dog has sharp teeth so that it can eat flesh easily?"
for i in desc:
    if i==('.','!','?'):
        desc = desc[0].upper()+desc[1:]
    else:
        desc = desc[0].upper()+desc[1:]
print(desc)