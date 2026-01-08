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

# Calculate outcome from grade
def getOutcome(grade):
    if grade == "A" or grade == "B" or grade == "C":
        return "Pass"
    else:
        return "Fail"
    
# Display Grade
def displayGrade(list):
    grade = ""
    
    if "Fail" in list[4]:
        grade = "Fail"
    else :
        grade = "Pass"
    print("\n{0} has achieved a grade of {1} for the certificate: {2}".format(list[0], grade.upper(), list[1]))

    
# Generate certificate
def generateCertificate(list):
    name = list[0]
    cert = list[1]
    results = list[2]
    grades = list[3]
    outcome = list[4]
    average = int(sum(results) / len(results))
    overallResult = "FAIL" if "Fail" in outcome else "PASS"
    filepath = "C:\\temp\\" + name + " " + cert + " Certificate.txt"

    try:
        with open(filepath, "w") as file:
            file.write("---------------------- CERTIFICATION RESULT SHEET  ----------------------\n")
            file.write("\nCandidate: \t" + name)
            file.write("\nCertification: \t" + cert)
            file.write("\n\nModule\t\t\tResult\tGrade\tOutcome\n")
            file.write("=================\t======\t=====\t=======\n")
            for i in range(0, len(moduleList)):
                file.write(moduleList[i] + "\t\t  " + str(results[i]) + "\t  " + grades[i] + "\t " + outcome[i] +"\n")
            file.write("\nAverage Result: " + str(average))
            if overallResult == "PASS":
                file.write("\nOverall Result: PASS")
            else:
                file.write("\nOverall Result: FAIL*")
                file.write("\n----------------------------------------------------------------------\n")
                file.write("* Candidates must pass all modules to obtain a certificate.\nThe pass rate for each module is 50%")
    except:
        print("File IO error")
    

# Write to log file

# Write to CSV

# Exit prompt
def exitPrompt():
    validEntries = ["Y", "y", "N", "n"]
    while(True):
        try:
            value = input("Enter results for another candidate [Y/N]")
            if value.strip() == "" or value not in validEntries:
                raise Exception
            else:
                if value.upper() == "Y":
                    return True
                else:
                    return False
        except:
            print("Invalid Entry, please enter Y for Yes or N for No")



# Display exit message
def displayExitMessage():
    print("======================================================================")
    print("Thank you for using GTI's Student Certification Processing Application")
    print("======================================================================")

def main():

    # Local variables
    keepGoing = True
    studentName = ""
    certificateName = ""
    resultList = [0] * len(moduleList)
    gradeList = [0] * len(moduleList)
    outcomeList = [0] * len(moduleList)

    # Display greeting
    displayGreeting()

    # Get Student Information
    while(keepGoing == True):
        certificateList = []
        studentName = getValidStringInput("\nEnter candidate's name: ")
        certificateName = getValidStringInput("Enter name of certificate: ")

        # Get results per module
        for i in range(0, len(moduleList)):
            resultList[i] = getValidIntInput("Enter result for module '" + moduleList[i] + "': ")
            gradeList[i] = getGrade(resultList[i])
            outcomeList[i] = getOutcome(gradeList[i])

        certificateList.append(studentName)
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
        
    displayExitMessage()
    
main()

