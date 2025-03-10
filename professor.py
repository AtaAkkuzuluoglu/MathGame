import random 
def main():
    MathProb()
    
def get_level():
    while True:
        try:
            MyLevel = int(input(""))
            if MyLevel in {1,2,3}:
                return MyLevel  
        except ValueError:
            continue

def generate_integer(level):
    for i in range(10):
        FirstNum = random.randint(10**(level-1)-1,10**level-1)
        SecondNum = random.randint(10**(level-1)-1,10**level-1)
        return FirstNum, SecondNum   

def MathProb():
    Score = 0
    Level = get_level()
    for i in range(10):
        FirstNum, SecondNum = generate_integer(Level)
        try:
            Answer = input(f"{FirstNum} + {SecondNum} = ")
            if int(Answer) == FirstNum + SecondNum:
                Score = Score +1
            else:
                for b in range(2):
                    print("EEE")
                    Answer = input(f"{FirstNum} + {SecondNum} = ") 
                    if b == 1:
                        print(f"{FirstNum} + {SecondNum} = {FirstNum + SecondNum} ")
        except ValueError:
            for c in range(2):
                    print("EEE")
                    Answer = input(f"{FirstNum} + {SecondNum} = ") 
                    if c == 1:
                        print(f"{FirstNum} + {SecondNum} = {FirstNum + SecondNum} ")
    print(Score)
if __name__ == "__main__":
    main()    