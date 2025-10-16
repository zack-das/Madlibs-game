def story_time():
    print("Please input the following to start the game!")


#User's input
    # name = input("Enter a name (default: "Isack"):").strip()
    name = input("Enter a name:").strip()
    if name == "":
        name = "Maxyme"
    place = input("Enter a place:")
    adjective = input("Enter an adjective:")

    story = f"""Once upon a time, {name} went to {place} looking all {adjective}. Suddenly, a talking goat walked up and said,
"Yo {name}, nice shoes... are those wi-Fi enabled?"
{name} tried  to ignore it but the goat kept saying "Baa-rilliant choice!"
People were staring, {name} panicked, and accidentally replied, "Thank you, Mr. Goat...' same to you."
\n That's when everyone in {place} realized...{name} had officially lost it. """

    print("Here is your Mad Libs story!")
    print(story)


story_time()

