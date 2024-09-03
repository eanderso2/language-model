import random as r


def interprt(user:str):
    userInput = user.lower().split(" ")
    replacedWords = []
    subjectsFile = open("subjects", "r")
    subjects = list(subjectsFile.read().split(","))
    posableSubjects = []
    for worda in subjects:
        if userInput.__contains__(worda):
            posableSubjects.append(worda)
        elif userInput.__contains__("hi"):
            return "hello", "james"
    if posableSubjects != []:
        subject : str = r.choice(posableSubjects)
    else:
        subject = None

    suffix = []
    prefix = []

    for wordb in userInput:
        match wordb:
            case "your":
                replacedWords.append("my")
            case "what" | "who" | "do" | "doing" | "how" | "where" | "when" | "why":
                continue
            case "you":
                replacedWords.append("i")
            case "my":
                replacedWords.append("your")
            case "are":
                replacedWords.append("am")
            case "can":
                prefix.append(wordb)
            case "is":
                suffix.append(wordb)
            case _:
                replacedWords.append(wordb)
    replacedWords = [*prefix, *replacedWords, *suffix]
    replacedWords = " ".join(replacedWords)
    return replacedWords, subject
