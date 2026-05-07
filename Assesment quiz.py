import time
MIN = 8
MAX = 13
questions = ["Q1","Q2","Q3","Q4"]
number = (MIN,MAX)
print ("Hello and welcome to the quiz")
time.sleep (1)
print ("This quiz is meant for ages "  +str(MIN)+" and "+str(MAX)+": ")
time.sleep (1)
#check the input is a number and not text
player_age = int(input("please enter your age "))
if player_age <= MIN:
  print ("You are too young for this quiz. Please play something else.")
elif player_age >= MAX:
  print ("You are too old for this quiz. I recommend the Cyber Smart Youth Quiz to ages 14 or higher")
while player_age >= MIN and player_age <= MAX:
  time.sleep (1)
  player_name = input ("Please enter your name (No personal information such as e-mails or phone numbers) ")
  print ("Hello, "+str(player_name) )
  time.sleep (1)
  print ("Question time")
  if player_age >= MIN and player_age <= MAX:
   Q1 = input ("You want to join an online gaming site. Which of the following information is okay to post on the site? A:A nickname B:Your real name C:Your e-mail address ").upper ()
   if Q1 == "A":
     print ("Correct!")
     Q2 = input ("If you see somebody with an offensive user name online, what is the correct response? A: Laugh at it B: Do nothing C: Report it ").upper()
  if Q2 == "C":
    print ("Correct!")
Q3 = input ("If someone sends something inappropriate to you, what is the best action to do? A:Ingnore it B:Tell a trusted adult C:Send it to your friends").upper()
if Q3 == "B":
  print ("Correct!")
Q4 = input ("")