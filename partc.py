import csv,operator

procurement1="C:/Users/bry/Downloads/Project Datasets/government-procurement/government-procurement-via-gebiz.csv"
procurement_dictionary={}
total_procurement_dictionary={}

#this function is to store all values of categories and awarded amount into a dictionary
def procurement_dictionary1():
    count=0
    global procurement_dictionary
    with open(procurement1,"r") as csvfile:
        reader=csv.reader(csvfile)
        #read allow me to call my line and specify the row
        count =0
        for line in reader:
            if count > 0:
                # this is so the first row which are all headers arent used
                procurement_dictionary.setdefault(line[1],[]).append(line[6])
                #creating a dictionary where the values to a key is stored in a list, so for each similar string the value will be appended to that list.
            else:
                count +=1
        return procurement_dictionary

#this function is to fiind total procurement value for each category, not individual values but total
def total_procurement_dictionary1():
    global total_procurement_dictionary
    string=""
    for k,v in procurement_dictionary.iteritems():
        total = 0
        # set total to 0 at this position so for each new category the total will start afresh at 0.
        for number in v:
            #finding total for each "category" and storing it into a new list
            total = round(float(number),2) + total
            #rounding to 2 decimal place
            total_procurement_dictionary[k]=(round(total,2))
    for rows,value in total_procurement_dictionary.iteritems():
        string = string + rows + ": " +str(value)+ "\n"
    return string
    #return total_procurement_dictionary

def sorter():
    choice=raw_input("Would you like to see procurement amount in ascending or descending order?")
    news=""
    total_count=0
    if choice.lower() == "ascending":
        sorted_total_procurement_dictionary= sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=False)
        for item in (sorted_total_procurement_dictionary):
            total_count += 1
            news = news +"#"+str(total_count) + str(item) +"\n"
        return (news)
        #return sorted_total_procurement_dictionary
        print news
    elif choice.lower() =="descending":
        sorted_total_procurement_dictionary= sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=True)
        for item in (sorted_total_procurement_dictionary):
            total_count +=1
            news = news +"#"+str(total_count) + str(item) +"\n"
        return news
        #return sorted_total_procurement_dictionary

    else:
        print "Invalid input please try again, key in ascending/descending only."
        return sorter()
    #print (sorted_total_procurement_dictionary)[112] this is just to check the max value

def largest_5():
    top_5descending={}
    count =0
    string_rep=""
    total_count = 0
    for k,v in sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=True):
        if count < 5:
            top_5descending[k]=v
            count +=1
        else:
            break
    for item in sorted(top_5descending.items(), key=operator.itemgetter(1) ,reverse=True):
        total_count +=1
        string_rep = string_rep + str(total_count) +str(item) + "\n"
    return "These are the top 5 highest awarded amount in descending order: " +"\n" + string_rep

def smallest_5():
    count = 0
    smallest_5ascending={}
    string_rep=""
    total_count =0
    for k,v in sorted(total_procurement_dictionary.items(), key=operator.itemgetter(1) ,reverse=False):
        if count < 5:
            smallest_5ascending[k]=v
            count +=1
        else:
            break
    for item in sorted(smallest_5ascending.items(), key=operator.itemgetter(1) ,reverse=False):
        total_count +=1
        string_rep = string_rep + str(total_count) + str(item) + "\n"
    return "These are the top 5 lowest awarded amount in ascending order: " +"\n" + string_rep
#MAIN-------------------------------------------------------------------------------------------------------------------------------------------------------
print procurement_dictionary1()
print total_procurement_dictionary1()
print sorter()
print largest_5()
print smallest_5()
