from logic import *


# Propositions

low_level = Variable("LowLevelCriminal")
joker = Variable("Joker")
penguin = Variable("Penguin")
riddler = Variable("Riddler")
acid_burn = Variable("AcidBurn")
playing_cards = Variable("PlayingCards")
joy_buzzer = Variable("JoyBuzzer")
umbrella_mark = Variable("UmbrellaMark")
riddle = Variable("Riddle")
hole = Variable("HoleInGround")

# Formulas

# Villain 
joker_formula = acid_burn >> joker
penguin_formula = umbrella_mark >> penguin
riddler_formula = riddle >> riddler


hole_found = hole
hole_formula = hole >> (acid_burn | umbrella_mark)


# Arguments

joker_argument = ArgumentForm(
    hole_found,
    hole_formula,
    joker_formula,
    conclusion=joker
)

penguin_argument = ArgumentForm(
    hole_found,
    hole_formula,
    penguin_formula,
    conclusion=penguin
)

riddler_argument = ArgumentForm(
    hole_found,
    hole_formula,
    riddler_formula,
    conclusion=riddler
)

low_level_argument = ArgumentForm(
    hole_found,
    hole_formula,
    conclusion=low_level
)

print("Who definitely committed this crime:")
print("A low-level criminal:", low_level_argument.is_valid())
print("The Joker:", joker_argument.is_valid())
print("The Penguin:", penguin_argument.is_valid())
print("The Riddler:", riddler_argument.is_valid())



