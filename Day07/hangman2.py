import random 
from hangman_words import word_list
from hangman_art import stages

word_list = ["aardvark", "baboon", "camel"]

# 도전회수
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = "_"
for letter in chosen_word:
    placeholder += "_"
print(placeholder)

# while을 이용한 반복 처리 
game_over = False
correct_letters = []

while not game_over:
    print("****************<???>/6 번의 기회가 남았습니다.********************")
    guess = input("단에를 추측하세요: ").lower()
    
    # 이미 추측한 단어를 다시 추측한 경우라면 
    if guess in correct_letters:
        print(f"{guess}는 이미 추측한 단어 입니다.")

    display = ""

    # 이전 단어를 유지해야 함 - correct_letters = []
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("게임 실패!!")

    if '_' not in display:
        game_over = True
        print("당신이 이겼습니다.")

    print(stages[6-lives])