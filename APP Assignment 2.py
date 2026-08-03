#Requirements

#---------------------------------------

# Define a decorator for formatting
#function bold_text(func):

# Define the Report class
# Class variable for storing templates
# Constructor to initialize the report with title and content
# Class method to add a template to the class variable
# Class method to retrieve a template from the class variable
# Magic method to call a report instance with a template name
# String representation of the report
# Define a simple template function
# Define a fancy template function with bold formatting
# Main function to generate and display reports
#function main():
# Add templates to the Report class
# Create a report instance
# Generate reports with different templates
# Display the reports
# Run the main function


#if __name__ == &quot;__main__&quot;:
#main()

#---------------------------------------

#Program

#Decorators

#Template for a bold format

def bold_format(func):  #Accepts a function as an argument
    def wrapper(*args,**kwargs): #Accepts any arguments passed to the original func using *args and **kwargs
        content = func(*args,**kwargs) #Calls the original function passed to this decorator
        return f"**{content}**"
    return wrapper  #Returns the altered / "Wrapped" function

#Template for a fancy format

def fancy_text(func):  #NOTE: Declaring this as shout_text would probably be better (output is not fancy)
    def wrapper(*args,**kwargs):
        content = func(*args,**kwargs)
        return content.upper() 
    return wrapper


#Here, *args --> Collects an arbitrary number of positional arguemnts into a tuple
#And, **kwargs --> Collects and arbitrary number of keyword arguments (name-value pairs) into a dictionary

#Class

class Report:
    templates = {}

    def __init__(self,title,content):
        self.title = title
        self.content = content

    @classmethod #We use @classmethod to to ensure that we invoke the Class itself and store the templates in template={}

    def add_template(cls, name, template_func): #cls --> Invokes the class "Report" itself
        cls.templates[name] = template_func 

    @classmethod

    def retrievetemplate(cls,temp_title):
        if temp_title not in cls.templates:
            raise ValueError (f"{temp_title} does not exist!") #Raising an error > printing out an error | raising an error stops the code at the source of the problem.
        return cls.templates[temp_title]


    #To make sure that we can output the desired strings and not memory addresses:

    def __repr__(self):
        return f"Report(title={self.title!r}, content={self.content!r})"
    
    def __str__(self):
        return f"Report(title = {self.title!r})"

    #NOTE: Here , without !r, the output of __str__ will be executed, however, when we use !r , it calls the __repr__ function of the class and gives an output based on the output code of __repr__

    #Using __call__ to call an instance or class object as a function that takes in a template name

    def __call__(self,template_name):
        template_func = self.retrievetemplate(template_name) #Here template_func is a placeholder name, When we do <object/variable name>() --> We call this __call__() function, Hence, here , template_func is just a temporary placeholder for the caller object
        return template_func(self.title, self.content)   #Return the object's inherited title and content from the above line of code


#Assigning Templates  

def simple_template(title,content):
    return f"{title}\n{'-'*len(title)}\n{content}"

@bold_format   #Here, we are telling the compiler to call / use the bold wrapper for this function
def bold_template(title,content):
    return f"{title} : {content}"


@fancy_text #Same logic as above
def fancy_template(title,content):
    return f"{title} -- {content}"


#Main

def main():

    #Adding templates that the user can choose into the "template" dictionary within Report class

    Report.add_template("simple",simple_template)  
    Report.add_template("bold", bold_template)
    Report.add_template("fancy",fancy_template)

    #Create a report and create a Report instance with it

    report=Report("Statistical Results", "Total number of students who got Distinction increased by 32%")


    #Now, we create different (i.e, simple, bold, fancy) versions of this report by calling it with the names of the templates we defined above
    #i.e, for Simple -- "simple" , For Bold -- "bold" , For Fancy -- "fancy"

    simple_report = report("simple") 
    bold_report = report("bold")
    fancy_report = report("fancy")

    #This invokes the __call__ inside Report Class and as per the functioning of __call__ defined above, it takes in a template name and returns 
    #the report in the desired template

    #Display the reports

    print("Reports:\n")

    print(report)
    print()

    print("Displaying Report in:\n")
    print(f"Simple Template:\n\n{simple_report}\n")
    print(f"Bold Template:\n\n{bold_report}\n")
    print(f"Fancy Template:\n\n{fancy_report}\n")

    print("------------------------------------")


if __name__ == "__main__": #If the code we are currently running is THIS code / If the code we are compiling is THIS code, then run the program by invoking main()
    main()