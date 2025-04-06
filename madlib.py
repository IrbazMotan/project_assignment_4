def madlib(Name:str, Age:int, Country:str, city:str, lucky_number:int, color:str, game:str):
    print(
        "Hello Everyone! I am here to introduce myself. My name is " + Name +
        " and I am " + str(Age) + " years old. I live in " + city + ", which is a city in " +
        Country + ". My lucky number is " + str(lucky_number) + ", and my favorite color is " +
        color + "." + game + " is the game that I play in my free time."
    )

# Input from the user
Name = input("What is your name?") 
Age = int(input("What is your current age? "))
city = input("In which city do you live? ")
Country = input("In which country do you live? ")  
lucky_number = int(input("What is your lucky number? "))
color = input("What is your favorite color? ")
game = input("Which game do you like to play? ")
# Call the function
madlib(Name, Age, Country, city, lucky_number, color, game)
