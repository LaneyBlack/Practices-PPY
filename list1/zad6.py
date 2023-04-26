#Ex6 - 4pkt
points = [150, 123, 110, 108, 80, 76, 74, 71, 70, 65, 49, 38, 29]
dates = ["14.5.2022","18.7.2022","12.9.2022","16.4.2022","11.9.2022","19.9.2022","6.7.2022","23.1.2022",
         "11.3.2021","12.2.2020","27.2.2019","5.10.2022","7.8.2020"]
players = ["Laney_Black", "AfanIvan", "Sfur1", "LVNDMARK", "SkipSG", "Senwise", "DiversityGaming",
              "SquishyMuffinz", "Scrub Killa", "GarrettG", "Kronovi", "Jstn", "Sizz"]  # size = 13
dic = {players[i]: [{dates[j]:points[j] for j in range(len(dates))}] for i in range(len(players))}
print(dic)