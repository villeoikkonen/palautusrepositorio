class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.p1_name = player1_name
        self.p2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self.tie()

        elif self.p1_score >= 4 or self.p2_score >= 4 and abs(self.p1_score - self.p2_score) >= 1:
            return self.tie_breaker(self.p1_score, self.p2_score)

        else:
            return self.uneven_score()

    def tie(self):
        return self.scores[self.p1_score] + "-All" if self.p1_score < 3 else "Deuce"
    
    def tie_breaker(self, p1_score, p2_score):
        difference = p1_score - p2_score
        if difference == 1:
            score = f"Advantage {self.p1_name}"
        elif difference == -1:
            score = f"Advantage {self.p2_name}"
        elif difference >= 2:
            score = f"Win for {self.p1_name}"
        else:
            score = f"Win for {self.p2_name}"
        return score
    
    def uneven_score(self):
        return self.scores[self.p1_score] + "-" + self.scores[self.p2_score]