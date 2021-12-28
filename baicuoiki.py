import random

with open('word.txt', 'r') as f:
    words = f.readlines()

valid = '1'


def space():
    blank = []
    for i in range(len(pick)):
        blank.append('_')  # khoảng cách tương ứng với số kí tự
    return blank


def guess():
    char = input("\nChoose a letter: ").upper()
    while (char.isalpha() is False) or (len(char) > 1): # kiểm tra hợp lệ
        char = input("Invalid. Please choose a letter: ").upper()
    while char in lst:          # kiểm tra xem đã đoán chưa
        char = input("You have guessed this one. Please choose another letter: ").upper()
    return char


def full():
    x = input("\nDo you want to guess the full word? Press 1 (Yes) or 0 (No): ")
    while x != '1' and x != '0':
        x = input("Invalid. Please try again: ")
    return x


print("\nWelcome to our GUESSING THE WORD game")
name = input("What's your name: ")
print("Ok, " + name + ". Let's start!")

while valid == '1':
    print("-"*50)   # trang trí
    pick: str = random.choice(words)[:-1].upper()   # Chọn từ trong thư viện

    ans = space()
    tries = 0  # số lần sai trong khoảng cho phép

    print("The word you have to guess has", len(pick), "letters")

    lst = []
    while tries < 10:
        count = 0  # số kí tự đúng trong từ đã cho
        print("Word: ", *ans, sep='')
        letter = guess()
        lst.append(letter)

        for i in range(len(pick)):  # dò hết các kí tự của từ
            if letter == pick[i]:
                count += 1      # đếm số lần đúng
                ans[i] = pick[i]      # thay thế vào kết quả

        if count > 0:
            print("Correct! The word has", count, "letter(s)", letter)
            print(*ans, sep='')
        else:
            tries += 1
            print("Sorry, wrong character! You have", 10 - tries, "time(s) left")

        # nếu đoán hết rồi thì không chạy cái này nữa
        if '_' in ans:
            if full() == '1':
                full_word = input("Guess the word: ").upper()
                while full_word.isalpha() is False:     # kiểm tra xem có nhập toàn ký tự hay không
                    full_word = input("Invalid. Please type a WORD: ").upper()
                if full_word == pick:
                    break
                else:
                    tries += 1
                    print("Sorry, wrong guess! You have", 10 - tries, "time(s) left")
            print("\nLetters you have guessed:", *lst, sep=' ')
        else:
            break

    if tries == 10:
        print("\nYou lost! The word is:", pick)
    else:
        print("\nCongratulation! The word is:", pick)

    valid = input('\nDo you want to play again? Press 1 to play or 0 to exit: ')
    while valid != '1' and valid != '0':
        valid = input('Invalid. Do you want to play again? Press 1 to play or 0 to exit: ')

print("-"*50)   # trang trí
print("See you later, " + name + ". Thank you for playing our game!")
