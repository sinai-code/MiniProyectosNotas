def analyze_grades(numbers):
    approved = [ ]
    for number in numbers:
        if number >= 5:
            approved.append(number)

    total = 0
    for number in numbers:
        total+= number

    average = total / len(numbers)

    return len(approved), approved, average

grades = [4, 7, 5, 9, 3, 8, 10, 6]

approved_count, approved, average = analyze_grades(grades)

print(approved_count, approved, average)
