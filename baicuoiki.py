import random

word = ['python', 'coding', 'pycharm', 'apple', 'eye', ]
valid = 1
while valid == 1:
    pick: str = random.choice(word).upper()   # Chọn từ trong thư viện

    ans = []
    for i in range(len(pick)):
        ans.append('_')
    print("The word you have to guess is: ", *ans, sep='')
    tries = 0  # số lần sai trong khoảng cho phép

    while tries < 10 and '_' in ans:
        dem_so = 0  # số kí tự đúng trong từ đã cho
        letter = input("The letter you choose is: ").upper()
        for i in range(len(pick)):  # dò hết các kí tự của từ
            if letter == pick[i]:
                dem_so += 1      # đếm số lần đúng
                ans[i] = pick[i]      # thay thế vào kết quả
        if dem_so > 0:
            print("Right character! The word have ", dem_so, " ", letter)
            print(*ans, sep='')
        else:
            tries += 1
            print("Sorry, wrong character! You have ", 10 - tries, "times left")
        valid1 = int(input("Do you want to guess full word? Press 1 to guess: "))   # cần Nhi bổ sung TA
        if valid1 == 1:
            fullword = input("Guess the word: ").upper()
            if fullword == pick:
                break
    if tries == 10:
        print("You Failed! The answer is :", pick)
    else:
        print("Congratulations! ")
    valid = int(input('Do you want to play again? Press 1 to play or 0 to exit '))
print("Thank you for playing our game!")
