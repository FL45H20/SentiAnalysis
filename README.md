# SentiAnalysis
This is a Sentment Analysis tool written in Python using TextBlob libary. It is made for teaching sentimnet analysis to beginners.

## Working
1. It will first take a paragraph as i/p using cmd line args. It can have a single sentence or more than one sentence as i/p.
2. Then it will pass this sentence to TextBlob object. This TextBlob object has many methods for natural language processing and its simple to use too.
3. We are using a method called sentiment to do sentiment anlaysis on our text. This methods first extract each word form a sentence of para and removes unnecessary words (Stop Words) such as is, am, are etc and these list of words is called Tokens, it also automatically checks for spell mistake and correct them. Then it uses its huge dictionary to get subjectivity and polarity scores of each word in tokens. Then it multiplies the subjectivity and polarity score of each word in sentence to get sentiment of sentence. For sentiment of whole paragraph we can get average sentiment of each sentence in the para.

## Use
```
pip install textblob
git clone https://github.com/FL45H20/SentiAnalysis.git
cd SentiAnalysis
python sentianalysis.py "she is beautiful." "fuck you"
```

### Sample o/p
```
python sentianalysis.py "she is beautiful." "fuck you"
```

#### Output:
```
she is beautiful.
Polarity: 0.85 Subjectivity: 1.0
fuck you
Polarity: -0.4 Subjectivity: 0.6
```
