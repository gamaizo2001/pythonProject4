""""
Password
1. Create a program that asks the user to either login or create an account.
2. If the user selects “create an account”.
    a. The program ask the user to enter his name and password.
    b. The program checks the strength of the password
        i. It has a minimum of 8 characters.
        ii. It contains letters between A-z
        iii. It contains an uppercase letter.
        iv. It contains a number.
        v. It contains either @ or $
    c. If the password is strong, the user and password is saved in a file.
    d. The password will be encrypted into the file using any encryption method.
    e. If the password is weak it asks the user to re-enter the password again.
3. If the user selects login
    a. The program asks the user his name and password
        i. The program checks if the user name and the password is the same as the ones
        saved in the file, if so prints “access granted” otherwise “access denied”.
        ii. If the program is checking for the password, it will decrypt it because it would
        be encrypted.
"""
import hashlib



# password hashiang One of the most popular uses of hashes is storing the hash of a password instead of the password
# itself. Of course, the hash has to be a good one or it can be decrypted.
# Bcrypt
def md5_hash(password):
    md5 = hashlib.amd5()
    md5.update(password.encode())
    return md5.hexdigest()


# create a function to check the strength of the password entered
# hello 12123456rrs3333211111111111111111111111111


# a function that checks if the password is less than 8
def is_password_strong(password):
    size = len(password)
    # i. It has a minimum of 8 characters.
    if size < 8:
        print("Password is less than 8 characters")
        return False

    #boolen value
    alpha_found = False
    upper_found = False
    digit_found = False
    symbol_found = False

    # for i=0 => len(password) - 1
    for i in range(size):
        # ii. It contains letters between A-z
        if password[i].isalpha():
            alpha_found = True
        # iii. It contains an uppercase letter.
        if password[i].isupper():
            upper_found = True
        # iv. It contains digit
        if password[i].isdigit():
            digit_found = True
        # v. It contains either @ or $
        if password[i] == '@' or password[i] == '$':
            symbol_found = True

    # check if we have reached the end or the last character, then return
    if not alpha_found:
        print("Password contains no letter")
        return False
    if not upper_found:
        print("password does not contain upper letter")
        return False
    if not digit_found:
        print("Password contains no number")
        return False
    if not symbol_found:
        print("Password contains neither @ nor $")
        return False

    return True


# ask the user to either login or create an account
account = input("""
     Press '1' to create and account and '2' to Login
               1.Create an account
               2.Login
               : """)
file_name = 'userFile.txt'
separator = '#'
# create an account
if account == "1":
    # ask the user to enter his name and password.
    username = input("Enter username: ")
    password = input("Enter Password: ")

    # while password is weak, ask the user to re-enter the password again.
    while True:
        # check if the password is strong
        if is_password_strong(password):
            print("Password is strong")

            #  If the password is strong, the user and password is saved in a file.
            with open(file_name, mode='a') as user_file:
                user_file.write(f'{username.lower()}{separator}{md5_hash(password)}\n')
                break
        else:
            # if the password is weak it asks the user to re-enter the password again.
            password = input("Enter the password again: ")
elif account == "2":
    # the user selects login
    # ask the user to enter his name and password.
    username = input("Enter username: ")
    password = input("Enter Password: ")
    # convert to lowercase
    username = username.lower()
    #         i. The program checks if the user name and the password is the same as the ones
    #         saved in the fi`le, if so prints “access granted” otherwise “access denied”.
    with open(file_name, mode='r') as user_file:
        user_found = False
        for line in user_file:
            if line == f'{username}{separator}{md5_hash(password)}\n':
                print("access granted")
                user_found = True
        if not user_found:
            print("access denied")

    #         ii. If the program is checking for the password, it will decrypt it because it would
    #         be encrypted. A12345678@
