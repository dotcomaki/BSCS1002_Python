'''
A sequence of integers of even length is said to be left-heavy if the sum of the terms in the left-half of the sequence is greater than the sum of the terms in the right half.
It is termed right-heavy if the sum of the second half is greater than the first half. It is said to be balanced if both the sums are equal.
Accept a sequence of comma-separated integers as input. Determine if the sequence is left-heavy, right-heavy or balanced and print this as the output.
'''

sequence = input().split(',')
length = len(sequence)
mid = length // 2
left = 0
right = 0
for i in range(mid):
    left += int(sequence[i])
    right += int(sequence[length - i - 1])
if left == right:
    print("balanced")
elif left > right:
    print("left-heavy")
elif left < right:
    print("right-heavy")
