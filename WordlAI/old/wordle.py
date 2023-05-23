allInputs = ['aesir', 'roier']
feedback = ['', '', '', '🟩', '🟩']

def filter_green(allInputs):
    lastInput = allInputs[-1]
    correctLetter = []
    for i in range(5):
        if feedback[i] == "🟩":
            correctLetter.append(((lastInput[i]), i))
    print(correctLetter)

filter_green(allInputs)