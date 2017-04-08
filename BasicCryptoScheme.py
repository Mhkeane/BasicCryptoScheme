import math


alphabet = ["A","B","C","D","E","F","G",'H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def convert_to_numbers(input_string):
	output_number = []
	for i in range(len(input_string)):
		numeric_representation = str(alphabet.index(input_string[i]))
		if len(numeric_representation) == 1:
			numeric_representation = "0" + numeric_representation
		output_number.append(numeric_representation)
	return "".join(output_number)
	
def convert_to_letters(input_number):
	output_letters = []
	for i in range(math.ceil(len(input_number)/2)):
		letter = alphabet[int(input_number[2*i:2*i+2])]
		output_letters.append(letter)
	return "".join(output_letters)

def encode(input_string):
	input_number = convert_to_numbers(input_string)
	encoded_number = []
	for i in range(math.ceil(len(input_number)/2)):
		#print(input_number[2*i:2*i+2])
		current_number = int(input_number[2*i:2*i+2])
		#print(current_number)
		output_number = str((15*current_number + 13)%26)
		#print(output_number)
		if len(output_number) == 1:
			output_number = "0" + output_number
		encoded_number.append(output_number)
	output_letters = convert_to_letters("".join(encoded_number))
	return output_letters
	
def decode(input_string):
	input_number = convert_to_numbers(input_string)
	decoded_number = []
	for i in range(math.ceil(len(input_number)/2)):
		current_number = int(input_number[2*i:2*i+2])
		output_number = str(((7*(current_number + 13))%26))
		if len(output_number) == 1:
			output_number = "0" + output_number
		decoded_number.append(output_number)
	output_letters = convert_to_letters("".join(decoded_number))
	return output_letters
	
#print(encode("ABA"))
print(encode("FRIGATEISINTHEGULF"))
print(decode("XBCLNIDAVONXXBAH"))