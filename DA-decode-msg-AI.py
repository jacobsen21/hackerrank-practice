'''
I need a function called decode(message_file) that can read in an encoded message from a .txt file and return the decoded version as a string.

Here's an example of what the message_file .txt file will look like:

3 love
6 computers
2 dogs
4 cats
1 I
5 you

As you can see, each word is associated with a number. Imagine you ordered all those numbers from smallest to biggest and arranged them into a pyramid. Each line of the pyramid includes one more number than the line before it:

1
2 3
4 5 6

The numbers at the end of each line (1, 3 and 6) correspond to the words that are part of the message. You should ignore all the other words. So for the example input file above, the message words are:

1: I
3: love
6: computers

and your function should return the string "I love computers"
'''

# data filename and path
message_file = "message_file.txt"

# decode function
def decode(message_file):
    
    # read in the file contents
    try:
        with open(message_file, 'r') as file:
            lines = file.readlines()

    except FileNotFoundError:
        raise FileNotFoundError(message_file)

    # Check if file has the expected format
    if len(lines) == 0:
        raise ValueError("The file is empty.")

    if not all('\n' in line for line in lines):
        raise ValueError("The file does not have the expected format. Each line should contain a number and a word separated by a newline.")

    # Split the lines into numbers and words
    data = [line.strip().split() for line in lines]
 
    # Sort the data based on the first column of numbers
    sorted_data = sorted(data, key=lambda x: int(x[0]))
 
    
    # outer loop to handle number of rows
    # init variables

    n=len(sorted_data)
    start_row = 0
    result_msg = ""

    # outer loop for rows
    for i in range(n):
        
        # inner loop for columns
        for j in range(i+1):
            
            # take last word from each row to build message
            word = sorted_data[start_row][1]
            print(word + " ", end="")  #debug remove

            # increment next row starting position
            start_row += 1
      
        # row line end
        print("\r")

        # concat decoded message
        result_msg += word + " "

        # prevent exceeding the index
        if(start_row >= n):
                break
             
    return result_msg

# call the function
result = decode(message_file)
print("decoded message: ", result)
