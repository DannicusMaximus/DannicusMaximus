print("MathHomework.py")
#Ask the user to enter a math problem
problem = input("Enter a math problem, or 'q' to quit: ")
#Keep going until the user enters 'q' to quit
while (problem != "q"):
    # Show the proble, and the answer using eval()
    print("The answer to ", problem, "is:", eval(problem) )
    # Ask for  another problem
    problem = input("Enter a math problem, or 'q' to quit: ")
