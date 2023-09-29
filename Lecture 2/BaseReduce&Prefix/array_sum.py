array = list(range(1,9))

def sum_elements():
    sum = 0
    for num in array: 
        sum += num
    return sum

def main():
    print("Array: " + str(array))
    print("Sum of elements: "+ str(sum_elements()))

if __name__ == "__main__":
    main()
