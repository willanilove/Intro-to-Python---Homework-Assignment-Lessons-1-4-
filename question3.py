# Build a grade calculator that uses loops and functions to process student scores.

def calculate_average(scores):
    total = 0

    for score in scores:
        total += score 
    average = total / len(scores) 
    return average

def get_letter_grade(average):

# Returns letter grade: A (90+), B (80-89), C (70-79), D (60-69), F (below 60)

    if average >= 90:
        return "A"
    elif average >= 80:
         return "B"
    elif average >= 70:
         return "C"
    elif average >= 60:
         return "D"
    else:
         return "F"
    
def main():
    scores = []
    
# Use a while loop to: Ask how many test scores to enter

    how_many = int(input("How many test scores do you want to enter? "))
    
    count = 1

    while count <= how_many:
        score = float(input(f"Enter score {count}: "))
        scores.append(score)
        count += 1

    average = calculate_average(scores)
    letter = get_letter_grade(average)

    print("\n=== GRADE REPORT ===")
    print("Test Scores:", scores)
    print("Average Score:", round(average, 2))
    print("Letter Grade:", letter)

main()