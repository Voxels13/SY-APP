input_file = 'input.txt'
output_file = 'output.txt'

try:
    with open(input_file,'r') as file:
        lines = file.readlines()


        print(f"Total number of lines in {input_file}: {len(lines)}\n")

        extract_two = lines[:2]
        print("First two lines: ")
        for line in extract_two:
            print(line,end="")


        with open(output_file,'w') as destfile:
            for line in extract_two:
                destfile.writelines(line)

        #confirmation

        print(f"The first two lines of {input_file} has been written to {output_file} successfully!")

except FileNotFoundError:
    print(f"File <{input_file}> was not found. Could not open said file in read mode!")