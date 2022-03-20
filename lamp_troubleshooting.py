# Tell user to turn light switch on
# If lamp turned on, declare success. If not, ask user if they have another bulb.
# If user has another bulb, ask them to turn the switch back off, change the bulb, and flip the switch back on again.
# If bulb is lit after that, declare success, otherwise advise that further troubleshooting is required.

# sorted = "not yet"

def success():
    print("Cool. Looks like you're all good.")

def tough_shit():
    print("Welp, my professional opinion of this here light fixture is that it is, as we say in the trade, fucked.")

def wtf():
    print("Wha? You gotta answer \"yes\" or \"no\".\n")

def is_fixed():
    sorted = input("Sorted?\n")
    if sorted.casefold() == "y" or sorted.casefold() == "yes":
        success()
    elif sorted.casefold() == "n" or sorted.casefold() == "no":
        tough_shit()

def go_shopping():
    print("Guess you better scoot that booty on over to the hardware store.\n")
    print("Once you've got a new bulb, stick it in there.\n")

def bulb_swap():
    new_bulb = input("Awright. Got another bulb? One that ain't broken, ideally?\n")
    if new_bulb.casefold() == "y" or new_bulb.casefold() == "yes":
        print("Great. Flip the switch back off, swap the bulb out for the new one, and flip the switch back on again.\n")
        is_fixed()
    elif new_bulb.casefold() == "n" or new_bulb.casefold() == "no":
        go_shopping()
        is_fixed()

def sanity_check():
    print("Make sure the light switch is in the \"off\" position, then flip it on.\n")
    sorted = input("Is the bulb lit?\n")
    if sorted.casefold() == "y" or sorted.casefold() == "yes":
        success()
    elif sorted.casefold() == "n" or sorted.casefold() == "no":
        bulb_swap()
    else:
        wtf()
        is_fixed()

sanity_check()