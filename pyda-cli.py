import wikipedia
import wolframalpha

while True:
    my_input = input("Question: ")

    try:
        #wolframalpha code here
        app_id = "Q2HXJ5-GYYYX6PYYP"

        #let's call our app id
        client = wolframalpha.Client(app_id)
        res = client.query(my_input)
        answer = next(res.results).text 

        print(answer)

    except:
        #wikipedia
        print(wikipedia.summary(my_input)) 