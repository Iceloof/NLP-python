import pandas as pd
import numpy as np
import warnings
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

class NLP:
        def __init__(self):
                warnings.filterwarnings("ignore")
                self.model = {'model':'model'}
        
        def training(self,input_list):
                for item in input_list:
                        print(item)
                        status=input("Positive/Negative(1?0):")
                        f = open("model","a")
                        f.write(item+"\t"+status+"\n")
                        f.close()        
        
        def getModel(self):
                df_list = []
                for source, filepath in self.model.items():
                        df = pd.read_csv(filepath, names=['sentence','label'], sep='\t')
                        df['source'] = source
                        df_list.append(df)
                        df= pd.concat(df_list)
                        df_model = df[df['source'] == 'model']
                        self.sentences = df_model['sentence'].values
                        self.label = df_model['label'].values

        def match(self, test):
                test_train = np.ones(len(test), dtype=np.int)
                vectorizer = CountVectorizer()
                vectorizer.fit(self.sentences)
                train = vectorizer.transform(self.sentences)
                test = vectorizer.transform(test)
                classifier = LogisticRegression()
                classifier.fit(train, self.label)
                score = classifier.score(test, test_train)
                return score

