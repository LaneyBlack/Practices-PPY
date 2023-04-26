#Ex4 - 5pkt
costsBefore = (3.69, 4.5, 3.6, 4.0, 3.99, 3.59)
costsAfter = (4.5, 5.5, 4.69, 4.99, 4.00)
print("Max cost after taxes: ", max(costsAfter))
print("Min cost overall: ", min(costsAfter+costsBefore))
print("Average cost before taxes: ", sum(costsBefore) / len(costsBefore))
print("Average cost overall: ", sum(costsAfter) / len(costsAfter))