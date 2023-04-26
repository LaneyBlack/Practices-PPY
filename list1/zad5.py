#Ex5 - 2pkt
points = [150, 123, 110, 108, 80, 76, 74, 71, 70, 65, 49, 38, 29]
players = ("Laney_Black", "AfanIvan", "Sfur1", "LVNDMARK", "SkipSG", "Senwise", "DiversityGaming",
              "SquishyMuffinz", "Scrub Killa", "GarrettG", "Kronovi", "Jstn", "Sizz")  # size = 13
dic = {players[i]: points[i] for i in range(len(players))}
print(dic)