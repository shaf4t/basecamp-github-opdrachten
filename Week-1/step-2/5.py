#Write down the complete alphabet in a variable. Split it halfway over two different variables. Join them back together in the wrong order and print it.

alphabet = "abcdefghijklmnopqrstuvwxyz"
half = len(alphabet) // 2
first_half = alphabet[:half]
second_half = alphabet[half:]
print(second_half + first_half)