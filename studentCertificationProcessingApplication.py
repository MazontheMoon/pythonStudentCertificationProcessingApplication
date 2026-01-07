# SD-TA-010-B - Assignment
# Author: Mary Ronan
# Student Certification Processing Application

# Global variables
moduleList = ["System Design", "Web Design", "Programming", "Databases", "Cyber Security"]

# Display greeting
def displayGreeting():
    print("======================================================================")
    print("    Welcome to GTI's Student Certification Processing Application")
    print("======================================================================")

# Validate string input
def getValidStringInput(message):
    while(True):
        try:
            value = input(message)
            if value == "" :
                raise Exception
            else:
                return value
        except:
            print("Invalid Entry, please try again. \n")

# Validate int input
def getValidIntInput(message):
    while(True):
        try:
            value = int((input(message)))
            if value < 0 :
                raise Exception
            else:
                return value
        except:
            print("Invalid Entry, please try again. \n")

# Calculate grade

# Calculate average result

# Calculate result

# Display results

# Generate certificate

# Write to log file

# Write to CSV

# Exit prompt
def exitPrompt():
    validEntries = ["Y", "y", "N", "n"]
    while(True):
        try:
            value = input("Enter results for another candidate [Y/N] \n")
            if value == "" or value not in validEntries:
                raise Exception
            else:
                if value == "Y" or value == "y":
                    return True
                else:
                    return False
        except:
            print("Invalid Entry, please enter Y for Yes or N for No\n")



# Display exit message
def displayExitMessage():
    print("======================================================================")
    print("Thank you for using GTI's Student Certification Processing Application")
    print("======================================================================")

def main():

    # Local variables
    keepGoing = True
    studentname = ""
    certificateName = ""
    resultList = [0] * len(moduleList)

    # Display greeting
    displayGreeting()

    # Get Student Information
    while(keepGoing == True):
        studentName = getValidStringInput("Enter candidate's name: ")
        certificateName = getValidStringInput("Enter name of certificate: ")

        # Get results per module
        for i in range(0, len(moduleList)):
            resultList[i] = getValidIntInput("Enter result for module '" + moduleList[i] + "': ")

        # Display grade
        print(resultList)

        #Prompt to exit
        keepGoing = exitPrompt()
        
    displayExitMessage()
    
main()

