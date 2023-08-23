####
# Group Number: Group 88 DAR
# STUDENT NAME: Abisekh Subedi, Ashal Bhattarai, Dawood Sunuwar, Samidha upadhyay
# STUDENT NUMBER: s371687
####


# function to run question 4
def program_4():

    # process text from .txt file and return a list of numbers and alphabetical characters
    def process_text(text):
        numbers = []
        chars = []

        # iterate through each character in text
        for char in text:
            # append to numbers list if digit
            if char.isdigit():
                numbers.append(int(char))
            # append to chars if alphabet character
            elif char.isalpha():
                chars.append(char)

        # return tuple of numbers and chars
        return numbers, chars

    # checks whether a string is a palindrome. CASE: string must be length greater than 4
    def is_palindrome(str):
        return str == str[::-1] and len(str) > 4

    # function to check if the number is prime or not
    def is_prime(num):
     if num > 1:
        # check whether the number is divisible by any other number than itself
        for i in range(2, num):
            if num % i == 0:
                # num is not prime number
                return False
        # num is prime number
        return True

    # question no 4 main code block
    try:
        with open("input_text.txt", "r") as file:
            # read the contenet of the file
            file_content = file.read()

            # destructing the tuple returned by process_text function
            numbers, chars = process_text(file_content)

            # function to get all the sum which is a prime number
            def get_prime_numbers(arr, numbers):
                num_sum = 0
                for num in numbers:
                    num_sum += num
                    # check if num_sum is prime
                    if is_prime(num_sum):
                        arr.append(str(num_sum))
                return arr

            # function to get the palindromes from the chars list
            def get_palindromes(arr, chars):
                alphabet_series = ""

                # loop through each character in chars list
                for char in chars:
                    alphabet_series += char

                # nested loop to go through alphabet_series to find palindromes
                for i in range(len(alphabet_series)):
                    # loop through alphabet_series starting from i + 1
                    for j in range(i + 1, len(alphabet_series) + 1):
                        # check if the substring is palindrome
                        if is_palindrome(alphabet_series[i:j]):
                            # append to alphabet_palindromes list
                            arr.append(alphabet_series[i:j])

                return arr

            # list of prime numbers
            prime_numbers = get_prime_numbers([], numbers)
            # list of palindromes
            palindromes = get_palindromes([], chars)


            if bool(prime_numbers):
                print(f"\nList of all the sums which are prime number:\n{', '.join(prime_numbers)}.")
            else:
                print("There are no prime numbers in the list")

            if bool(palindromes):
                print(f"\nList of palindrome words (words > 4 characters): \n{', '.join(palindromes)}.")
            else:
                print("There are no palindrome in the list")

   # handle file not found error
    except FileNotFoundError as e:
        print(e, '\n')
        print("File not found. Please check the file name and try again")

def main():
    userchoice = 1
    try:
        while userchoice != 0:
            userchoice = input("\nInput between 1 to 4 to run the program. Input 0 to terminate: \n")

            if int(userchoice) == 1:
                # Ques. No 1:
                print("Solution 1 \n")

            elif int(userchoice) == 2:
                # Ques. No 2:
                print("Solution 2 \n")

            elif int(userchoice) == 3:
                # Ques. No 3:
                print("Solution 3 \n")

            elif int(userchoice) == 4:
                # Ques. No 4: Program that add each individual numbers in the text and check the palindrome in the characters.
                program_4()

            else:
                print("Program exit!")
                break
    except ValueError:
        print("\nPlease enter a valid input.")
        main()
if __name__ == "__main__":
    main()
