#!/usr/bin/python3
#script ask user for the total house cost and based upon the credit score, calculates the down payment 


price=input("Enter the cost of the house:\n")
credit_score=input("Enter the credit score:\n")

if(len(price)<=0) or (len(credit_score)<=0):
    if(len(price)>0) and (len(credit_score)<=0):
        print("Credit score field is empty")
    elif(len(price)<=0) and (len(credit_score)>0):
        print("Price field is empty")
    else:
        print("Issues with the user input")

elif(len(price)>0) and (len(credit_score)>0):
    if (int(credit_score)>=750):
        print("*"*30)
        down_payment=int(price)*10/100
        print("Cost of House is --> " + str(price))
        print("CRedit score is --> " + str(credit_score))
        print("Down Payment -->" + str(down_payment))
        print("*"*30)
    elif (int(credit_score)<750) and (int(credit_score)>=650):
        print("*"*30)
        down_payment=int(price)*20/100
        print("Cost of House is --> " + str(price))
        print("CRedit score is --> " + str(credit_score))
        print("Down Payment -->" + str(down_payment))
        print("*"*30)
    else:
        print("*"*30)
        print("Bad credit score")                                                   
        print("Re-apply in next 6 months")                                          
        print("*"*30) 
