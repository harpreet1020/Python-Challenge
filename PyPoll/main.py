import csv

election_data = '/Users/HarpreetSingh/Desktop/Python-Challenge/election_data.csv'

with open(election_data, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=',')

    next(csvreader)

    tot_votes = []
    candidates = []
    unique_candidates = []

    #Loop through the data
    for col in csvreader:
        tot_votes.append(col[0])
        candidates.append(col[2])

    for i in candidates:
        if candidates not in unique_candidates:
            unique_candidates.append(i)



    print('Election Results\n----------------')
    print("Total Votes:", len(tot_votes))
    print('---------------------')
    print(unique_candidates)

