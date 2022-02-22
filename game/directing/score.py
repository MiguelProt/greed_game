class Score:

    def __init__(self):
        self.__score = 600
        self.__substract = 50
        self.__add = 50

    def update_points(self, operation):
        if operation == '+':
            self.__score = self.__score + self.__add
        elif operation == '-':
            print("discounting")
            self.__score = self.__score - self.__substract
        else:
            self.__score = 0
    
    def show_score(self):
        score_message = "Score: " + str(self.__score)
        return score_message