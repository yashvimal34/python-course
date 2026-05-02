questions = [
    [ "Who is Virat Kohli:", "Actor", "Astronaut", "Cricketer", "Footballer", 3 ],
    [ "Which is largest mammel on Earth:", "Elephant", "Giraffe", "Shark", "Blue Whale", 4 ],
    [ "Which Ocean is largest:", "Pacific Ocean", "Indian Ocean", "Atlantic Ocean", "Artic Ocean", 1 ],
    [ "What is the smallest City in world:", "San Francisco", "Vatican City", "Monaco", "Italy", 2],
]

Prizes = [ 100000, 200000, 400000, 1000000 ]

i = 0
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Check wheather the answer is correct or not
    a = int(input("Enter Your answer: "))
    if(question[5] == a):
        print("Correct Answer")
    else:
        print("Incorrect Answer")
        print("Better Luck Next Time!")
        break
    print(f"You Won {Prizes[i]}")
    i += 1