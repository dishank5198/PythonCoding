def sum_odd(start, stop):
    final_sum = 0
    for x in range(start, stop+1):
        if x % 2 != 0:
            final_sum += x
    return final_sum


if __name__ == "__main__":
    start = int(input("Enter the start number: "))
    end = int(input("Enter the last number: "))
    final_sum = sum_odd(start, end)
    print("The sum of odd number between {start} and {stop} is {final_sum}".format(start=start, stop=end, final_sum=final_sum))