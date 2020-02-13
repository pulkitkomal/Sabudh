from PIL import Image as image
import os
from nltk.tokenize import word_tokenize
from tesserocr import PyTessBaseAPI
import pickle
from pymongo import MongoClient

class punjabiExtraction():
    # stop words for extraction
    stopWords = ['a.', 'n.', 'nn.', 'adv.', 'aa.', 'abf.', 'advv.', 'attrib.', 'cap.', 'collect.', 'comb. forms',
                 'comb. form', 'conj.', 'esp.', 'i.', 'imperat.', 'ind. art.', 'int.', 'intt.', 'l.c.', 'neg.', 'nn.',
                 'oft.', 'pass.', 'pers.', 'phr.', 'pl.', 'poss.', 'pred.', 'pref.', 'preff.', 'prep.', 'prepp.',
                 'pres.p.', 'pres.t.', 'pron.', 'p.p.', 'p.t.', 'sent.', 'sing.', 'suf.', 'suff.', 'super.', 't.',
                 'usu.', 'v.vb.', 'var.', 'v.aux.', 'v.i.', 'v.refl.', 'v.subst.', 'v.t.', 'vv.', '#.', '».']

    punjabiEnglish_Dict = {}
    punjabiString = ""
    englishString = ""
    index = 0
    count = 0
    # to break the loop
    wordFlag = False
    # to extract the string
    def text_input(self):
        with PyTessBaseAPI(lang='gur+eng') as api:
            direc = input('Enter Directory for images: ')
            ent = os.listdir(r'{}'.format(direc))
            text_data = []
            for i in ent:
                img = image.open(r'{}'.format(direc) + '/' + i)
                gray = img.convert('L')
                blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
                blackwhite.save(r"outputS.jpg")
                api.SetImageFile(r"outputS.jpg")
                Text = api.GetUTF8Text()
                text_data.append(Text)
                self.count = self.count + 1
                print(self.count)

        # removing the new line characters
        text_data = [i.replace("\n", " ") for i in text_data]
        text_data = [i.replace(r"\u", " ") for i in text_data]

        text = str(text_data).replace(r"\n", " ")
        return text

    def is_ascii(self, string):
        return all(ord(c) < 128 for c in string)

    def stringInput(self, rawInput):

        # splitting the raw input
        spaceSplit = word_tokenize(rawInput)
        return spaceSplit

    def extraction(self):
        rawInput = self.text_input()
        temp_stringInput = self.stringInput(rawInput)
        while True:
            englishDelta = -1
            if self.index >= len(temp_stringInput):
                break
            else:
                singleChar = temp_stringInput[self.index]
                if singleChar in self.stopWords and self.wordFlag:
                    self.punjabiEnglish_Dict[self.englishString] = self.punjabiString

                    # finding how many steps we need to take back to find the english character
                    currentChar = temp_stringInput[self.index]
                    bol = True
                    while bol:
                        if self.is_ascii(currentChar):
                            englishDelta = englishDelta - 1
                            currentChar = temp_stringInput[self.index + englishDelta]

                        else:
                            bol = False
                    lst1 = []
                    x = temp_stringInput[self.index + englishDelta:self.index]

                    for x in x:

                        if self.is_ascii(x):
                            lst1.append(x)

                    newEnglish_Char = " ".join(lst1)
                    self.punjabiString = self.punjabiString.replace(newEnglish_Char, "")
                    self.punjabiEnglish_Dict[newEnglish_Char] = self.punjabiString
                    self.punjabiString = ""

                    self.wordFlag = True

                elif singleChar in self.stopWords:
                    self.englishString = temp_stringInput[self.index]
                    self.wordFlag = True
                elif self.wordFlag:
                    if not self.is_ascii(singleChar):
                        self.punjabiString += singleChar + " "
                self.index += 1
        return self.punjabiEnglish_Dict





pe = punjabiExtraction()
temp_dict = pe.extraction()

with open ("dummy_file.pkl","wb") as dummy:
   pickle.dump(temp_dict,dummy)
with open("dummy_file.pkl","rb") as dummy:
   dummy_test_data=pickle.load(dummy)


#D:\PyCharm\Sabudh\punjabi
