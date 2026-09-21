import re

def find_emails(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

if __name__ == "__main__":
    input_text = input("Enter text: ")
    emails = find_emails(input_text)
    print(emails)



#Explanations
'''
[a-zA-Z0-9._%+-]+ — matches the local part (before @), allowing letters, digits, and common symbols like ., _, %, +, -
@ — matches the literal @ symbol
[a-zA-Z0-9.-]+ — matches the domain name, allowing letters, digits, dots, and hyphens
(slash).[a-zA-Z]{2,} — matches the dot followed by the top-level domain (e.g., .com, .org), requiring at least 2 letters
'''