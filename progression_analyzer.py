from graphics import *
list_outcomes = []        #defining an empty list
progress_count = trailer_count = retriever_count = exclude_count = 0       #initialising values to zero      

user_identification = input("Enter 'staff' if you are a staff member or 'student' if you are a student: ").lower()
while True:
    def validation(text):
        while True:
            value = input(text)          #prompt for the user input
            try:
                value = int(value)
                if value in range(0 , 130 , 20):
                    return value         #loop breaks and goes out of the function , returns the value to the place which called the function

                else:
                    print("Out of range\n")      

            except ValueError:
                print("Integer Required\n")              
 
    if user_identification in ["staff" , "student"]:
        pass_credit = validation("Please enter your credits at pass : ")          #calls to the function and the returning value is stored to the variable
        defer_credit = validation("Please enter your credits at defer : " )
        fail_credit = validation("Please enter your credits at fail : " )

        if pass_credit + defer_credit + fail_credit != 120:
            print("Total incorrect\n")

        elif pass_credit == 120:
            progression_outcome = "Progress"
            progress_count += 1        #incrementing the count by 1
        
        elif pass_credit == 100:
            progression_outcome = "Progress (module trailer)"
            trailer_count += 1
       
        elif fail_credit >= 80:
            progression_outcome = "Exclude"
            exclude_count += 1
        
        else:
            progression_outcome = "Module Retriever"
            retriever_count += 1
        
        if not pass_credit + defer_credit + fail_credit != 120:
            print(progression_outcome)          #print the progression outcome
            list_outcomes.append(f"{progression_outcome} - {pass_credit}, {defer_credit}, {fail_credit}")        #in each round progression outcome and 3 inputs will append to the list as individual strings

        if user_identification == "staff":
            while True:
                result = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ").lower() ; print("\n")
                if result in ["y" , "q"]:
                    break

                else:
                    print("Invalid input")       #for an invalid input the loop continues and prompts for the user's input
            
            if result == "q":
                break             #loop breaks when q is entered

        elif pass_credit + defer_credit + fail_credit != 120:
            continue         #if user is a student with an incorrect total the loop continues

        else:        
            break         #if user is a student with a total mark of 120 the loop breaks

    else:
        break        #if the user_identification is invalid the loop breaks

if user_identification == "staff":
    win = GraphWin("Histogram" , 700 ,600)            #histogram
    total_count = progress_count + trailer_count + retriever_count + exclude_count
    scale = 400 / max(progress_count , trailer_count , retriever_count , exclude_count)        #calculating the scale value

    def graphics(n , value_count , color , progress_outcome):          #passing values are assigned to these variables
        x1 = 40 + (140 * n)                              #left top corner of x-coordinate
        y1 = 500                                             #left top corner of y-coordinate
        x2 = x1 + 120                                     #right bottom corner of x-coordinate
        y2 = 500 - (value_count * scale)        #right bottom corner of y-coordinate

        bar = Rectangle(Point(x1 , y1) , Point(x2 , y2))
        bar.setFill(color)
        bar.draw(win)

        Text(Point(x1 + 60 , y1 + 20) , progress_outcome).draw(win)
        Text(Point(x1 + 60 , y2 - 10) , value_count).draw(win)

    value_count = [progress_count , trailer_count , retriever_count , exclude_count]
    color = ["#98FB98" , "#93C47D" , "#8A9A5B" , "#E6A6C6"]
    progress_outcome = ["Progress" , "Trailer" , "Retriever" , "Excluded"]

    for i in range(len(value_count)):
        graphics(i , value_count[i] , color[i] , progress_outcome[i])          #calling the function "graphics"

    Line(Point(25 , 500) , Point(650 , 500)).draw(win)

    text1 = Text(Point(165 , 550) , (f"{total_count} outcomes in total."))          
    text1.setSize(18)
    text1.draw(win)              #printing the total outcomes
    text2 = Text(Point(165 , 50) , "Histogram Results")
    text2.setSize(18)
    text2.draw(win)
    
    win.getMouse()
    win.close()
    
    text_file = open("Outcomes.txt" , "w")         #opening the text file with write only permission
    print("Part 2: ")
    text_file.write("Part 3: " + "\n")

    for i in list_outcomes:
        print(i)                                                       #printing the values one by one in the list
        text_file.write(i + "\n")                               #writing the values to the text file
                                            
    print("\n")
    text_file = open("Outcomes.txt" , "r")          #opening the same text file with read only permission
    data = text_file.read()                            
    print(data)                                                    #printing the data in the text file          

    text_file.close()               #closing the text file
    

        
