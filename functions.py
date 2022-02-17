# Functions

def age():
    print("THIS IS THE AGE FUNCTION")
    age = int(input("Enter your age"))
    return age

def main():
    print("THIS IS MAIN FUNCTION")
    userAge = age()
    print("THIS IS NOW MAIN FUNCTION")
    print(userAge)
main()
#this last main() make the function close we need to use functionname() like this to close a function

