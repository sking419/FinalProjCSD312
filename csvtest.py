import csv



# Initialize the 'sentences' array

sentences = []



# Open the CSV file

with open('stock_tweets.csv', newline='') as csvfile:

    # Create a CSV reader object

    reader = csv.reader(csvfile)

    

    # Iterate through each row in the CSV file

    for row in reader:

        # Check if the first item starts with '2022-09-29' and the third item starts with 'TSLA'

        if row[0].startswith('2022-09-29 12') and row[2].startswith('TSLA'):

            # Add the second item to the 'sentences' array

            sentences.append(row[1])



# Print the sentences array

print(sentences)


