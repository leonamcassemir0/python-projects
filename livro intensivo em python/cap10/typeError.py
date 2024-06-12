while True:
    try:
        first_number = input("first number: ")
        second_number = input("\n second number: ")
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('Not add texts!')
    else:
        print(f'\n {answer}')
