print("You see a monkey walking on the wall fence")
instinct =input("Would you RUN or STARE at the sight of a wild animal? ")

if instinct.lower() == "run":
    print("Ouch! You run towards a crawling snake") 
    response = input("You are at crossroads.HIT the snake, SCREAM or CALL SOS? ")
    if response.lower() == "hit":
        print("You hit the snake so hard, it's the end of the snake")
    elif response.lower() == "scream":
        print("Ahah! your scream is so loud it terrified the poor snake to seek cover")
    else:   
        response.lower() == "call SOS"
        print("You have called SOS which seemed like the dumbest choice.A lizard passes by an falls prey to the snake.")
        print("The snake has a firm grip on its prey and drags it away. Oh! what a relief.")
else: 
    instinct.lower() == "STARE"
    print("Stare? such bravery")
    action = input("The monkey appears hungry. Attempts to jump down. PASS it some food or SCARE it away? ")
    if action.lower() == "pass":
        print("Isn't a bad idea to show some love to an animal, the problem is the monkey will take you as a friend. it will keep coming")    
    else:   
        action.lower() == "scare"
        print("Raising your hands to scare the monkey. It mimics your every step\n Monkeys are friends to humans afterall.")
