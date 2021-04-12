import time
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import stanza
import pandas as pd
from nltk import tokenize
from textblob import TextBlob
from pattern.en import sentiment, Sentence
import flair


# nltk.download('punkt')



# Evaluating NLP libraries
#
# https://towardsdatascience.com/python-libraries-for-natural-language-processing-be0e5a35dd64
#
# 1) TextBlob
#           https://textblob.readthedocs.io/en/dev/quickstart.html
# 2) Stanza (via CoreNLP)
#           https://stanfordnlp.github.io/stanza/
# 3) VADER (via NTLK)
#           http://www.nltk.org/howto/sentiment.html
# 4) Pattern
#           https://textminingonline.com/getting-started-with-pattern
# 5) Flair
#           https://github.com/flairNLP/flair
#

neg_text = open('cudi_review.txt', 'r').read() # https://pitchfork.com/reviews/albums/21351-speedin-bullet-2-heaven/
pos_text = open('boc_review.txt', 'r').read()  # https://pitchfork.com/reviews/albums/838-music-has-the-right-to-children/

sentences_text = tokenize.sent_tokenize(neg_text)
sentences_text = pd.DataFrame(sentences_text, columns=['Text'])

sentences_text2= tokenize.sent_tokenize(pos_text)
sentences_text2 = pd.DataFrame(sentences_text2, columns=['Text'])


# def timer(func):
#     def wrapper(*args, **kwargs):
#         before = time.time()
#         func(*args, **kwargs)
#         print(func.__name__, "function took:", time.time() - before, "seconds")
#     return wrapper
from functools import wraps
from time import time

def timer(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r took: %2.4f sec' % (f.__name__, te-ts))
        return result
    return wrap





# 1) TEXTBLOB

@timer
def textblob_analyzer(doc):
    txt = TextBlob(doc)
    df = pd.DataFrame(columns=['Sentiment'])
    for i, sentence in enumerate(txt.sentences):
        df = df.append({'Sentiment': sentence.sentiment.polarity}, ignore_index=True)
    return df

blob_neg = textblob_analyzer(neg_text)
print(blob_neg)
# blob_pos = textblob_analyzer(pos_text)

# print('TEXTBLOB')
# print(df_blob)
# print('-' * 20)




# 2) STANZA
# stanza.download('en') # download English model
nlp2 = stanza.Pipeline(lang='en', processors='tokenize,sentiment') # initialize English neural pipeline

@timer
def stanza_analyzer(doc):
    df = pd.DataFrame(columns=['Sentiment'])
    doc_neg = nlp2(doc)
    for i, sentence in enumerate(doc_neg.sentences):
        df = df.append({'Sentiment': sentence.sentiment}, ignore_index=True)
    return df

# stanza_neg = stanza_analyzer(neg_text)
# stanza_pos = stanza_analyzer(pos_text)
# print('STANZA')
# print(df_stanza)
# print('-' * 20)




# 3) VADER via NTLK
# nltk.download('vader_lexicon')

@timer
def vader_analyzer(doc):
    analyzer = SentimentIntensityAnalyzer()
    df = pd.DataFrame(columns=['Sentiment'])
    sentences = tokenize.sent_tokenize(doc)
    for i, sentence in enumerate(sentences):
        # returns neg, neu, pos, compound sentiment for each sentence token
        df = df.append({'Sentiment': analyzer.polarity_scores(sentence)['compound']}, ignore_index=True)
    return df

# vader_neg = vader_analyzer(neg_text)
# vader_pos = vader_analyzer(pos_text)
# print('VADER')
# print(df_vader)
# print('-' * 20)


#  4) Pattern
@timer
def pattern_analyzer(doc):
    df = pd.DataFrame(columns=['Sentiment'])
    sentences = tokenize.sent_tokenize(doc) # nltk tokenizer
    df['Sentiment'] = [sentiment(sentence)[0] for sentence in sentences]  # polarity
    return df


# pattern_neg = pattern_analyzer(neg_text)
# print(pattern_neg)
# pattern_pos = pattern_analyzer(pos_text)

# print('Pattern')
# print(df_pattern)
# print('-' * 20)


#   5) Flair
#       https://christineeeeee.com/posts/nlp_sentiment_tool/

# flair_sentiment = flair.models.TextClassifier.load('en-sentiment')

# Sentiment Score function via Flair

def senti_score(n):
    s = flair.data.Sentence(n)
    flair_sentiment.predict(s)
    total_sentiment = s.labels[0]
    assert total_sentiment.value in ['POSITIVE', 'NEGATIVE']
    sign = 1 if total_sentiment.value == 'POSITIVE' else -1
    score = total_sentiment.score
    return sign * score

@timer
def flair_analyzer(doc):
    df = pd.DataFrame(columns=['Sentiment'])
    sentences = tokenize.sent_tokenize(doc)
    df['Sentiment'] = [senti_score(sentence) for sentence in sentences]
    return df

# flair_neg = flair_analyzer(neg_text)
# flair_pos = flair_analyzer(pos_text)
# print('Flair')
# print(df_flair)
# print('-' * 20)

# cols = ['Index', 'Textblob', 'Stanza', 'VADER', 'Pattern', 'Flair', 'Sentence_Text']
# frame_neg = pd.concat([blob_neg, stanza_neg, vader_neg, pattern_neg, flair_neg, sentences_text], axis=1, ignore_index=True)
# print(frame_neg)

# frame_pos = pd.concat([blob_pos, stanza_pos, vader_pos, pattern_pos, flair_pos, sentences_text2], axis=1, ignore_index=True)
# print(frame_pos)

# pd.set_option("display.max_rows", None, "display.max_columns", None)
# frame_neg.to_excel('negative_sentiment.xlsx')
# frame_pos.to_excel('positive_sentiment.xlsx')


