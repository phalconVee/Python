'''
Wolframalpha app credentials:
APP NAME: pyda
APPID: Q2HXJ5-GYYYX6PYYP
USAGE TYPE: Personal/Non-commercial Only
'''
import wolframalpha
app_id = "Q2HXJ5-GYYYX6PYYP"

''' Basic usage of wolframalpha library

client = wolframalpha.Client(app_id)
res = client.query('temperature in Washington, DC on October 3, 2012')
print(next(res.results).text) '''

#let's call our app id
client = wolframalpha.Client(app_id)

my_input = input("Question: ")
res = client.query(my_input)
answer = next(res.results).text 

print(answer)
