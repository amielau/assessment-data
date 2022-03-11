log_file = open("um-server-01.txt")
#opens file and allows proccess.py to comb through data in file

def sales_reports(log_file):
    #creating sales_reports function with log_file param
    for line in log_file:
        #looping over log_file(see line 1)
        line = line.rstrip()
        # .rstrip removes whitespace from right side of line
        day = line[0:3]
        #assigning line[0:3] to 'day' value
        if day == "Mon":
            #condition
            print(line)
            #what to do if condition is met


sales_reports(log_file)
# invoking the function
