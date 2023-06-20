# Nested Lists

# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any
# student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format
# The first line contains an integer, N, the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains
# their grade.

# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.

# Output Format
# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names
# alphabetically and print each one on a new line.

# Obhective, solve using lists, nested lists, etc.


if __name__ == '__main__':
    name_and_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_and_score.append([name,score])

    scores = [x[1] for x in name_and_score]
    min_li = sorted(set(scores))
    students = sorted([y[0] for y in name_and_score if y[1]==min_li[1]])
    [print(k) for k in students]


    


    # for entry in name_and_score:

