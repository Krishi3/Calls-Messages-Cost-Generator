total = 0
#print statement welcoming the user to this app 
print("Hi there! Welcome to the minutes and messages fee calculator app. Hopefully, you are able to pay your total costs received for the number of minutes and messages you use.")
print("Please type 'enter' to begin.")
enter = str(input())
#variable that stores inputted number of call minutes
nOCM = float(input("Enter the number of minutes used this month:"))

#variable that stores inputted number of text messages
nOM = float(input("Enter the number of messages made this month:"))

#if elif statement for additional minutes cost
if nOCM <= 150:
  addMinTotal = 0
elif nOCM > 150:
  addMinTotal = (nOCM - 150) * 0.85
print("Additional Call Minutes Cost:", addMinTotal)

#if elif statement for additional messages cost
if nOM <= 220:
  addMessTotal = 0
elif nOM > 220:
  addMessTotal = (nOM - 220) * 0.15
print("Additional Text Messages Cost:", addMessTotal)

#total without tax
total = 175 + addMinTotal + addMessTotal + 0.44
print("Total without Tax:", total)

#total with tax
totalTax = total + (total)*0.06
print("Total with Tax:", totalTax)

#print statement - where the user is asked for feedback
print("Thank you for receiving help with your cost calcuations today. Feel free to give us a comment on your opinion regarding our app. Thank you!")

#variable which allows user to input any comments
comment = str(input("Comment: (Not required, but appreciated!)"))
#if you do not want to add a comment, press an enter to continue!

#if else statement to respond to any or no comments provided
if comment:
  print ("Thank you for the feedback/comments! We'll see you next time.")
else:
  print("Have a good day! See you next time.")
