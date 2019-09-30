import pandas as pd

data = pd.read_csv('../Data/data.csv')
#print(data['Outlook'].unique())
#print(type(data))
#print(data.dtypes)

x = data.iloc[:, :-1].values
y = data.iloc[:, 2].values

#count_rainy_yes = 0
#count_overcast_yes = 0
#count_sunny_yes = 0


#--------------------label encoding for outlook feature----------------
l1 = list(x[:, 0])

rainy = l1[0]
overcast = l1[2]
sunny = l1[4]

#------------------count of yes for each outlook feature-----------------
for i in range(0, len(l1)):

    if(l1[i] is rainy):
        #print("yes")
        l1[i] = 0

    if(l1[i] is overcast):
    #print("yes")
        l1[i] = 1

    if(l1[i] is sunny):
        #print("yes")
        l1[i] = 2

#print(l1)

#----------------------------count of dependent variable---------------------------------------

l3 = list(y)
#print(len(l3))
yes_total_count = l3.count("Yes")
#print(type(yes_total_count))

no_total_count = l3.count("No")
#print(no_total_count)

#-----------------------------------------------------------------


yes = l3[2]
no = l3[0]



def Outlook(num, variable):

    number = num
    output = variable

    count_rainy_yes = 0
    count_overcast_yes = 0
    count_sunny_yes = 0


    #-------count of yes for each outllok feature---------------------------
    for i in range(0, len(l1)):

        if(l3[i] is yes and l1[i] is 0):
            count_rainy_yes = count_rainy_yes + 1

        if(l3[i] is yes and l1[i] is 1):
            count_overcast_yes = count_overcast_yes + 1

        if(l3[i] is yes and l1[i] is 2):
            count_sunny_yes = count_sunny_yes + 1

    #total_outlook_yes = count1 + count2 + count3
    #print(total_outlook_yes)

    #print(count_rainy_yes)
    #print(count_overcast_yes)
    #print(count_sunny_yes)


    prob_rainy_yes = float(count_rainy_yes) / float(yes_total_count)
    #print(prob_rainy_yes)

    prob_overcast_yes = float(count_overcast_yes) / float(yes_total_count)
    #print(prob_overcast_yes)

    prob_sunny_yes = float(count_sunny_yes) / float(yes_total_count)
    #print(prob_sunny_yes)

#---------------------------------------------------------------

    count_rainy_no = 0
    count_overcast_no = 0
    count_sunny_no = 0


    #--------------------------count of no for each outlook feature---------------------------
    for i in range(0, len(l1)):
        if(l3[i] is no and l1[i] is 0):
            count_rainy_no  = count_rainy_no + 1

        if(l3[i] is no and l1[i] is 1):
            count_overcast_no = count_overcast_no + 1

        if(l3[i] is no and l1[i] is 2):
            count_sunny_no = count_sunny_no + 1
 

    #print("\n")
    #print(count_rainy_no)
    #print(count_overcast_no)
    #print(count_overcast_no)


    #print("\n")
    prob_rainy_no = float(count_rainy_no) / float(no_total_count)
    #print(prob_rainy_no)

    prob_overcast_no = float(count_overcast_no) / float(no_total_count)
    #print(prob_overcast_no)

    prob_sunny_no = float(count_sunny_no) / float(no_total_count)
    #print(prob_sunny_no)


#--------------------------------------------------------------------------total

    total_rainy_prob = (count_rainy_yes + count_rainy_no ) / (yes_total_count + no_total_count)
    #print(total_rainy_prob)

    total_overcast_prob = (count_overcast_yes + count_overcast_no ) / (yes_total_count + no_total_count)
    #print(total_overcast_prob)

    total_sunny_prob = (count_sunny_yes + count_sunny_no ) / (yes_total_count + no_total_count)
    #print(total_sunny_prob)


    if(number is 0 ):
        if(output is yes):
            return ((prob_rainy_yes * (yes_total_count / (yes_total_count + no_total_count))) / total_rainy_prob)

    if(number is 1 ):
        if(output is yes):
            return ((prob_overcast_yes * (yes_total_count / (yes_total_count + no_total_count))) / total_overcast_prob)

    if(number is 2 ):
        if(output is yes):
            return ((prob_sunny_yes * (yes_total_count / (yes_total_count + no_total_count))) / total_sunny_prob)

    if(number is 0 ):
        if(output is no):
            return ((prob_rainy_no * (no_total_count / (yes_total_count + no_total_count))) / total_rainy_prob)

    if(number is 1 ):
        if(output is no):
            return ((prob_overcast_no * (no_total_count / (yes_total_count + no_total_count))) / total_overcast_prob)

    if(number is 2 ):
        if(output is no):
            return ((prob_sunny_no * (no_total_count / (yes_total_count + no_total_count))) / total_sunny_prob)



#label encoding
l2 = list(x[:, 1])
hot = l2[0]
mild = l2[3]
cool = l2[4]

for i in range(0, len(l2)):

    if(l2[i] is hot):
        #print("yes")

        l2[i] = 0
    if(l2[i] is mild):
    #print("yes")
        l2[i] = 1

    if(l2[i] is cool):
        #print("yes")
        l2[i] = 2

#print(l2)


#---------------------------------------temperature-----------------------------------------------
def temperature(num, variable):

    number = num
    output = variable

    count_hot_yes = 0
    count_mild_yes = 0
    count_cool_yes = 0

    for i in range(0, len(l1)):

        if(l3[i] is yes and l2[i] is 0):
            count_hot_yes = count_hot_yes + 1

        if(l3[i] is yes and l2[i] is 1):
            count_mild_yes = count_mild_yes + 1

        if(l3[i] is yes and l2[i] is 2):
            count_cool_yes = count_cool_yes + 1

    prob_hot_yes = float(count_hot_yes) / float(yes_total_count)
    #print(prob_rainy_yes)

    prob_mild_yes = float(count_mild_yes) / float(yes_total_count)
    #print(prob_overcast_yes)

    prob_cool_yes = float(count_cool_yes) / float(yes_total_count)
    #print(prob_sunny_yes)

#---------------------------------------------------------------

    count_hot_no = 0
    count_mild_no = 0
    count_cool_no = 0


    for i in range(0, len(l1)):
        if(l3[i] is no and l2[i] is 0):
            count_hot_no  = count_hot_no + 1

        if(l3[i] is no and l2[i] is 1):
            count_mild_no = count_mild_no + 1

        if(l3[i] is no and l2[i] is 2):
            count_cool_no = count_cool_no + 1
 

    #print("\n")
    #print(count_rainy_no)
    #print(count_overcast_no)
    #print(count_overcast_no)


    #print("\n")
    prob_hot_no = float(count_hot_no) / float(no_total_count)
    #print(prob_rainy_no)

    prob_mild_no = float(count_mild_no) / float(no_total_count)
    #print(prob_overcast_no)

    prob_cool_no = float(count_cool_no) / float(no_total_count)
    #print(prob_sunny_no)


#--------------------------------------------------------------------------total-----------------------------------------------------------------------------------

    total_hot_prob = (count_hot_yes + count_hot_no ) / (yes_total_count + no_total_count)
    #print(total_rainy_prob)

    total_mild_prob = (count_mild_yes + count_mild_no ) / (yes_total_count + no_total_count)
    #print(total_overcast_prob)

    total_cool_prob = (count_cool_yes + count_cool_no ) / (yes_total_count + no_total_count)
    #print(total_sunny_prob)


    if(number is 0 ):
        if(output is yes):
            return ((prob_hot_yes * (yes_total_count / (yes_total_count + no_total_count))) / total_hot_prob)

    if(number is 1 ):
        if(output is yes):
            return ((prob_mild_yes * (yes_total_count / (yes_total_count + no_total_count))) / total_mild_prob)

    if(number is 2 ):
        if(output is yes):
            return ((prob_cool_yes * (yes_total_count / (yes_total_count + no_total_count))) / total_cool_prob)

    if(number is 0 ):
        if(output is no):
            return ((prob_hot_no * (no_total_count / (yes_total_count + no_total_count))) / total_hot_prob)

    if(number is 1 ):
        if(output is no):
            return ((prob_mild_no * (no_total_count / (yes_total_count + no_total_count))) / total_mild_prob)

    if(number is 2 ):
        if(output is no):
            return ((prob_cool_no * (no_total_count / (yes_total_count + no_total_count))) / total_cool_prob)






if __name__ == "__main__" :

    print("\n")
    print("Enter ---> 0 : Rainy, 1 : Overcast,  2 : Sunny")
    feature1 = input()

    probability_outlook_yes = Outlook(int(feature1), yes)
    
    print("\n")
    print("Enter ---> 0 : Hot, 1 : Mild, 2 : Cool")
    feature2 = input()

    probability_temperature_yes = temperature(int(feature2), yes)
    
    yes_prob = probability_outlook_yes * probability_temperature_yes
    #print(yes_prob)

    probability_outlook_no = Outlook(int(feature1), no)

    probability_temperature_no = temperature(int(feature2), no)

    no_prob = probability_outlook_no * probability_temperature_no
    #print(no_prob)

    print("\n")
    total_yes_prob = yes_prob / (yes_prob + no_prob)
    print(total_yes_prob)

    total_no_prob = no_prob / (yes_prob + no_prob)
    print(total_no_prob)

    print("\n")
    if(total_yes_prob > total_no_prob):
        print("Hurraahhh you can play today !!!")
    else:
        print("Better luck next time !!")