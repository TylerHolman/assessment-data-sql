log_file = open("um-server-01.txt") #opens the file in the string which is being assigned to the var log_file

#
def sales_reports(log_file): #defining a function sales_reports with a parameter of log_file
    for line in log_file: #is a for loop that is going to run in the log_file which was assigned in line 1
        line = line.rstrip() #gets rid of unnecessary white space
        day = line[0:3]  #checks the first 3 letters of the line
        if day == 'Mon': #checking to make sure the day is Monday 
            print(line) #telling it to print the line of code if the day is Mon


sales_reports(log_file) #invoking the function we defined on line 4
