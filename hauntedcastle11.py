import time
import random
import winsound



def yeah():
    for x in range(9999):
        print("yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! yeah! ")

def bye():
    for x in range(9999):
        print('bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye bye')

print("Welcome to the Hanted Castle")
a = int(input("Choose your reading speed (1 -> very quick, 5 -> medium, 10 -> very slow)"))
def tt():
    time.sleep(a)
print("This is a place that you will never leave, exept if you answer right to all my questions, are you ready ? (All the game is in english so please write in English, it's also training your mind)")
ready=str(input())

if ready == "Yes":
    print('Let\'s go dear stranger')
    tt()
    print("So first try to anwer this very simple riddle:")
    tt()
    print("What kind of coat can you only put on when it's wet")
    tt()
    print("Hihi I've told you it was simple")
    tt()
    print("Choose one and you'll be freeee (not really but chhh)")
    tt()
    print("A coat of paint tap 1")
    tt()
    print("Just a wet coat LOL and tap 2")
    tt()
    print("The new Dior collection, with blue and grey shades that appear when it's raining, alternatively, it's white white white (ugly ugly ugly) tap DIDI")
    tt()
    print("DONT'T TAP ANYTHING ELSE !!!")
    tt()
    print("If you want you can tap nothing")
    riddle1=str(input())

    if riddle1 == "1":
        bye()
    elif riddle1 == "2":
        bye()
    elif riddle1 == "DIDI":
        bye()
    elif riddle1 == "nothing" or riddle1 == "Nothing":
        print("But...")
        tt()
        print("How did you know ?")
        tt()
        print("It was a secret")
        tt()
        print("Okay")
        tt()
        print("Okay, okay")
        tt()
        phonenum=input("Let's be friends, gimme ya number bro")
        tt()
        rep1=str(input(" Is it this one: " , phonenum, "?"))
        if rep1==phonenum:
            print("Okay, right, call you later")
        else:
            print("OK, got it, see you")
        tt()
        print("Oh I forgot to give you the code of the locker")
        tt()
        print("83475")
        code1=int(input("Write it here:"))
        if code1 == "83475":
            print("You're free, go now")
            tt()
            yeah()
        else:
            print("C:/User Error__Syntaxe: CannotFindFile_TryAgai/")
            time.sleep(5)
            bye()
        
    
    elif riddle1 != "DIDI" and riddle1 != "1" and riddle1 != "2":
        accode=8
        
        print("You're more clever than at the end, go next ->>>")
        tt()
        print("Oho, you won this ; the first number of the access code, if you have five of them (maybe more, I'm not sure), you will go out of this d***** castle")
        tt()
        print("code = ", accode)
        tt()
        print("You know I'm a very lonely person")
        tt()
        print("What you just said, \"You're not a real person\" Ok ok I'm taking your number back")
        time.sleep(7)
        print("Now you have 3 doors, normally it's two but I added you one cause I'm very nice")
        tt()
        print("Yeah I know no thanks please, please")
        tt()
        print("No seriously here are two doors and choose quickly, I have no time for thoose games")
        tt()
        print("You still didn't choose, hum ok I'm gonna choose for you")
        tt()
        a = random.randint(1, 3)
        print("Hihi your door is the number", a)
        
        if a == 2:
            print("Welcome my dear friend, you passed it, well done !")
            time.sleep(10)
            bye()

        else:
            accode=83
            print("I'm sorry it was the other one, now you'll have zombies or something like that in this room, bye bye")
            tt()
            print("HAHAHA no it's a prank you passed the second level so you have the second number")
            tt()
            print("code = ", accode)
            tt()
            print("Hum hum, let's stay serious")
            tt()
            print("The room is dark, and there is a corridor in the darkest place of the room")
            tt()
            print("And in the end of the corridor")
            time.sleep(3)
            print("There is a yellow light")
            tt()
            print("What is this light ?")
            tt()
            print("Your right answer is another number of the code" )
            tt()
            print("1 : there is no light at all it's an optic illusion")
            tt()
            print("2 : oh there someone here, maybe he can help me ")
            tt()
            print("3 : A light, that's the exit")
            tt()
            print("4 : Maybe, maybe it's someone who wanna fight you, but I don't know, I'm just the person who's telling the things you can do, remember")
            tt()
            print("Do your choice")
            
            choice1=input()
              
            if choice1 == "1":
              print("I is it a little weird but everything here is weird so I completly understand you")
              tt()
              print("But this still isn't right")
              bye()
              
            elif choice1=="2":
              print("Sorry it was the ghost you saw earlier so it ate you")
              time.sleeper(5)
              print("Good luck")
              bye()
              
            elif choice1 == "3":
              print("Ok you found it, run there")
              tt()
              print("Oupsss sorry you lay into it")
              tt()
              print("Snif snif")
              tt()
              bye()

            elif choice1 == "4":
              name=str(input("Tell me your name"))
              print("Go go", name, "Gooo")
              tt()
              accode=834
              print("code = ", accode)
              tt()
              print("Haha now you have 3 numbers in your access code, 2 left")
              tt()
              print("Next step :")
              tt()
              print("Oups I'm sorry I think you can't fight it it's too big and too strong for you")
              tt()
              print("If you want you can still fight it tap 1 to do it")
              tt()
              print("But if you want to run (and it's more intelligent if you want my opinion) tap 2")
              tt()
              choice2=input()
              
              if choice2 == "1":
                  print("Hoho")
                  tt()
                  print("It's coming")
                  tt()
                  print("Oh no I think you're dead")
                  tt()
                  print("Sorry for you")
                  bye()
              
              elif choice2 == "2":
                  print("Quick quick")
                  print("Find a place where you can cover up")
                  tt()
                  print("Oh no a locked door with a locker")
                  tt()
                  print("THERE IS SOMETHING WRITTEN")
                  tt()
                  print("A philosophic question")
                  tt()
                  print("What makes you, young")
                  tt()
                  print("Okay 1 : being a baby")
                  tt()
                  print("2 : just have some great time with someone you love")
                  tt()
                  print("3 : adding the letters \"ng\" (this is soooo not interesting)")
                  tt()
                  print("4 : feeling young is the most important")
                  tt()
                  question2=(input())
              
                  if question2=="1":
                      print(" Ow so cute")
                      time.sleeep(10)
                      bye()
                
                  elif question2 =="2":
                      print("Yeah that's great")
                      tt()
                      print("But that's not the reality")
                      tt()
                      print("So...")
                      time.sleep(10)
                      bye()

                  elif question2 == "3":
                      print("Yeah there is someone realistic !!!!")
                      tt()
                      accode =  8347
                      print("You're right")
                      tt()
                      print("Now you have FOUR numbers")
                      tt()
                      print("code = ", accode)
                      tt()
                      print("Stay hidden and let's do another question")
                      tt()
                      print("A and B were sitting on a table, A disappeared, B left the table")
                      tt()
                      print("Who is still on the table")
                      tt()
                      print("This is just a question of logic so don't think too much")
                      tt()
                      print("PS : it's an str input")
                      question3=str(input())
                      if question3 == "and" or question3 == "And":
                                accode = 83475
                                print("Okay now you have all the code numbers : ")
                                print("code = ", accode)
                                print("Now enter the code here and run to the door at your left, it's the exit, you deserved it")
                                codeee=int(input())
                                if codeee == accode:
                                         yeah()
                                else:
                                    bye()

                                         
                      else:
                        print("So sorry you lost at the last question")
                        bye()
                                
                                
                    
                      
                    
                      
elif ready =="No":
    bye()

