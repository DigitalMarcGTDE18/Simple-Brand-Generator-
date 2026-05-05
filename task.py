print("Hello my fellow friend! Welcome to the band name generator. How are you doing today?")
print(input("Enter good or bad: "))
if input == "bad":
    print(input("I am sorry to hear that! Would you like to continue, q/n"))
elif input == "q":
    exit(0)
else:
    print("Are you ready to create a band name!?")

user_input = (input("Enter the name of a pet you have/had: "))
city_input = (input("Enter the name of the city you are living in: "))

print(f'Your newly made band is called {city_input} {user_input} ')


