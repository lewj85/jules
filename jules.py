import tkinter as tk
from tkinter import ttk

# globals
option1 = False
option2 = False
option3 = False
option4 = False
option5 = False
option6 = False
option7 = False
option8 = False
race = ''


class ToggledFrame(tk.Frame):

    def __init__(self, parent, text="", *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)

        self.show = tk.IntVar()
        self.show.set(0)

        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill="x", expand=1)

        ttk.Label(self.title_frame, text=text).pack(side="left", fill="x", expand=1)

        self.toggle_button = ttk.Checkbutton(self.title_frame, width=2, text='+', command=self.toggle,
                                            variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="left")

        self.sub_frame = tk.Frame(self, relief="sunken", borderwidth=1)

    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill="x", expand=1)
            self.toggle_button.configure(text='-')
        else:
            self.sub_frame.forget()
            self.toggle_button.configure(text='+')


def create_dashboard():
    root = tk.Tk()
    root.title("I know, I'm amazing")
    root.minsize(width=600, height=100)
    # root.maxsize(width=600, height=500)
    # scrollbar = tk.Scrollbar(root)
    # scrollbar.pack(side='right', fill='y')

    root_label1 = tk.Label(root, text="Jules's Path", font=20)
    root_label1.pack()
    root_label2 = tk.Label(root, text="A Choose-Your-Own Adventure Story")
    root_label2.pack()

    #################################
    # Introduction
    #################################
    intro = ToggledFrame(root, text='Introduction', relief="raised", borderwidth=1)
    intro.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(intro.sub_frame, text="Once upon a time, in a galaxy far, far away... There lived a brave adventurer named Jules."
                                  "\nShe loved exploring and helping people, so she set out through the woods with one goal: "
                                  "\none day, she would save the world.").pack()
    ttk.Label(intro.sub_frame, text='\nChoose a race').pack()
    message = ''
    racepick = ttk.Label(intro.sub_frame, text=message) 
    def pick_race(value):
        global race
        race = value
        if value == 'infp':
            message = "You gain a bonus to diplomacy and have a giant bunny companion\n"
        elif value == 'elf':
            message = "You've lived in the forest for hundreds of years and own a magical sword.\n"
        else:
            message = "LOTR races are overrated! You have a long neck and are fluent in GSL (Giraffe Sign Language).\n"
        racepick.config(text=message)
    innerintro = ttk.Frame(intro.sub_frame)
    ttk.Button(innerintro, text='INFP', command=lambda: pick_race('infp')).grid(row=0, column=1)
    ttk.Button(innerintro, text='Elf', command=lambda: pick_race('elf')).grid(row=0, column=2)
    ttk.Button(innerintro, text='Giraffe', command=lambda: pick_race('giraffe')).grid(row=0, column=3)

    # add empty columns before and after to center
    innerintro.grid_columnconfigure(0, weight=1)
    innerintro.grid_columnconfigure(4, weight=1)
    innerintro.pack()

    racepick.pack()


    #################################
    # Chapter 1
    #################################
    # troll bridge - infp option = empathize
    #   - RIGHT UNDERSTANDING - see the world as it really is
    ch1 = ToggledFrame(root, text='Chapter 1', relief="raised", borderwidth=1)
    ch1.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")
    
    ttk.Label(ch1.sub_frame, text="\nWhile traveling through the forest, Jules approached a bridge over a small creek. There "
                                  "\nwas a troll blocking the way. She noticed that the troll looked weak and hungry. He "
                                  "\nwouldn't pose much of a challenge if things got messy. When the troll demanded that she "
                                  "\npay a toll to cross, Jules heard childlike giggling from beneath the bridge.").pack()
    message = ''
    ch1pick = ttk.Label(ch1.sub_frame, text=message) 
    def pick_ch1(value):
        global race
        global option1
        if value == 'choice1':
            option1 = False
            message = "You easily defeat the weak troll! Two emaciated troll children come out from under the bridge and " \
                      "\nrun away sobbing. They get lost. One starves to death alone in the forest and the other ends up being" \
                      "\nadopted by an angry and abusive drunk in town. He grows up never remembering what it was like to " \
                      "\nbe loved."
        elif value == 'choice2':
            option1 = True
            message = "The troll looks relieved, thanks you, and lets you pass. Later that day, you spot the troll in town " \
                      "\nbuying food for his starving children. They all look happy."
        else:
            if race == 'infp':
                option1 = True
                message = "You ask the troll if everything is alright. He looks surprised. Nobody has ever asked him that" \
                          "\nbefore. He lets his guard down and says it's been a rough year. You begin to understand that he's" \
                          "\nacting out of desperation. He tells you that he just lost his wife and is having a hard time " \
                          "\nraising the kids alone. He just wants money to help feed them. You give him some money for food, " \
                          "\nbut also tell him about a friend in your hometown who's hiring and owes you a favor. You tell " \
                          "\nthe troll to head there and mention your name. You've befriended the troll and set him up with a " \
                          "\nsteady job. He thanks you profusely for understanding and caring. His children come out from" \
                          "\nhiding and hug you. They all head off toward town with hope in their hearts."
            else:
                option1 = False
                message = "You're not an INFP! Pick again."
        ch1pick.config(text=message)
    innerch1 = ttk.Frame(ch1.sub_frame)
    ttk.Button(innerch1, text='Slay the troll', command=lambda: pick_ch1('choice1')).grid(row=0, column=1)
    ttk.Button(innerch1, text='Pay the toll', command=lambda: pick_ch1('choice2')).grid(row=0, column=2)
    ttk.Button(innerch1, text='Empathize and listen (INFP only)', command=lambda: pick_ch1('choice3')).grid(row=0, column=3)

    # add empty columns before and after to center
    innerch1.grid_columnconfigure(0, weight=1)
    innerch1.grid_columnconfigure(4, weight=1)
    innerch1.pack()

    ch1pick.pack()

    #################################
    # Chapter 2
    #################################
    # lost - giraffe option = get directions from nearby deaf giraffes
    #   - RIGHT INTENT - passion for the journey, commitment to the path
    ch2 = ToggledFrame(root, text='Chapter 2', relief="raised", borderwidth=1)
    ch2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch2.sub_frame,
              text="Jules set out toward the jungles far to the south. It was rumored that there was a long-forgotten "
                   "\ncivilization hidden under all the foliage there. After several days of travel through a foggy valley, "
                   "\nover a pink glacier, and past a prairie of tall grass and passionflowers, Jules finally reached the "
                   "\nedge of the jungle. She ventured in without a map, and it wasn't long before she got lost.").pack()
    message = ''
    ch2pick = ttk.Label(ch2.sub_frame, text=message)

    def pick_ch2(value):
        global race
        global option2
        if value == 'choice1':
            option2 = False
            message = "You give up searching and turn back. Had you continued on, you would have scared off a warthog, which " \
                      "\nlater ended up walking into a family of leopards. You didn't though, so the leopards kept hunting and " \
                      "\neventually found a young troll cultist nearby. He managed to escape them, but not before they ate his " \
                      "\nfoot. The troll boy would now walk with a peg leg and a painful limp for rest of his life."
        elif value == 'choice2':
            option2 = True
            message = "You continue searching and eventually find some stones with beautiful carvings. You bring them to the" \
                      "\nnext town you get to and donate them to the local museum. The curator insists on a small reward. You " \
                      "\ncontinue on your journey knowing you've preserved a small part of history."
        else:
            if race == 'giraffe':
                option2 = True
                message = "You break out your GSL and ask some giraffes in the nearby prairie where to find the ruins. They " \
                          "\ngive you directions to a waterfall and say the entrance is hidden behind it. You look behind " \
                          "\nthe waterfall and discover an entire lost city of immeasurable beauty. When you get to the next" \
                          "\ntown, you find the curator of the local museum and he organizes an expedition based on your " \
                          "\ndirections. The city is able to be studied in great depth and generations of historians benefit " \
                          "\nfrom what is discovered about the lost civilization."
            else:
                option2 = False
                message = "You're not a Giraffe! Pick again."
        ch2pick.config(text=message)

    innerch2 = ttk.Frame(ch2.sub_frame)
    ttk.Button(innerch2, text='Give up', command=lambda: pick_ch2('choice1')).grid(row=0, column=1)
    ttk.Button(innerch2, text='Keep looking', command=lambda: pick_ch2('choice2')).grid(row=0, column=2)
    ttk.Button(innerch2, text="Get directions from nearby deaf giraffes (Giraffe only)",
               command=lambda: pick_ch2('choice3')).grid(row=0, column=3)

    # add empty columns before and after to center
    innerch2.grid_columnconfigure(0, weight=1)
    innerch2.grid_columnconfigure(4, weight=1)
    innerch2.pack()

    ch2pick.pack()

    #################################
    # Chapter 3
    #################################
    # challenged to duel - elf option = "I have a secret: I'm not left-handed"
    #   - RIGHT SPEECH - thoughtful communication, words have great power, both good and bad
    ch3 = ToggledFrame(root, text='Chapter 3', relief="raised", borderwidth=1)
    ch3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch3.sub_frame, text="That evening, Jules ordered dinner in a tavern. There were no empty tables, so she grabbed "
                                  "\na seat at a table with as few people as possible. One was a loud, drunk man who boasted "
                                  "\nabout his adventures. Jules minded her own business, but the drunk man at her table "
                                  "\naccidentally knocked over his own mead without noticing. When he turned back around and "
                                  "\nsaw his spilled drink, he looked at Jules with angry eyes and yelled at her for being so"
                                  "\nclumsy. He stood up (with difficulty) and pulled out his sword. He challenged Jules to "
                                  "\na duel.").pack()
    message = ''
    ch3pick = ttk.Label(ch3.sub_frame, text=message) 
    def pick_ch3(value):
        global race
        global option3
        if value == 'choice1':
            option3 = False
            message = "The fight is over as fast as it begun; you're much too fast for his drunken reflexes. You stab him and " \
                      "\nhe falls over dead. His adopted troll son runs away screaming and sobbing. The son joins a cult of " \
                      "\nevil wizards and vows revenge. While in the cult, one of the evil wizards curses him to make all his " \
                      "\ndrinks taste like cucumber water for the rest of his life."
        elif value == 'choice2':
            option3 = True
            message = "Using a few choice words, you're able to convince him to lay down his sword. You offer to buy him another " \
                      "\ndrink and ask him about his adventures. He happily boasts for a while and reveals a few interesting " \
                      "\nsecrets that may be helpful to you on your journey. He wishes you luck on your travels and heads to bed."
        else:
            if race == 'elf':
                option3 = True
                message = "You've had many years to practice your swordplay. You brandish your sword, twirling it through the air " \
                          "\nwith incredible dexterity. The drunkard isn't scared off so easily, however. That is, until you say, " \
                          "\n\"I know something you don't know; I am not left-handed!\" You switch to your right hand. At this, " \
                          "\nhe steps back and lowers his weapon; he realizes his mistake and apologizes. You tell him not to " \
                          "\nworry and even offer to teach him a few moves. He seems grateful and offers to teach you what he knows. " \
                          "\nYou leave with a new fencing friend and a couple of new techniques that may come in handy."
            else:
                option3 = False
                message = "You're not an Elf! Pick again."
        ch3pick.config(text=message)
    innerch3 = ttk.Frame(ch3.sub_frame)
    ttk.Button(innerch3, text='Duel the drunkard', command=lambda: pick_ch3('choice1')).grid(row=0, column=1)
    ttk.Button(innerch3, text='Buy him a new drink', command=lambda: pick_ch3('choice2')).grid(row=0, column=2)
    ttk.Button(innerch3, text="Intimidate him (Elf only)", command=lambda: pick_ch3('choice3')).grid(row=0, column=3)

    # add empty columns before and after to center
    innerch3.grid_columnconfigure(0, weight=1)
    innerch3.grid_columnconfigure(4, weight=1)
    innerch3.pack()

    ch3pick.pack()
    
    #################################
    # Chapter 4
    #################################
    # starving sharks - share your food with them?
    #   - RIGHT ACTION - always take the ethical approach in life
    ch4 = ToggledFrame(root, text='Chapter 4', relief="raised", borderwidth=1)
    ch4.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch4.sub_frame,
              text="Jules eventually found her way to a short, beautiful cliff overlooking a cove that connected to the ocean. "
                   "\nShe heard screaming and looked down. She saw a troll boy splashing in the water, circled by a school of "
                   "\nsharks. He cried out to Jules for help.").pack()
    message = ''
    ch4pick = ttk.Label(ch4.sub_frame, text=message) 

    def pick_ch4(value):
        global race
        global option4
        if value == 'choice1':
            option4 = False
            message = "Sharks and deep water? Screw that. You run like hell and let nature take its course. The troll boy " \
                      "\nmanages to swim to safety, but loses a hand in the process. He relives the trauma every day and " \
                      "\ngoes the rest of his life with night terrors and PTSD."
        else:
            option4 = True
            message = "You have rope you can throw him but it's too short. You run down to the water's edge and take a few " \
                      "\nbrave steps into the shark-infested waters. You toss the rope to him and he catches it. You're able " \
                      "\nto reel him in before the sharks can do any damage. He even punches a few in the nose and laughs " \
                      "\na couple times. He says thanks and runs off to tell the story of how he braved a pool of sharks to " \
                      "\nhis cultist buddies."
        ch4pick.config(text=message)

    innerch4 = ttk.Frame(ch4.sub_frame)
    ttk.Button(innerch4, text='Run away', command=lambda: pick_ch4('choice1')).grid(row=0, column=1)
    ttk.Button(innerch4, text='Try to save him', command=lambda: pick_ch4('choice2')).grid(row=0, column=2)

    # add empty columns before and after to center
    innerch4.grid_columnconfigure(0, weight=1)
    innerch4.grid_columnconfigure(3, weight=1)
    innerch4.pack()

    ch4pick.pack()
    
    #################################
    # Chapter 5
    #################################
    # protect a caravan - giraffe option = your long neck makes you a great lookout!
    #   - RIGHT LIVELIHOOD - pick a career that helps the community
    ch5 = ToggledFrame(root, text='Chapter 5', relief="raised", borderwidth=1)
    ch5.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch5.sub_frame,
              text="Jules walked east along a dirt road. A traveling caravan caught up to her, heading in the same direction. "
                   "\nThere were nine wagons, each carrying its own family and goods for sale. Roads were common places for "
                   "\nbandits to rob passersby. The leader of the caravan asked if Jules wanted to join them and even offered "
                   "\nto pay her to protect the wagons for the next couple days, until they reached the next big town.").pack()
    message = ''
    ch5pick = ttk.Label(ch5.sub_frame, text=message)

    def pick_ch5(value):
        global race
        global option5
        if value == 'choice1':
            option5 = False
            message = "You tell him you're not interested in helping. The caravan passes you. An hour later, you see the caravan" \
                      "\nagain in the distance. You catch up to it and see that it's been robbed and ransacked. There are dead" \
                      "\nbodies everywhere. There are ripped evil wizard cultist robes on the ground. There's also a pool of green " \
                      "\ntroll blood on the ground; evidently, a member of the caravan was able to injure one of the cultists " \
                      "\nwho attacked them."
        elif value == 'choice2':
            option5 = True
            message = "Your caravan approaches a small group of cultists blocking the road about an hour later. They seem " \
                      "\nhesitant due to the fact that they're outnumbered. You step forward and their confidence wavers, ever" \
                      "\nso slightly. It seems to be the straw that breaks the camel's back though; they decide to back off " \
                      "\nand let you pass. The caravan families thank you and pay you when you get to town safely."
        else:
            if race == 'giraffe':
                option5 = True
                message = "Your long neck makes you a great lookout! You can see a group of cultists far down the road and " \
                          "\nwarn the caravan not to go further. You also spot a somewhat hidden road off that appears to run" \
                          "\nparallel. You guide the caravan to this second road, which turns out to not only be bandit-free, " \
                          "\nbut a shortcut to town! The caravan families thank you profusely for protecting them. They pay" \
                          "\nyou double what you originally agreed to for showing them an alternate, safer route they can take " \
                          "\nin the future."
            else:
                option5 = False
                message = "You're not a Giraffe! Pick again."
        ch5pick.config(text=message)

    innerch5 = ttk.Frame(ch5.sub_frame)
    ttk.Button(innerch5, text='Ignore his request', command=lambda: pick_ch5('choice1')).grid(row=0, column=1)
    ttk.Button(innerch5, text='Protect the caravan', command=lambda: pick_ch5('choice2')).grid(row=0, column=2)
    ttk.Button(innerch5, text="Offer to be a lookout (Giraffe only)", command=lambda: pick_ch5('choice3')).grid(row=0, column=3)

    # add empty columns before and after to center
    innerch5.grid_columnconfigure(0, weight=1)
    innerch5.grid_columnconfigure(4, weight=1)
    innerch5.pack()

    ch5pick.pack()

    #################################
    # Chapter 6
    #################################
    # chasm with broken bridge - infp option = climb on the back of your giant bunny and hop to the other side
    #   - RIGHT EFFORT - positive attitude, cheerful determination
    ch6 = ToggledFrame(root, text='Chapter 6', relief="raised", borderwidth=1)
    ch6.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch6.sub_frame,
              text="Jules approached a rocky gorge with deep chasms and cracks. There was a large river at the bottom that "
                   "\nseemed tiny from this high up. An old and questionable rope bridge stretched across from one side to "
                   "\nthe other. There were no other ways across.").pack()
    message = ''
    ch6pick = ttk.Label(ch6.sub_frame, text=message)

    def pick_ch6(value):
        global race
        global option6
        if value == 'choice1':
            option6 = False
            message = "The bridge would probably break if you tried to cross it. You decide to turn back and head home. Later," \
                      "\na group of cultists approach the bridge and try to cross it. A few cultists begin to cross, including " \
                      "\na troll. The additional weight stresses the bridge and the rope snaps, sending them falling into the " \
                      "\nravine! The troll survives due to his Jiu Jitsu, but breaks several bones, including his butt. He'll " \
                      "\nnever sit comfortably again."
        elif value == 'choice2':
            option6 = True
            message = "Feeling hopeful, you cross the bridge. You make sure to be extra careful where you choose to step, but" \
                      "\nyour confidence prevents you from lingering and putting extra pressure on any one spot for too long." \
                      "\nJust as you make it to the other side, the rope finally gives way and snaps. You made it safely though," \
                      "\nand continue on your journey."
        else:
            if race == 'infp':
                option6 = True
                message = "You hug your giant bunny and climb onto its back. You scratch it behind its ears and it hops across" \
                          "\nthe chasm with joy. When you get to the other side, you notice that the rope bridge is a little weak" \
                          "\nfrom this side. You take a few minutes to re-secure the rope bridge on this side, allowing others to " \
                          "\ncross it without danger. You continue on your journey knowing you probably saved a life or two."
            else:
                option6 = False
                message = "You're not an INFP! Pick again."
        ch6pick.config(text=message)

    innerch6 = ttk.Frame(ch6.sub_frame)
    ttk.Button(innerch6, text='Turn back', command=lambda: pick_ch6('choice1')).grid(row=0, column=1)
    ttk.Button(innerch6, text='Give the bridge a chance', command=lambda: pick_ch6('choice2')).grid(row=0, column=2)
    ttk.Button(innerch6, text="Hop across with your giant bunny (INFP only)", command=lambda: pick_ch6('choice3')).grid(row=0, column=3)

    # add empty columns before and after to center
    innerch6.grid_columnconfigure(0, weight=1)
    innerch6.grid_columnconfigure(4, weight=1)
    innerch6.pack()

    ch6pick.pack()
    
    #################################
    # Chapter 7
    #################################
    # lava pit - swim through it and complain that it's too cold - skeletal remains of an INTJ nearby
    #   - RIGHT MINDFULNESS - be focused and undistracted in the moment
    ch7 = ToggledFrame(root, text='Chapter 7', relief="raised", borderwidth=1)
    ch7.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch7.sub_frame,
              text="News spread that a dragon egg had been spotted in the crater of an active volcano. An evil wizard cult"
                   "\nwanted to capture the egg for themselves to raise an evil dragon and conquer the world. When Jules "
                   "\nheard this, she knew she had to beat the cultists to the egg. She headed for the volcano and climbed "
                   "\nto the crater at the top. At the center of the lava pit was the dragon egg. Jules noticed a scorched "
                   "\nskeleton off to the side in the lava.").pack()
    message = ''
    ch7pick = ttk.Label(ch7.sub_frame, text=message)

    def pick_ch7(value):
        global race
        global option7
        if value == 'choice1':
            option7 = False
            message = "You head over to the skeleton. After careful analysis, you conclude these are the bones of an INTJ who" \
                      "\ntried to shower in the lava and burned to death. While investigating the bones, a troll cultist sneaks" \
                      "\nover to the egg and performs an evil summoning ritual. The dragon hatches and tries to eat the troll," \
                      "\nknocking him back into the lava. The troll manages to crawl out, but half his skin has melted off, leaving" \
                      "\nhim horribly disfigured. The evil ritual succeeds and so the dragon heralds an age of darkness upon " \
                      "\nthe land."
        else:
            option7 = True
            message = "You focus and head straight for the egg. As you swim through the lava pit, you complain that it's too" \
                      "\ncold. You hug the egg, showing it love and compassion. The dragon hatches as a good dragon, heralding" \
                      "\na golden age of peace and prosperity."
        ch7pick.config(text=message)

    innerch7 = ttk.Frame(ch7.sub_frame)
    ttk.Button(innerch7, text='Investigate the skeleton', command=lambda: pick_ch7('choice1')).grid(row=0, column=1)
    ttk.Button(innerch7, text='Head straight for the egg', command=lambda: pick_ch7('choice2')).grid(row=0, column=2)

    # add empty columns before and after to center
    innerch7.grid_columnconfigure(0, weight=1)
    innerch7.grid_columnconfigure(3, weight=1)
    innerch7.pack()

    ch7pick.pack()

    #################################
    # Chapter 8
    #################################
    # runes - elf option = you've lived for hundreds of years and recognize this ancient language
    #   - RIGHT CONCENTRATION - learn to focus and select worthy directions for the mind
    ch8 = ToggledFrame(root, text='Chapter 8', relief="raised", borderwidth=1)
    ch8.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch8.sub_frame,
              text="After saving/dooming the world, Jules decided to end her adventure. She headed back home. On the way "
                   "\nback, she found a giant boulder with a bunch of ancient runes carved into it.").pack()
    message = ''
    ch8pick = ttk.Label(ch8.sub_frame, text=message)

    def pick_ch8(value):
        global race
        global option8
        if value == 'choice1':
            option8 = False
            message = "Why would you click this?!"
        elif value == 'choice2':
            option8 = True
            message = "You feel that translating/learning languages is a worthy pursuit and take the time to decipher the runes."
        else:
            if race == 'elf':
                option8 = True
                message = "You recognize your old tongue: Quenya."
            else:
                option8 = False
                message = "You're not an Elf! Pick again."
        ch8pick.config(text=message)

    innerch8 = ttk.Frame(ch8.sub_frame)
    ttk.Button(innerch8, text="Languages are boring", command=lambda: pick_ch8('choice1')).grid(row=0, column=1)
    ttk.Button(innerch8, text="Take the time to decipher it", command=lambda: pick_ch8('choice2')).grid(row=0, column=2)
    ttk.Button(innerch8, text="Recognize the ancient language (Elf only)", command=lambda: pick_ch8('choice3')).grid(row=0, column=3)

    # add empty columns before and after to center
    innerch8.grid_columnconfigure(0, weight=1)
    innerch8.grid_columnconfigure(4, weight=1)
    innerch8.pack()

    ch8pick.pack()

    #################################
    # Epilogue
    #################################
    # display all choices and results
    epi = ToggledFrame(root, text='Epilogue', relief="raised", borderwidth=1)
    epi.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    epipick1 = ttk.Label(epi.sub_frame)
    epipick2 = ttk.Label(epi.sub_frame)
    epipick3 = ttk.Label(epi.sub_frame)
    epipick4 = ttk.Label(epi.sub_frame)
    epipick5 = ttk.Label(epi.sub_frame)
    epipick6 = ttk.Label(epi.sub_frame)
    epipick7 = ttk.Label(epi.sub_frame)
    epipick8 = ttk.Label(epi.sub_frame)
    final1 = ttk.Label(epi.sub_frame)
    final2 = ttk.Label(epi.sub_frame)

    def pick_epi(value):
        global option1
        global option2
        global option3
        global option4
        global option5
        global option6
        global option7
        global option8

        message1 = ''
        message2 = ''
        message3 = ''
        message4 = ''
        message5 = ''
        message6 = ''
        message7 = ''
        message8 = ''

        if option1:
            message1 = "By paying the toll to help the troll, Jules demonstrated RIGHT UNDERSTANDING. " \
                       "\nShe understood that things aren't always as they appear. She saw the world as it really was."
        if option2:
            message2 = "By not giving up when she lost her way, Jules demonstrated RIGHT INTENT. " \
                       "\nHer passion for the journey and commitment to the path led her to what she sought."
        if option3:
            message3 = "By talking to the drunk man rather than fighting, Jules demonstrated RIGHT SPEECH." \
                       "\nWords have great power, both for good and for bad. Thoughtful communication helped her."
        if option4:
            message4 = "By trying to save the troll from the sharks, Jules demonstrated RIGHT ACTION." \
                       "\nShe always took the ethical approach in life, even when it wasn't easy."
        if option5:
            message5 = "By helping to protect the caravan, Jules demonstrated RIGHT LIVELIHOOD." \
                       "\nShe chose a job that helped those around her. She made a positive difference."
        if option6:
            message6 = "By crossing the chasm despite the obvious difficulties, Jules demonstrated RIGHT EFFORT." \
                       "\nHer positive attitude and cheerful determination helped her to move forward and make progress."
        if option7:
            message7 = "By going straight for the dragon egg, Jules demonstrated RIGHT MINDFULNESS." \
                       "\nShe remained focused and undistracted in the moment, keeping her primary goal in mind."
        if option8:
            message8 = "By deciphering the runes, Jules demonstrated RIGHT CONCENTRATION. " \
                       "\nShe learned to focus and select worthy directions for her mind."
        message9 = "\nJules was well on her way to Nirvana."
        message10 = "\n\nJules,\nYou've made this past month the happiest time of my life. I hope we're together for many more." \
                    "\n\nI see you.\n"

        epipick1.config(text=message1)
        epipick2.config(text=message2)
        epipick3.config(text=message3)
        epipick4.config(text=message4)
        epipick5.config(text=message5)
        epipick6.config(text=message6)
        epipick7.config(text=message7)
        epipick8.config(text=message8)
        final1.config(text=message9)
        final2.config(text=message10)

    ttk.Label(epi.sub_frame, text="Double-check your answers and then click below to generate the rune message!").pack()
    ttk.Button(epi.sub_frame, text="Generate runes",
               command=lambda: pick_epi('choice1')).pack()

    epipick1.pack()
    epipick2.pack()
    epipick3.pack()
    epipick4.pack()
    epipick5.pack()
    epipick6.pack()
    epipick7.pack()
    epipick8.pack()
    final1.pack()
    final2.pack()

    root.mainloop()


if __name__ == "__main__":
    create_dashboard()