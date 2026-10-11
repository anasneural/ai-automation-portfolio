Poem = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star."""
print(Poem)

# Use REPL and print the table of 5 using it.
# >>> 5*1
# 5
# >>> 5*2
# 10
# >>> 5*3
# 15
# >>> 5*4
# 20
# >>> 5*5
# 25
# >>> 5*6
# 30
# >>> 5*7
# 35
# >>> 5*8
# 40
# >>> 5*9
# 45
# >>> 5*10
# 50


# using pyttsx3 is a python moduel
import pyttsx3
pyttsx3.speak("Fuck you All")


# Write a Python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# Print the contents of the current directory
contents = os.listdir("/home/muhammad-anas/Downloads")

for item in contents:
    print(item)
