import string
from collections import Counter
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def sentiment_analyse(text):
    obj=SentimentIntensityAnalyzer()
    sentiment_dict = obj.polarity_scores(text)
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("tweets are rated as ", sentiment_dict['neg']*100, "% Negative")
    print("tweets are rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("tweets are rated as ", sentiment_dict['pos']*100, "% Positive")
 
    print("Tweets sentiment Overall Rated As", end = " ")
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
    else :
        print("Neutral")



# reading text file
text = open('tweets.txt', encoding='utf-8').read()

# converting to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# splitting text into words
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization - From plural to single + Base form of a word (example better-> good)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)


emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')
        if word in lemma_words:
            emotion_list.append(emotion)

print("************************************************* TWEETS EMOTIONS *********************************************************\n",emotion_list)
print("************************************************** TWEETS EMOTIONS COUNT *******************************************************")
emotion_count = Counter(emotion_list)
print(emotion_count)
print("*********************************************** SENTIMENT INTENSITY OF THE TWEETS ************************************************")
sentiment_analyse(cleaned_text)
fig, ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
plt.pie(emotion_count.values(),labels=emotion_count.keys(),shadow=True)
fig.autofmt_xdate()
plt.savefig('pie.png')
plt.show()