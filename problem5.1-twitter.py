import math
tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
number_of_tweets = len(tweets)
# Determine the number of tweets in the dataset that can be classified as happy.
number_of_happy_tweets = 0
for i in range(len(tweets)):
    for word in happy_words:
        # Check if the tweet contains the word
        if word in tweets[i]:
            number_of_happy_tweets += 1

print(number_of_happy_tweets)
#What fraction of the total number of tweets are happy?
happy_fraction = number_of_happy_tweets/number_of_tweets
print(happy_fraction)


#Determine the number of tweets in the dataset that can be classified as sad.
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']
number_of_sad_tweets = 0
for i in range(len(tweets)):
    for word in sad_words:
        # Check if the tweet contains the word
        if word in tweets[i]:
            number_of_sad_tweets += 1

print(number_of_sad_tweets)

#What fraction of the total number of tweets are sad?
sad_fraction = number_of_sad_tweets /number_of_tweets
print(sad_fraction)

#Q16b (Optional): Calculate the sentiment score, which is defined as the difference betweek the fraction of happy tweets and the fraction of sad tweets.
sentiment_score = (happy_fraction-sad_fraction)
print("The sentiment score for the given tweets is {}".format(sentiment_score,".2f"))
#Display whether the overall sentiment of the given dataset of tweets is happy or sad, using the sentiment score.
if sentiment_score<.5:
    print("The overall sentiment is happy")
else:
    print("The overall sentiment is sad")

#Q16d (Optional): What is the fraction of tweets that are neutral i.e. neither happy nor sad.
number_of_neutral_tweets = 0
for i in range(len(tweets)):
    for word in sad_words and happy_words:
        # Check if the tweet contains the word
        if word in tweets[i]:
            number_of_neutral_tweets -= 1
            


print(number_of_neutral_tweets)