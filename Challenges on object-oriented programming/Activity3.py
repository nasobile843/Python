class FruitQuiz:

    def __init__(self):
        self.fruits={'apple':'red', 'orange':'orange', 'watermelon':'green', 'banana':'yellow'}

    def quiz(self):
        while(True):
            fruit, colour = random.choice(list(self.fruits.items()))
            print("What is the colour of {}".format(fruit))
            user_answer = input()
            if(user_answer.lower() == colour):
                print("Correct answer")
            else