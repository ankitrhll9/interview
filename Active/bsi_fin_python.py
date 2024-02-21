sample_string = "I love my country India"

counter = len(sample_string) - 1
final_string = ""
last_space = counter + 1

for i in range(len(sample_string)):    
    if sample_string[counter] == " ":
        for j in range(counter, last_space):
            final_string += sample_string[j]
        last_space = counter
    if counter == 0:
        final_string += " " + sample_string[counter]
        break
    counter -= 1

print(final_string)

'''
Code Breakdown:

1. Initialization:
sample_string = "I love my country India": Assigns a string to be processed.
counter = len(sample_string) - 1: Initializes a counter to start at the end of the string.
final_string = "": Creates an empty string to store the reversed words.
last_space = counter + 1: Sets a variable to track the last encountered space.

2. Main Loop:
for i in range(len(sample_string)): Iterates through each character of the string.

3. Word Reversal:
if sample_string[counter] == " ": Checks if the current character is a space.
for j in range(counter, last_space): If a space is found, it iterates through the characters of the current word (from the space to the last space) and appends them in reverse order to final_string.
last_space = counter: Updates last_space to mark the new boundary for the next word.

4. Handling the First Word:
if counter == 0: If the beginning of the string is reached, adds the first word (and an initial space) to final_string and breaks the loop.

5. Output:
print(final_string): Prints the final reversed string.
Overall, the code reverses the order of words in a string without using built-in string methods like split or reverse. 
It does this by iterating through the string in reverse order, extracting words based on spaces, and building the reversed string character by character.

The output of this code is:
India country my love I
'''