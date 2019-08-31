class readFile(object):
    frequency = {}
    totalLetters = 0
    probability = {}
    fileName = ''

    def __init__(self, name='Words.txt'):
        self.fileName = name
        self.getFrequencies()
        self.getProbabilities()

    def getFrequencies(self):
        with open(self.fileName, "r") as words:
            contents = words.read().lower()
            words.seek(0)
            for char in contents:
                self.totalLetters = self.totalLetters+1
                if char in self.frequency:
                    self.frequency[char] = self.frequency[char] + 1
                else:
                    self.frequency[char] = 1

        return self.frequency

    def getProbabilities(self):
        for key in self.frequency:
            self.probability[key] = (self.frequency[key] / self.totalLetters)
        return self.probability

    def extractMax(self):
        maxValue = 0
        maxKey = ""
        for key in self.probability:
            if self.probability[key] > maxValue:
                maxValue = self.probability[key]
                maxKey = key
        self.probability[maxKey] = 0
        return maxKey, maxValue