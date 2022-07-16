"""
Palindrome class realization.
"""

from Lab12.palindrome.Stack.arraystack import ArrayStack  # or from linkedstack import LinkedStack
import re


class Palindrome:
    """
    Read words from files and write to a file words that are palindromes
    palindrome = Palindrome()
    palindrome.find_palindromes("base.lst", "palindrome_uk.txt")
    palindrome.find_palindromes("words.txt", "palindrome_en.txt")
    """

    def __init__(self):
        self.stack = ArrayStack()
        self.palindrome_list = []

    def _palidrome_check(self, word):
        """
        Check if word is palindrome.
        """
        self.stack = ArrayStack()
        for i in range(len(word)):
            self.stack.push(word[i])
        for i in range(len(word)):
            if self.stack.pop() != word[i]:
                return False
        if not re.search(r"[а-яА-Яієґїa-zA-z']{2,}", word):
            return False
        return True

    def _read_file(self, file_name):
        """
        Read words from file.
        """
        with open(file_name, 'r', encoding='utf-8') as file:
            lines = file.read()
            if lines.find('ж') != -1:
                wordlist = re.findall(r"[а-яА-Яієґї'-]{2,}", lines)
            else:
                wordlist = lines.split('\n')
        return wordlist

    def find_palindromes(self, file_name, output_file_name):
        """
        Read words from file and write to a file words that are palindromes.
        """
        wordlist = self._read_file(file_name)
        for word in wordlist:
            if self._palidrome_check(word):
                self.palindrome_list.append(word)
        self._write_to_file(output_file_name, self.palindrome_list)

    def _write_to_file(self, filepath, words):
        """
        Write words to file.
        """
        with open(filepath, 'w', encoding='utf-8') as file:
            for word in words:
                file.write(word + '\n')
        self.palindrome_list = []


if __name__ == '__main__':
    palindrome = Palindrome()
    palindrome.find_palindromes("ukr words.lst", "palindrome_uk.txt")
    palindrome.find_palindromes("eng words.txt", "palindrome_en.txt")
