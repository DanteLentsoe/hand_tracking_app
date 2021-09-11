# take user number
while True:
    try:
        number_input = input('Enter your number: ')
        char_num = "+"

        # check is number starts with +
        if (number_input.find(char_num) != -1 and number_input[0] == char_num):
            validated_num = number_input
            break
        else:
            raise ValueError
            break
    except ValueError:
        print('Please enter a + sign followed by a number!')


number = validated_num
