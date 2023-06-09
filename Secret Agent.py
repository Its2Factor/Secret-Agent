from time import sleep

user_name = ["jim", "maria", "nick", "alex"]
door_code = "0914"
code_attempts = 3


name = input("Enter Your Username: ").lower()

if name in user_name:
    print("\n- Welcome -")

    while code_attempts > 0:
        entered_code = input("Enter your specialized code to login: ")

        if entered_code == door_code:
            print("\n- Verified Login -\n")
            break
        else:
            code_attempts -= 1
            if code_attempts > 1:
                print("\nIncorrect code: " + str(code_attempts) + " attempts left.\n")

            elif code_attempts == 1:
                print("\nIncorrect code: " + str(code_attempts) + " attempt left.\n")

            else:
                code_attempts == 0
                print("\nSuspicious Login Detected, Self Destruction Commencing", end='')

                for _ in range(8):
                    print(".", end='')
                    sleep(0.7)

                print("\n" * 3)

                print("             (  _---_  )          ")
                print("           (  _.__, _._  )        ")
                print("         (_ ' ( `  )_  .__)       ")
                print("           ( (  ()`)  ) _)        ")
                print("         (__(_(_._) _), __)       ")
                print("          `~~`\ ' . /`~~`         ")
                print("                 ;;               ")
                print("                / \               ")
                print("_____________ / ___ \_____________")


else:
    print("Incorrect Username!")
