class Player:

    #writing
    def write(score):
        file = open('score.txt', 'a') #a => append, w => write, r => read
        file.writelines(score+'\n')
        file.close()

    #reading
    def read(self):
        file = open('score.txt', 'r')
        count = 0 
        for i in file:
            count += 1
        
        count -= 3
        new = 0
        while count:
            new = max(file.readline(int(i)), file.readline(eval(i)+1))
            count -= 1
        print(int(new))
        return new

            
    
    def get_best(self):
        best = self.read()
        return int(best)
    