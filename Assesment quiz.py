import time
MIN = 8
MAX = 13
guess = 0
guesses = 0
score = 0
questions = ["Q1","Q2","Q3","Q4"]
number = (MIN,MAX)
print ("Hello and welcome to the quiz")
time.sleep (1)
print ("This quiz is meant for ages "  +str(MIN)+" to "+str(MAX)+": ")
time.sleep (1)
#check the input is a number and not text
player_age = int(input("please enter your age "))
if player_age <= MIN:
  print ("You are too young for this quiz. Please play something else.")
elif player_age >= MAX:
  print ("You are too old for this quiz. I recommend the Cyber Smart Youth Quiz to ages 14 or higher")
else:
  while player_age >= MIN and player_age <= MAX:
    time.sleep (1)
    player_name = input ("Please enter your name (No personal information such as e-mails or phone numbers) ")
    print ("Hello, "+str(player_name) )
    time.sleep (1)
    print ("Question time")
    time.sleep (1)
    if player_age >= MIN and player_age <= MAX:
     Q1 = input ("You want to join an online gaming site. Which of the following information is okay to post on the site? A:A nickname B:Your real name C:Your e-mail address ").upper ()
    if Q1 == "A":
      print ("Correct!")
      score += 1
      time.sleep (1)
      Q2 = input ("If you see somebody with an offensive user name online, what is the correct response? A: Laugh at it B: Do nothing C: Report it ").upper()
      if Q2 == "C":
       print ("Correct!")
       score += 1
       time.sleep (1)
    Q3 = input ("If someone sends something inappropriate to you, what is the best action to do? A:Ingnore it B:Tell a trusted adult C:Send it to your friends ").upper()
    if Q3 == "B":
      print ("Correct!")
      score += 1
    time.sleep (1)
    Q4 = input ("You lose a game to one of your friends, what is the best way to respond? A:Yell at them B:Rage quit C:Say something positive ").upper()
    if Q4 == "C":
     print ("Correct!")
     score += 1
     RES = input("Would you like to see your results? Y/N ").upper()
    if RES == "N":
       print ("Ok")
    elif RES == "Y":
         print("Your score is "+str(score))
  
  