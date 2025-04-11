print("Welcome to Mad Libs! Fill in the blanks:\n")

adj = input("Enter an adjective (e.g., funny, scary): ")
verb1 = input("Enter a verb (e.g., run, eat): ")
verb2 = input("Enter another verb (e.g., dance, sleep): ")
famous_person = input("Enter a famous person (e.g., Einstein, SRK): ")

story = f"""
Computer programming is so {adj}! It makes me so excited all the time
because I love {verb1}. Stay hydrated and {verb2} like you are {famous_person}!
"""

print("\n" + "="*50)
print("YOUR MAD LIBS STORY:")
print(story)
print("="*50)

while input("\nPlay again? (yes/no): ").lower() == 'yes':
    print("\nNew Game:")
    adj = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    famous_person = input("Enter a famous person: ")

    story = f"""
    Computer programming is so {adj}! It makes me so excited all the time
    because I love {verb1}. Stay hydrated and {verb2} like you are {famous_person}!
    """

    print("\n" + "="*50)
    print("YOUR MAD LIBS STORY:")
    print(story)
    print("="*50)

print("\nThanks for playing!")