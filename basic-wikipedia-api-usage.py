import wikipedia

while True:
    my_input = input("Question: ")
    print(wikipedia.summary(my_input))