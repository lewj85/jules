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
classs = ''


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
    #root.maxsize(width=1200, height=900)

    root_label1 = tk.Label(root, text="Jules's Path", font=20)
    root_label1.pack()
    root_label2 = tk.Label(root, text="A Choose-Your-Own Adventure Story")
    root_label2.pack()

    #################################
    # Introduction
    #################################
    intro = ToggledFrame(root, text='Introduction', relief="raised", borderwidth=1)
    intro.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(intro.sub_frame, text='Choose a race').pack() # grid(row=0, column=2, pady=5)
    message = ''
    racepick = ttk.Label(intro.sub_frame, text=message)  # grid(row=2, column=2, pady=5)
    def pick_race(value):
        global race
        race = value
        if value == 'infp':
            message = "You gain a bonus to diplomacy and have a giant bunny companion."
        elif value == 'elf':
            message = "You've lived in the forest for hundreds of years and start with a magical sword."
        else:
            message = "LOTR races are overrated! You have a long neck and are fluent in GSL (Giraffe Sign Language)."
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
    
    ttk.Label(ch1.sub_frame, text="Once upon a time, in a galaxy far, far away... There lived a brave adventurer named Jules."
                                  "\nShe loved exploring, so she set out through the woods toward the next town over."
                                  "\nSoon, she approached a bridge over a small creek. There was a troll blocking the way."
                                  "\nShe noticed that the troll looked weak and hungry. He wouldn't pose much of a challenge"
                                  "\nif things got messy. When the troll demanded that she pay a toll to cross, Jules heard"
                                  "\nchildlike giggling from beneath the bridge.").pack() # grid(row=0, column=2, pady=5)
    message = ''
    ch1pick = ttk.Label(ch1.sub_frame, text=message)  # grid(row=2, column=2, pady=5)
    def pick_ch1(value):
        global race
        global option1
        if value == 'choice1':
            message = "You easily defeat the weak troll! Two emaciated troll children come out from under the bridge and " \
                      "\nrun away sobbing. They get lost. One starves to death alone in the forest and the other ends up being" \
                      "\nadopted by an angry and abusive drunk in town. He grows up to be a thug and hurts many innocent people" \
                      "\nbecause pain is all he knows. He slowly drinks himself to death, alone and unloved."
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
    # challenged to duel - elf option = "I have a secret: I'm not left-handed"
    #   - RIGHT SPEECH - thoughtful communication, words have great power, both good and bad
    ch2 = ToggledFrame(root, text='Chapter 2', relief="raised", borderwidth=1)
    ch2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch2.sub_frame, text="That evening, Jules ordered dinner in a tavern. There were no empty tables, so she grabbed "
                                  "\na seat at a table with as few people as possible. One was a loud, drunk man who boasted "
                                  "\nabout his adventures. Jules minded her own business, but the drunk man at her table "
                                  "\naccidentally knocked over his own mead without noticing. When he turned back around and "
                                  "\nsaw his spilled drink, he looked at Jules with angry eyes and yelled at her for being so"
                                  "\nclumsy. He stood up (with difficulty) and pulled out his sword. He challenged Jules to "
                                  "\na duel.").pack() # grid(row=0, column=2, pady=5)
    message = ''
    ch2pick = ttk.Label(ch2.sub_frame, text=message)  # grid(row=2, column=2, pady=5)
    def pick_ch2(value):
        global race
        global option2
        if value == 'choice1':
            message = "The fight is over as fast as it begun; you're much too fast for his drunken reflexes. You stab him and " \
                      "\nhe falls over dead. His adopted troll son runs away screaming and sobbing. The son joins a cult of " \
                      "\nevil wizards and vows revenge. While in the cult, one of the evil wizards curses him to make all his " \
                      "\ndrinks taste like cucumber water for the rest of his life. Oh, the humanity..."
        elif value == 'choice2':
            option2 = True
            message = "Using a few choice words, you're able to convince him to lay down his sword. You offer to buy him another " \
                      "\ndrink and ask him about his adventures. He happily boasts for a while and reveals a few interesting " \
                      "\nsecrets that may be helpful to you on your journey. He wishes you luck on your travels and heads to bed."
        else:
            if race == 'elf':
                option2 = True
                message = "You've had many years to practice your swordplay. You brandish your sword, twirling it through the air " \
                          "\nwith incredible dexterity. The drunkard isn't scared off so easily, however. That is, until you say, " \
                          "\n\"I know something you don't know; I am not left-handed!\" You switch to your right hand. At this, " \
                          "\nhe steps back and lowers his weapon; he realizes his mistake and apologizes. You tell him not to " \
                          "\nworry and even offer to teach him a few moves. He seems grateful and offers to teach you what he knows. " \
                          "\nYou leave with a new fencing friend and a couple of new techniques that may come in handy."
            else:
                message = "You're not an Elf! Pick again."
        ch2pick.config(text=message)
    innerch2 = ttk.Frame(ch2.sub_frame)
    ttk.Button(innerch2, text='Duel the drunkard', command=lambda: pick_ch2('choice1')).grid(row=0, column=1)
    ttk.Button(innerch2, text='Buy him a new drink', command=lambda: pick_ch2('choice2')).grid(row=0, column=2)
    ttk.Button(innerch2, text="Intimidate him (Elf only)", command=lambda: pick_ch2('choice3')).grid(row=0, column=3)

    # add empty columns before and after to center
    innerch2.grid_columnconfigure(0, weight=1)
    innerch2.grid_columnconfigure(4, weight=1)
    innerch2.pack()

    ch2pick.pack()

    #################################
    # Chapter 3
    #################################
    # lost - giraffe option = get directions from nearby deaf giraffes
    #   - RIGHT INTENT - passion for the journey, commitment to the path
    ch3 = ToggledFrame(root, text='Chapter 3', relief="raised", borderwidth=1)
    ch3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    ttk.Label(ch3.sub_frame,
              text="That evening, Jules ordered dinner in a tavern. There were no empty tables, so she grabbed "
                   "\na seat at a table with as few people as possible. One was a loud, drunk man who boasted "
                   "\nabout his adventures. Jules minded her own business, but the drunk man at her table "
                   "\naccidentally knocked over his own mead without noticing. When he turned back around and "
                   "\nsaw his spilled drink, he looked at Jules with angry eyes and yelled at her for being so"
                   "\nclumsy. He stood up (with difficulty) and pulled out his sword. He challenged Jules to "
                   "\na duel.").pack()  # grid(row=0, column=2, pady=5)
    message = ''
    ch3pick = ttk.Label(ch3.sub_frame, text=message)  # grid(row=2, column=2, pady=5)

    def pick_ch3(value):
        global race
        global option2
        if value == 'choice1':
            message = "The fight is over as fast as it begun; you're much too fast for his drunken reflexes. You stab him and " \
                      "\nhe falls over dead. His adopted troll son runs away screaming and sobbing. The son joins a cult of " \
                      "\nevil wizards and vows revenge. While in the cult, one of the evil wizards curses him to make all his " \
                      "\ndrinks taste like cucumber water for the rest of his life. Oh, the humanity..."
        elif value == 'choice2':
            option2 = True
            message = "Using a few choice words, you're able to convince him to lay down his sword. You offer to buy him another " \
                      "\ndrink and ask him about his adventures. He happily boasts for a while and reveals a few interesting " \
                      "\nsecrets that may be helpful to you on your journey. He wishes you luck on your travels and heads to bed."
        else:
            if race == 'elf':
                option2 = True
                message = "You've had many years to practice your swordplay. You brandish your sword, twirling it through the air " \
                          "\nwith incredible dexterity. The drunkard isn't scared off so easily, however. That is, until you say, " \
                          "\n\"I know something you don't know; I am not left-handed!\" You switch to your right hand. At this, " \
                          "\nhe steps back and lowers his weapon; he realizes his mistake and apologizes. You tell him not to " \
                          "\nworry and even offer to teach him a few moves. He seems grateful and offers to teach you what he knows. " \
                          "\nYou leave with a new fencing friend and a couple of new techniques that may come in handy."
            else:
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
    t1 = ToggledFrame(root, text='Chapter 4', relief="raised", borderwidth=1)
    t1.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")


    #################################
    # Chapter 5
    #################################
    # protect a caravan - giraffe option = your long neck makes you a great lookout!
    #   - RIGHT LIVELIHOOD - pick a career that helps the community
    t1 = ToggledFrame(root, text='Chapter 5', relief="raised", borderwidth=1)
    t1.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")


    #################################
    # Chapter 6
    #################################
    # chasm with broken bridge - infp option = climb on the back of your giant bunny and hop to the other side
    #   - RIGHT EFFORT - positive attitude, cheerful determination
    t1 = ToggledFrame(root, text='Chapter 6', relief="raised", borderwidth=1)
    t1.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")


    #################################
    # Chapter 7
    #################################
    # lava pit - swim through it and complain that it's too cold - skeletal remains of an INTJ nearby
    #   - RIGHT MINDFULNESS - be focused and undistracted in the moment
    t1 = ToggledFrame(root, text='Chapter 7', relief="raised", borderwidth=1)
    t1.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")


    #################################
    # Chapter 8
    #################################
    # runes - elf option = you've lived for hundreds of years and recognize this ancient language
    #   - RIGHT CONCENTRATION - learn to focus and select worthy directions for the mind
    t1 = ToggledFrame(root, text='Chapter 8', relief="raised", borderwidth=1)
    t1.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")


    #################################
    # Epilogue
    #################################
    # display all choices and results
    epi = ToggledFrame(root, text='Epilogue', relief="raised", borderwidth=1)
    epi.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")



    root.mainloop()


if __name__ == "__main__":
    create_dashboard()