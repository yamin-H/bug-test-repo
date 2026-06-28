def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def capitalize_words(s):
    words = s.split(" ")
    result = []
    for word in words:
        result.append(word[0].upper() + word[1:])  # bug: crashes on empty string
    return " ".join(result)

def truncate(s, max_length):
    if len(s) > max_length:
        return s[:max_length - 3] + "..."  # bug: wrong, should be max_length not max_length-3
    return s
