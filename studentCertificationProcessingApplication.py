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
def getGrade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 40:
        return "D"
    else:
        return "E"

# Calculate outcome from result
def getOutcome(grade):
    if grade == "A" or grade == "B" or grade == "C":
        return "Pass"
    else:
        return "Fail"

# Display Grade
def displayGrade(list):
    if list[][]
    
# Generate certificate
def generateCertificate(list):
    print("======================================================================")
    
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
    gradeList = [0] * len(moduleList)
    outcomeList = [0] * len(moduleList)
    certificateList = []

    # Display greeting
    displayGreeting()

    # Get Student Information
    while(keepGoing == True):
        studentName = getValidStringInput("Enter candidate's name: ")
        certificateName = getValidStringInput("Enter name of certificate: ")

        # Get results per module
        for i in range(0, len(moduleList)):
            resultList[i] = getValidIntInput("Enter result for module '" + moduleList[i] + "': ")
            gradeList[i] = getGrade(resultList[i])
            outcomeList[i] = getOutcome(gradeList[i])

        certificateList.append(studentname)
        certificateList.append(certificateName)
        certificateList.append(resultList)
        certificateList.append(gradeList)
        certificateList.append(outcomeList)

        # Display grade
        displayGrade(certificateList)

        # Generate certificate
        generateCertificate(certificateList)

        # Add to log

        # Add to CSV

        # Prompt to exit
        keepGoing = exitPrompt()

        # Clear lists
        resultList.clear()
        gradeList.clear()
        outcomeList.clear()
        certificateList.clear()
        
    displayExitMessage()
    
main()

