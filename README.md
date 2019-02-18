# Reuters News
Natural Language Processing to detect sentences are positive or negative

## Install
```
pip install NLP-python
```

## Usage
- Initializing
```
from NLP import NLP
nlp = NLP()
```
- Traning
Input a list of sentences, it will create a model file
```
nlp.training(list)
```
- Get model file
```
nlp.getModel()
```
- Match your sentence(list) to model, it will return a score
```
nlp.match(sentence)
```
