class Score:
    def __init__(self, points):
        self.points = points

    def __eq__(self, other):
        return self.points == other.points


score1 = Score(500)
score2 = Score(500)
score3 = Score(300)

print(score1 == score2)
print(score1 == score3)
