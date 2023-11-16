# Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
def convert(dec_number: int = None, bin_number: str = None):
    def convert_to_bin(dec_number):
        bin_result = ''
        if dec_number % 2:
            bin_result += '1'
        elif not dec_number % 2:
            bin_result += '0'
        if dec_number == 1:
            return bin_result
        dec_number //= 2
        return bin_convert(dec_number) + bin_result
    def convert_to_dec(bin_number):
        number = 0
        for i in range(1, len(bin_number) + 1):
            if bin_number[-i] == '1':
                number += 2 ** (i - 1)
        return number
    if dec_number == None:
        return convert_to_bin(bin_number)
    elif bin_number == None:
        return convert_to_dec(dec_number)
    else:
        return convert_to_bin(dec_number), convert_to_dec(bin_number)
