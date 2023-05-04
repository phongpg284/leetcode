class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rad = 0
        dire = 0
        new = ""
        for player in senate:
            if player == "R":
                if dire > 0:
                    dire -= 1
                else:
                    new += 'R'
                    rad += 1
            else:
                if rad > 0:
                    rad -= 1
                else: 
                    new += 'D'
                    dire += 1

        while(rad > 0):
            i = new.find("D")
            if i == -1:
                return "Radiant"
            new = new[:i] + new[i+1:]
            rad -= 1

        while(dire > 0):
            i = new.find("R")
            if i == -1:
                return "Dire"
            new = new[:i] + new[i+1:]
            dire -= 1

        return self.predictPartyVictory(new)