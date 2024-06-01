def map_number_to_char(number):
    return chr(number)

def generate_number_sequence():
    return [104, 101, 108, 108, 111, 119, 111, 114, 100]

def manipulate_numbers(numbers, manipulation_logic):
    manipulated_numbers = []
    for number in numbers:
        for logic in manipulation_logic:
            if logic == 'add':
                number += 1
            elif logic == 'subtract':
                number -= 1
        manipulated_numbers.append(number)
    return manipulated_numbers

number_sequence = generate_number_sequence()
manipulation_logic = ['subtract', 'add'] 

manipulated_sequence = manipulate_numbers(number_sequence, manipulation_logic)

character_sequence = [map_number_to_char(number) for number in manipulated_sequence]

final_string = ''.join(character_sequence)

print(final_string)
