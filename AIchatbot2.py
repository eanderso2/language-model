import random

def getWord(seedWords : str,data : str):
    startAt = 0
    possableWords = []
    while data.find(seedWords, startAt) != -1:
        word = ""
        itterations = 0
        while (
            not word.endswith(" ")
            and not word.endswith(".")
            and not word.endswith("!")
            and not word.endswith("?")
        ):
            word += data[
                data.find(seedWords, startAt) + len(seedWords) + itterations
            ]
            itterations += 1
        startAt = (
            data.find(seedWords, startAt) + len(seedWords) + itterations + 1
        )
        possableWords.append(word)
    if possableWords != []:
        return possableWords
    else:
        return []

def getLast(list : list,int : int):
    int = len(list) - int
    while int > 0:
        list.pop(0)
        int -= 1

def runAI(sentence:str, subject:str = None):
    TDfile = open("trainingData", "r")
    trainingData = TDfile.read().lower()

    sentence += " "
    speceficData = ""
    trainingSentences = trainingData.replace("!","!.").replace("?","?.").split(".")
    if subject == None:
        speceficData = trainingData
    else:
        for x in trainingSentences:
            if x.__contains__(" " + subject + " "):
                speceficData += x + "."
    speceficData = speceficData.replace("!.","!").replace("?.","?").replace("..", ".")
    print(speceficData)
    while not sentence.endswith("."):
        possableWords = list(getWord(sentence, speceficData))
        possableWords.extend(list(getWord(" ".join(getLast(sentence.split(" "),3)), speceficData)))

        if possableWords == []:
            possableWords = getWord(sentence,speceficData)
        print(possableWords)
        sentence += random.choice(possableWords)
    return sentence
