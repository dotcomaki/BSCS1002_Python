'''
You are given a list marks that has the marks scored by a class of students in a Mathematics test. Find the median marks and store it in a float variable named median. You can assume that marks is a list of float values.
Procedure to find the median
(1) Sort the marks in ascending order. Do not try to use built-in methods. Look at the lecture 4.5 of week-4 to get a better idea.
(2) If the number of students is odd, then the median is the middle value in the sorted sequence. If the number of students is even, then the median is the arithmetic mean of the two middle values in the sorted sequence.
'''
def solution(marks):
    newMarks = []
    while len(marks) > 0:
        min_mark = marks[0]
        for mark in marks:
            if mark < min_mark:
                min_mark = mark
        newMarks.append(min_mark)
        marks.remove(min_mark)

    n = len(newMarks)
    if n % 2 == 0:
        index1 = n // 2 - 1
        index2 = n // 2
        median = (newMarks[index1] + newMarks[index2]) / 2.0
    else:
        index = n // 2
        median = newMarks[index]
    
    return median
