from vaderSentiment import SentimentIntensityAnalyzer

import csv
import json



dayCompoundDict = {}

sentences = []

#set the day and stock looking for
#day = "2022-05-27"
stock = "TSM"
days = []
# Open the CSV file

with open('stock_tweets.csv', newline='') as csvfile:


    #get the days to analyze
    daysReader = csv.reader(csvfile)
    for row in daysReader:
        currentDay = row[0][:10]
        if currentDay in days:
            pass
        else:
            days.append(currentDay)
   
    #run the analysis for each day
for day in days:
    with open('stock_tweets.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        sentences = []
        for row in reader:
            currentDay = row[0][:12]
            if row[2].startswith(stock) and currentDay.startswith(day):
                sentences.append(row[1])

        analyzer = SentimentIntensityAnalyzer()

        compoundValues = []

        for sentence in sentences:

            vs = analyzer.polarity_scores(sentence)

            data = json.loads(str(vs).replace("'", "\""))
            compoundVal = data['compound']
            compoundValues.append(compoundVal)

            #print("{}".format(str(compoundVal)))
        length = len(compoundValues)
        if length != 0:
            avgVal = sum(compoundValues)/len(compoundValues)
            print("On %s,  %s had %d tweets with an average compound value of %f" % (day,stock,length,avgVal))
            dayCompoundDict[day] = avgVal
        else:
            dayCompoundDict[day] = 0;
            print("No tweets for %s on %s" % (stock, day))
            pass
#write data to output csv file
with open('tsmOutputs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Day','Compound Sentiment'])
    for key, value in dayCompoundDict.items():
        writer.writerow([key,value])
