class Player:

    #writing
    @staticmethod
    def write(score):
        with open('score.txt', mode="w+", encoding="utf-8") as myfile:
            myfile.write(str(score))
    

    #reading
    def read(self):
        with open('score.txt', encoding="utf-8") as myfile:
            return(int(myfile.read()))

            
    
    def get_best(self):
        best = self.read()
        return int(best)
    