# string_manipulation
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
  
3. reverse - reverses a strng

  Example: Word("hello world").reverse()
  output: dlrow olleh
  
4. delete - deletes all matched instances of the target string
  
  Example: Word("hello world").delete('h')
  output: ello world
  
5. capitalize letter - 
