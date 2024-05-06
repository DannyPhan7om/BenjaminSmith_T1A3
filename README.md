# BenjaminSmith_T1A3

## Provide full attribution to referenced sources.

Abraham Esquivel and Shubham Sharma Shubham Sharma, Change a variable over time, Stack Overflow. Available at: https://stackoverflow.com/questions/60904063/change-a-variable-over-time (Accessed: 28 April 2024).

Haddad, A. (2020) The Python Sleep Function – How to Make Python Wait A Few Seconds Before Continuing, With Example Commands, freeCodeCamp.org. freeCodeCamp.org. Available at: https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/ (Accessed: 28 April 2024).

Real Python (2023) What Does if __name__ == ‘__main__’ Do in Python?, Real Python. Real Python. Available at: https://realpython.com/if-name-main-python/ (Accessed: 4 May 2024).

How To Print Colored Text in Python (Colorama Tutorial) (2020) YouTube. YouTube. Available at: https://www.youtube.com/watch?v=u51Zjlnui4Y (Accessed: 4 May 2024).

Python Tutorial: How to Read and Write Text Files (2020) YouTube. YouTube. Available at: https://www.youtube.com/watch?v=gSbEXZvgyBw (Accessed: 4 May 2024).

Reading Text Files in Python | Python for Beginners (2022) YouTube. YouTube. Available at: https://www.youtube.com/watch?v=WwC3Vy9Sv58 (Accessed: 4 May 2024).

(No date) Python Delete File. Available at: https://www.w3schools.com/python/python_file_remove.asp (Accessed: 4 May 2024).

Learning, G. (2023) Strip in Python: An Overview of Strip() Function with Examples in 2024, Great Learning Blog: Free Resources what Matters to shape your Career! Available at: https://www.mygreatlearning.com/blog/strip-in-python/#:~:text=Python%20strip()%20is%20a,the%20end%20of%20the%20string. (Accessed: 4 May 2024).

(No date) Python String strip() Method. Available at: https://www.w3schools.com/python/ref_string_strip.asp (Accessed: 4 May 2024).

Pykes, K. (2022) How to Write a Bash Script: A Simple Bash Scripting Tutorial, DataCamp. DataCamp. Available at: https://www.datacamp.com/tutorial/how-to-write-bash-script-tutorial (Accessed: 6 May 2024).

## Provide a link to your source control repository

https://github.com/DannyPhan7om/BenjaminSmith_T1A3

## Develop a list of features that will be included in the application.

### Feature 1 - Menu Options:

#### Use of Variables and Variable Scope:

- The menu options are defined within the create_menu function and variables like pet and user_choice are included below to make sure they are only accessible from here.

#### Loops and Conditional Control Structures:

- A while loop has been used in the create_menu function to make sure it’s continuously displayed until the user chooses to exit or the game ends.

#### Error Handling:

- If the player enters an invalid choice, an error message will display and the menu will loop again to allow the player to retry.

### Feature 2 - Time-based Alteration of Attributes:

#### Use of Variables and Variable Scope:

- Happiness, fullness and energy are attributes stored within the class of virtual pets, these are altered over time by variables like is_running.

#### Loops and Conditional Control Structures:

- A while loop makes sure that the pets attributes continue to update based on the time, this occurs until the game is over.

- I used conditional statements to ensure that the attributes stay within certain limits, and if these limits are deviated from the game_over flag becomes true, ending the game and triggering a message.

#### Error Handling:

- Once again if an attribute falls below 0 or goes above 100, a message is generated and the game ends.

### Feature 3 - Saving and Loading of Files:

#### Use of Variables and Variable Scope:

- attributes such as pet_name, fullness, happiness and energy store pet data in an external txt file, calling to it when required and deleting when the game ends

#### Loops and Conditional Control Structures:

- Conditional statements are used to make different decisions based on whether or not the file exists, if it does not it is created, if it does, the data is loaded. If the game ends without the game_over flag being triggered the file is saved but if the pet dies triggering the flag, the file is deleted.

#### Error Handling:

- If the file is not found during the loading process the application should return the error FileNotFoundError

## Develop an implementation plan which outlines how each feature will be implemented and a checklist of tasks for each feature

#### Feature 1 - Using Classes for Virtual Pet:
- Create a class for the virtual pet
- give the class functions for feeding, playing and resting
- Make these functions alter the attributes of hunger, happiness, energy
- add some fun text to each function to show its working, ie snoring for resting

#### Feature 2 - Menu Options:
- Create a function for the menu options
- Include options for feeding, playing, resting and quitting the application as well as an option to refresh the screen
- Create the ability to accept user input
- Create the ability for this input to alter the pets happiness, hunger and energy levels.
- Make sure if an invalid input is selected an error appears
- Make sure this loops until the game is over or exited

#### Feature 3 - Time Based Alteration of Attributes:

- Make sure you have your pets happiness, hunger and energy attributes set up correctly
- Set up the ability for these to alter based on passing time
- Set up conditions that must be adhered to including min/max values for the game to function
- If these conditions are not met, end the game and print a message to the user.
- Make sure any errors are handled

#### Feature 4 - Saving and Loading Files:
- Create the ability for the pets attriubtes to be stored in an external file
- If this file does not exist on launch, ask for pets name and set stats to default
- If the file does exist, load the previous stats
- If the game is exited voluntarily ie by pressing 4, save the updated attributes to the file. If the pet dies, delete the file.
- If the file cannot be found at any point include adequate error handling

#### Feature 5 - Customising the layout:
- Create a virtual environment
- Install colorama
- Use colours to make the text more lively and have important things in bright colours
- Make sure your error messages are clear and in red

## Design help documentation which includes a set of instructions which accurately describe how to use and install the application.

### Introduction:
- The virtual pet simulator is a python application that allows the user to name and interact with a virtual pet. They can do so by feeding it, playing with it, and allowing it to rest when needed. The pet has minimum and maximum values for relating to these tasks that need to be maintained. If not the game will end and the pet will pass away.

### Installation:

- Make sure Python 3.12.0 or higher is installed
- Download the Virtual pet script 
- Open a terminal session
- Navigate to the directory where you’ve saved the script
- Run the script using virtual_pet.py


### How to play:
- Enter your pet's name
- From here you’ll be able to see your pets current stats as well as the menu of options
- Press numbers 1-3 and ENTER/RETURN to interact with your pet
- Once you’re done, press 4 to exit the script


### Saving and Loading:
- Your pets status will automatically be saved to a file named pet_status.txt when you exit the game. If you die in the game your progress is lost and the file will be deleted representing the pet's death. When you launch the game the previous file will be loaded and the stats pulled. If no file exists, one will be created.

### Troubleshooting:
- Check that you have the required dependencies installed, such as the colorama library.