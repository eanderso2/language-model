import AIchatbot2
import interprter as i
import formatter

formatter
while True:
    user, subject = i.interprt(input("User: "))
    response = AIchatbot2.runAI(user, subject)
    print(response)
