import random

# Generates the numbers that the operations will work on (the "addends," "factors," etc.)
def generateNumbers(n:int = 4, lowerBound:int = -20, upperBound:int = 20) -> list[int]:
    numbers = []
    for i in range(n):
        num = random.randrange(lowerBound, upperBound + 1, 1)
        numbers.append(num)
    return numbers

# Operations
def generateOperations(n:int = 3, level = 1):
    opsPerLevel = {
        1: 2, #     + -
        2: 4, #     + - x /
        3: 6  #     + - x / % * 
    }
    operations = []
    for i in range(n):
        num = random.randrange(1, opsPerLevel[level] + 1, 1)
        operations.append(num)
    return operations

def performCalculations(numbers: list[int], operations: list[int]):
    assert(len(numbers) == len(operations) + 1) # or greater than or equal to

    if len(numbers) == 1:
        return numbers
    
    result = numbers[0]

    for i in range(1, len(numbers)):
        if operations[i-1] == 1:
            result += numbers[i]
        elif operations[i-1] == 2:
            result -= numbers[i]
        elif operations[i-1] == 3:
            result *= numbers[i]
        elif operations[i-1] == 4:
            result = result // numbers[i]
        elif operations[i-1] == 5:
            result %= numbers[i]
        else:
            result = result**numbers[i]
    
    return result

def gameOver(score = 0):
    print("Congratulations! Your score is: ", score)


def main():
    score = 0

    userInput = ""

    while userInput != "Exit":
        print("Select mode")

##### Testing Code #####

nums = [3, 4, 6, 2]
nums2 = [4, 6, 3, 1]

operations = [1, 2, 3]
operations2 = [6, 5, 4]

print(performCalculations(nums, operations))
print(performCalculations(nums2, operations))
print(performCalculations(nums, operations2))
print(performCalculations(nums2, operations2))

print((4 + 6 - 2)*3)

'''
3 to the 4 is 81
81 %= 6 is 3
3 /= 2 = 1

4 to the 6 is 4096?
'''
print(4096%3)