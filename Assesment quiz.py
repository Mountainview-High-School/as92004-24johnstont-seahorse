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
    time.sleep (1) #Time is there so the player of the quiz gets time to read things before each question
    player_name = input ("Please enter your name (No personal information such as e-mails or phone numbers) ")
    print ("Hello, "+str(player_name) )
    time.sleep (1)
    print ("Question time")
    time.sleep (1)

    while guesses < 3: #While loop makes it so the code repeats for 3 guesses when the question is guessed wrong, then it moves on to the next one
      guesses += (1)
      Q1 = input ("You want to join an online gaming site. Which of the following information is okay to post on the site? A:A nickname B:Your real name C:Your e-mail address ").upper ()
      if Q1 == "A":
        print ("Correct!")
        score += 1
        time.sleep (1)
        break

    guesses = 0 #resets the amount of guesses so the code can continue
    while guesses < 3:
     guesses += (1)
     Q2 = input ("If you see somebody with an offensive user name online, what is the correct response? A: Laugh at it B: Do nothing C: Report it ").upper()
     if Q2 == "C":
       print ("Correct!")
       score += 1
       time.sleep (1)
       break
     
    guesses = 0
    while guesses < 3:
     guesses += (1)
     Q3 = input ("If someone sends something inappropriate to you, what is the best action to do? A:Ingnore it B:Tell a trusted adult C:Send it to your friends ").upper()
     if Q3 == "B":
      print ("Correct!")
      score += 1
     time.sleep (1)
     break

    guesses = 0
    while guesses < 3:
      guesses += (1)
      Q4 = input ("You lose a game to one of your friends, what is the best way to respond? A:Yell at them B:Rage quit C:Say something positive ").upper()
      if Q4 == "C":
       print ("Correct!")
      score += 1
      break

#Make it repeat if input is not Y or N
    RES = input("Would you like to see your results? Y/N ").upper()
    if RES == "N":
       print ("Thanks for playing the quiz "+str(player_name))
    elif RES == "Y":
         print("Your score is "+str(score))
  