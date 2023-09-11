def get_sum_name(name_string):
    sum_name = 0
    for s in name_string:
        s_code = ord(s)
        if s_code < ord('A'): # symbol's code must be greater or equal than 41h
            return 'Invalid Name'
        if s_code >= 90: # condition if char code > char code for 'Z' symbol
            s_code = s_code - 32 # must be subtracted 20h
        sum_name += s_code
    return sum_name


def get_sum_serial(name, xor_operand_name, xor_operand_serial):
    sum_name = get_sum_name(name)
    if sum_name == 'Invalid Name':
        return sum_name
    condition_number = sum_name ^ xor_operand_name
    sum_serial = condition_number ^ xor_operand_serial
    return sum_serial

def find_serial(sum_serial):
    result = 0
    result_string = ''
    counter = 2
    sum_serial_string = str(sum_serial)
    while result != sum_serial:
        current_sum_serial = sum_serial_string[:counter]
        result = result * 10 # imul 0Ah
        if counter == 2:
            new_int = int(current_sum_serial) + 48 # must be subtracted by 30h
        else:
            # find symbol_code from formula edi = (symbol_code - 48) + edi_prev*10
            new_int = int(current_sum_serial) - int(previous_sum)*10 + 48
        new_char = chr(new_int)
        result = (new_int - 48) + result
        result_string = result_string + new_char
        counter += 1
        previous_sum = current_sum_serial
    return result_string


def main():
    name = input('-> ')
    sum_serial = get_sum_serial(name, 0x5678, 0x1234)
    if sum_serial == 'Invalid Name':
        print(sum_serial + ": symbol's code must be greater or equal than 41h")
        return
    serial = find_serial(sum_serial)
    print(serial)


main()
