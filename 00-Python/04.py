def parity_bit(binaryAsString):
    countOfOnes = binaryAsString.count("1")
    if (countOfOnes % 2 != 0):
        return "1" + binaryAsString
    else:
        return "0" + binaryAsString
