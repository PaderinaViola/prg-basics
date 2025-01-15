arr = [(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

final_scores = list(map(lambda scores: sum(scores) - max(scores) - min(scores), arr))
print(final_scores)