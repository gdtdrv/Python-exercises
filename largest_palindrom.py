def get_largest_palindrome(input):
    a=str(input)
    num_digits=len(a)
    middle_digit= int(is_palindrom(a)[1])
    digits_list = is_palindrom(a)[2]
    middle_digit_index = is_palindrom(a)[3]
    if is_palindrom(a)[0]:
        if num_digits%2==0:
            digits_list[middle_digit_index] = str(middle_digit -1)
            digits_list[middle_digit_index+1] = str(middle_digit - 1)
            digits_list=digits_list[1:]
            new_palindrom =''.join(digits_list)
        else:
            digits_list[middle_digit_index+1] = str(middle_digit - 1)
            digits_list = digits_list[1:]
            new_palindrom = ''.join(digits_list)
    else:
        for digit in range(1,middle_digit_index+1):
            digits_list[-digit] = digits_list[digit]
        digits_list=digits_list[1:]
        new_palindrom =''.join(digits_list)
    return int(new_palindrom)

def is_palindrom(n):
    num_digits = len(n)
    i = 1
    digits_list = [None] * (num_digits + 1)
    for ch in n:
        digits_list[i] = ch
        i = i + 1
    j = 0
    middle_digit_index = int(num_digits // 2)
    symmetry= 0
    for j in range(middle_digit_index):
        if digits_list[j] == digits_list[-j]:
            symmetry = symmetry + 1
        else:
            return False, digits_list[middle_digit_index+1],digits_list,middle_digit_index
    if symmetry ==middle_digit_index:
        return True, digits_list[middle_digit_index+1],digits_list,middle_digit_index

if __name__ == "__main__":
    print(get_largest_palindrome('''125569'''))