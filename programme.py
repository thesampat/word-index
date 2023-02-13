import re

class CreateIndex():
    def __init__(self, files, word) -> None:
        self.files = files
        self.word = word

    def writeIndex(self, file):
            
            next = 0
            file.write(f'{self.word} : ')
            for index, j in enumerate(self.files):

                if self.word in j:
                   
                    if next > 0 and (index+1) <= len(self.files):
                        file.write(',')

                    file.write(f'{index+1}')

                    next = next+1
                    
            return file
        



class ClearWords():
    def __init__(self, files, exclude) -> None:
        self.files = files
        self.exclude = exclude
        self.clean_words = []
        self.read_files = []
        self.combinewords = []
        self.exclud_words_file = []

    def readfiles(self):

        exclude_open = open(self.exclude, mode='r')
        exclude_read =exclude_open.read()

        for i in exclude_read.split('\n'):
             if i != '':
                self.exclud_words_file.append(i)


        for file in self.files:

            # ope the file
            file = open(file, mode='r')

            # read the files
            readf = file.read().strip('\n')

            self.read_files.append(readf)

        return self.read_files
    
    def getUnqueWords(self, words):
        unique_words_set = set(words)
        return list(unique_words_set)
    
    def clean_file(self):

        # remove special characters
        for read_file in self.read_files:

            words = read_file.replace('\n', ',').replace('.', ',').replace(' ',',').replace('(', ',').replace('“', ',').replace('-', ',')
            words = words.replace(')', ',').replace('"', ',').replace('/', ',').replace(';', ',').replace('"/"', ',').replace(':', ',')
            words = words.split(',')


            #filter out the numbers
            words = [i.lower() for i in words if i.isnumeric() == False]

            # remove any number within string
            complete_char = [re.sub(r'[0-9]', '', i) for i in words]

            final_words = [i.lower() for i in complete_char if i not in self.exclud_words_file  if i != '']

            unique_words = self.getUnqueWords(final_words)

            self.clean_words.append(unique_words)

        return self.clean_words
    
    def getCombinedWords(self):
        for i in clean_words:
                for word in i:
                    self.combinewords.append(word)

        uniqueCombinedWords = self.getUnqueWords(self.combinewords)

        

        uniqueCombinedWords.sort()

        return uniqueCombinedWords

            
        

text_files = ['Page1.txt', 'Page2.txt', 'Page3.txt']
exclude_file = 'exclude-words.txt'

f = ClearWords(text_files, exclude_file)
readed = f.readfiles()
clean_words = f.clean_file()

uniqueCombinedWords = f.getCombinedWords()

initial = True

for word in uniqueCombinedWords:
    indexx = CreateIndex(clean_words, word)
    with open('demofile3.txt', mode='a+') as file:
        if initial:
            file.write('Word : Page Numbers \n')
            file.write('--------------- \n')
            initial = False
        wrfile = indexx.writeIndex(file)
        wrfile.write('\n')
        




            
        






        
        
    
   