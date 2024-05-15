from Games import Games
# TODO: add multi choice options to quiz
# TODO: fix implementation of total points
class Quiz(Games):

    QUESTIONS_ANSWER_LIST = [
            ("What is the capital city of France ", "Paris"),
            ("Who wrote the famous play 'Romeo and Juliet' ", "William Shakespeare"),
            ("How many continents are there in the world (enter a digit) ", "7"),
            ("What is the 5th planet in the solar system ","Jupiter" ),
            ("What was Disney's first animated character ", "Mickey Mouse")
        ]
    
    def __init__(self, total_points=0):
        super().__init__("5 Question Quiz Game", "Answer all 5 questions correctly to win", "1")
        self.total_points = total_points
    
    
    def play(self):
        playing = input("Are you ready to play?(yes/no) ")

        if playing != "yes":
            quit()
        
        print("okay let's play")

        i = 1
        score = 0
        for question, correct_answer in self.QUESTIONS_ANSWER_LIST:

            answer = input(f"{i} {question}?")
            i += 1

            if answer == correct_answer:
                print("Correct!")
                score +=1
            else:
                print(f"Oh no, the correct answer is {correct_answer}")

        print(f"\nYou got {score} correct out of {i-1} questions")
        self.total_points += score

if __name__ == "__main__":
    quiz_game = Quiz()
    quiz_game.play()