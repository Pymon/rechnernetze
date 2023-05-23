def crc_calculator (binary_number_string):
    # Polynom zur Berechnung ist g(x) = x^4 + x + 1 oder 10011
    generator_polynom = 0b10011
    binary_number = int(binary_number_string, 2) << 4

    # division
    binary_number_for_calc = int(binary_number_string, 2) << 4
    binary_number_bits = binary_number_for_calc.bit_length()
    generator_polynom_bits = generator_polynom.bit_length()

    while binary_number_bits >= generator_polynom_bits:
        shift = binary_number_bits - generator_polynom_bits
        binary_number_for_calc ^= generator_polynom << shift
        binary_number_bits = binary_number_for_calc.bit_length()    
    
    binary_number += binary_number_for_calc

    return bin(binary_number)[2:]

number = input("Enter your binary number: ")
print(f"your binary number with crc rest is: {crc_calculator(number)}")
