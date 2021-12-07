import random
name=input("What's your name") 
print("Welcome ",name," This is Hangman game")
word = ['python', 'coding', 'pycharm', 'apple', 'eye', ]
valid = 1

while valid == 1:
    pick: str = random.choice(word).upper()   # Chọn từ trong thư viện

    ans = []
    for i in range(len(pick)):
        ans.append('_')     # khoảng cách tương ứng với số kí tự
    print("The word you have to guess has", len(pick), "letters")
    tries = 0  # số lần sai trong khoảng cho phép

    lst = []
    while tries < 10:
        count = 0  # số kí tự đúng trong từ đã cho
        print("Word: ", *ans, sep='')
        letter = input("\nChoose a letter: ").upper()
        while letter in lst:    # kiểm tra xem đã đoán chưa
            letter = input("You have guessed this one. Please choose another letter: ").upper()
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

        if '_' in ans:  # nếu đoán hết rồi thì không chạy cái này nữa
            valid1 = input("\nDo you want to guess the full word? Press 1 (Yes) or 0 (No): ")
            while valid1 != '1' and valid1 != '0':
                valid1 = input("Wrong input. Please try again: ")
            if valid1 == '1':
                fullword = input("Guess the word: ").upper()
                if fullword == pick:
                    break
                else:
                    tries += 1
                    print("Sorry, wrong guess! You have", 10 - tries, "time(s) left")
            print("\nLetters you have guessed:", *lst, sep=' ')
        else:
            break

    if tries == 10:
        print("\nYou lost! The answer is:", pick)
    else:
        print("\nCongratulations! The word is:", pick)

    valid = int(input('\nDo you want to play again? Press 1 to play or 0 to exit: '))
    while valid != 1 and valid != 0:
        valid = int(input('Invalid. Do you want to play again? Press 1 to play or 0 to exit: '))

print("\nThank",name," for playing our game!")
