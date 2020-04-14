# Made with love by Nick Nyaumwe (https://nick.co.zw)

class Word():
    
    def __init__(self, str):
        self.str = str

    def length(self):
        total = 0

        for letter in self.str:
            total += 1
        
        return total
    
    # Split string into array
    def split(self, type=0, key=" "):
        str_list = []
        position = 0

        # SPlit every letter of the string into an array
        if type == 0:
            for letter in self.str:
                str_list.append(letter)

        # Split each individual word into an instance of an array
        if type == 1:
            word = Word(self.str)
            current_word = []
            for letter in self.str:
                if letter == key and self.str[position - 1] != key:
                    str_list.append("".join(current_word))
                    current_word = []
                else:
                    current_word.append(letter)
                    if position == word.length() - 1:
                        str_list.append("".join(current_word))

                position += 1

        return str_list

    # Reverses the string
    def reverse(self):
        # Iterative
        
        reversed_str = []
        str_len = len(self.str) - 1
        position = 0
        
        for letter in self.str:
            reversed_str.append(self.str[str_len - position])
            position += 1

        return "".join(reversed_str)
        
        # Recursive

        # if self.str == "":
        #     return self.str
        # else:
        #     return Word(self.str[1:]).reverse() + self.str[0]

    # Delete every matching instance of the target arguement
    def delete(self, target):
        letters = Word(self.str).split()
        target = str(target)
        position = 0

        for letter in letters:
            if letter == target:
                letters[position] = ""

            position += 1

        return "".join(letters)

    # Checks if string is a palindrome
    def is_palindrome(self):
        result = False

        if Word(self.str).reverse() == self.str:
            result = True

        return result

    # Capitalize every instance of the target within the string
    def capitalize_letter(self, target, type=0):
        letters = [["a","A"],
                    ["b","B"],
                    ["c","C"],
                    ["d","D"],
                    ["e","E"],
                    ["f","F"],
                    ["g","G"],
                    ["h","H"],
                    ["i","I"],
                    ["j","J"],
                    ["k","K"],
                    ["l","L"],
                    ["m","M"],
                    ["n","N"],
                    ["o","O"],
                    ["p","P"],
                    ["q","Q"],
                    ["r","R"],
                    ["s","S"],
                    ["t","T"],
                    ["u","U"],
                    ["v","V"],
                    ["w","W"],
                    ["x","X"],
                    ["y","Y"],
                    ["z","Z"]]
                    
        
        if type == 0:
            capital_letter = ""
            position = 0
            string_list = Word(self.str).split()

            for letter in letters:
                if letter[0] == target:
                    capital_letter = letter[1]

            for letter in string_list:
                if letter == target:
                    string_list[position] = capital_letter
                position += 1

            return "".join(string_list)
                    

        if type == 1:
            for letter in letters:
                if letter[0] == target:
                    return letter[1]

    def capitalize(self, type=0):
        word = Word(self.str)
        letters = word.split()
        position = 0

        # Capitalize first letter only
        if type == 0:
            return word.capitalize_letter(self.str[0], 1) + self.str[1:]

        # Capitalize every first letter of each word
        if type == 1:

            for letter in letters:
                if position == 0:
                    letters[0] = word.capitalize_letter(letter, 1)

                if position > 0 and letters[position - 1] == ' ':
                    letters[position] = word.capitalize_letter(letter, 1)

                position += 1
            return "".join(letters)

        # Capitalize all letters
        if type == 2:
            
            for letter in letters:
                if letter != ' ':
                    letters[position] = word.capitalize_letter(letter, 1)
                position += 1
            
            return "".join(letters)

    def compare(self, default_text=""):
        if default_text != "":
            score = 0
            position = 0
            total = 0
            if Word(self.str).length() >= Word(default_text).length():
                target = Word(self.str).split(1)
                default_text = Word(default_text).split(1)
            else:
                target = Word(default_text).split(1)
                default_text = Word(self.str).split(1)

            for string in default_text:
                if target[position].lower() == string.lower():
                    total += 1
                else: 
                    total_letters = 0
                    letter_position = 0
                    letters_list = Word(target[position].lower()).split()
                    for letter in letters_list:
                        if letter == Word(string.lower()).split()[letter_position]:
                            total_letters += 1
                    letter_position += 1

                    total += total_letters/len(letters_list)
                

                position += 1

            score = round(total/len(target) * 100, 1)

            if ".0" in str(score):
                score = str(score).replace(".0", "")

            return score
        else:
            return None
