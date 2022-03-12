import numpy as np
import csv



playoffTeams = [
         "Philadelphia Phillies", "Atlanta Braves",
         "St. Louis Cardinals", "Toronto Blue Jays", "Boston Red Sox", "New York Yankees", "Chicago White Sox",
         "Milwaukee Brewers", "Houston Astros", "Tampa Bay Rays", "Los Angeles Dodgers", "San Francisco Giants"
         ]

lottoTeams = ["Baltimore Orioles", "Arizona Diamondbacks", "Texas Rangers", "Pittsburgh Pirates", "Washington Nationals",
              "Miami Marlins", "Chicago Cubs", "Minnesota Twins", "Kansas City Royals", "Colorado Rockies",
              "Detroit Tigers", "Los Angeles Angels", "New York Mets", "San Diego Padres", "Cleveland Guardians",
              "Cincinnati Reds", "Oakland Athletics", "Seattle Mariners"]
# print(len(lottoTeams))
for x in range(1001):
    draftOrder = np.random.choice(lottoTeams, size=len(lottoTeams), replace=False, p=[.165, .165, .165, .1325, .1, .075,
                                                                                      .055, .039, .027, .018, .014,
                                                                                      .011, .009, .0076,
                                                                                      .0062, .0048, .0036, .0023])
    with open('insertyourfiledirectoryhere', "a", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(draftOrder)

    print(*draftOrder, sep="\n")

