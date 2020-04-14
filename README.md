# String Manipulation
String Manipulation library for Python

This is a basic String Manipulation library I wrote for fun.

Here are the functions included in the library:

1. length - return the length of a string

  Example: Word("hello world").length()
  output: 11

2. split - splits a string into either an array of letters or words depending on your specification.

  Example (Split string into individual letters):
  Word("hello world").split()
  output: ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']


  Example (Split string into words):
  Word("hello world").split(1)
  outout: ['hello', 'world']

  Example (Split string using custom key):
  Word("hello,world").split(1, ",")
  output: ['hello', 'world']
  
3. reverse - reverses a strng.

  Example: Word("hello world").reverse()
  output: dlrow olleh
  
4. delete - deletes all matched instances of the target string.
  
  Example: Word("hello world").delete('h')
  output: ello world
  
5. capitalize letter - capitalizes all instances of a the target letter of a string returns a capital letter only for the specified target.

  Example (Capitalize all matching instances of target letter):
  Word("hello world").capitalize_letter('o')
  output: hellO wOrld

  Example (Return capital letter of target only):
  Word("hello world").capitalize_letter('h', 1)
  output: H

6. capitalize - capitalizes string.

  Example (Capitalizes first letter only):
  Word("hello world").capitalize()
  output: Hello world

  Example (Capitalizes first letter of each word):
  Word("hello world").capitalize(1)
  output: Hello World
  
  Example: (Capitalizes all letters)
  Word("hello world").capitalize(2)
  output: HELLO WORLD

7. compare - returns the percentage by which two strings match.

  Example: Word("hello world").compare("hello")
  output: 50
