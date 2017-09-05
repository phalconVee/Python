import wikipedia

while True:
    my_input = input("Question: ")
    wikipedia.set_lang("es")
    print(wikipedia.summary(my_input, sentences=2))

    