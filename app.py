import streamlit as st
import random

st.set_page_config(page_title="🎮 Mini Game Arcade", layout="wide")
st.title("🎯 Mini Game Arcade")
st.write("Choose a game and start playing! All games are rule-based, no AI required 😉")

# ----------------- Game Selection -----------------
games = [
    "Rock Paper Scissors",
    "Guess the Number",
    "Word Scramble",
    "Emoji Quiz",
    "Math Quiz",
    "Coin Toss",
    "Hangman",
    "Trivia Quiz",
    "Dice Roll",
    "Score Tracker"
]

choice = st.selectbox("Select a Game:", games)

# ----------------- 1. Rock Paper Scissors -----------------
if choice == "Rock Paper Scissors":
    st.subheader("✊✋✌ Rock Paper Scissors")
    user_choice = st.radio("Choose:", ["Rock", "Paper", "Scissors"])
    if st.button("Play"):
        computer = random.choice(["Rock", "Paper", "Scissors"])
        st.write(f"Computer chose: **{computer}**")
        if user_choice == computer:
            st.info("It's a draw!")
        elif (user_choice == "Rock" and computer == "Scissors") or \
             (user_choice == "Paper" and computer == "Rock") or \
             (user_choice == "Scissors" and computer == "Paper"):
            st.success("You win! 🎉")
        else:
            st.error("You lose 😢")

# ----------------- 2. Guess the Number -----------------
elif choice == "Guess the Number":
    st.subheader("🔢 Guess the Number (1-20)")
    number = random.randint(1, 20)
    guess = st.number_input("Enter your guess:", 1, 20, 1)
    if st.button("Check"):
        if guess == number:
            st.success("Correct! 🎉")
        else:
            st.warning(f"Wrong! The number was {number}")

# ----------------- 3. Word Scramble -----------------
elif choice == "Word Scramble":
    st.subheader("🔤 Word Scramble")
    words = ["python", "streamlit", "arcade", "engineer", "science", "laptop"]
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    st.write(f"Scrambled Word: **{scrambled}**")
    answer = st.text_input("Your guess:")
    if st.button("Submit"):
        if answer.lower() == word:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The word was **{word}**")

# ----------------- 4. Emoji Quiz -----------------
elif choice == "Emoji Quiz":
    st.subheader("😀 Emoji Quiz")
    quizzes = {
        "🎬🍿": "movie",
        "⚽🏆": "football",
        "🎶🎤": "music",
        "🍕🥤": "food"
    }
    emoji, ans = random.choice(list(quizzes.items()))
    st.write(f"Guess the word for: {emoji}")
    guess = st.text_input("Your Answer:")
    if st.button("Guess"):
        if guess.lower() == ans:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! Answer was **{ans}**")

# ----------------- 5. Math Quiz -----------------
elif choice == "Math Quiz":
    st.subheader("➗ Math Quiz")
    a, b = random.randint(1, 10), random.randint(1, 10)
    st.write(f"What is {a} + {b}?")
    ans = st.number_input("Your answer:", 0, 100, 0)
    if st.button("Check Answer"):
        if ans == a + b:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! Answer was {a+b}")

# ----------------- 6. Coin Toss -----------------
elif choice == "Coin Toss":
    st.subheader("🪙 Coin Toss")
    guess = st.radio("Choose:", ["Heads", "Tails"])
    if st.button("Flip"):
        result = random.choice(["Heads", "Tails"])
        st.write(f"Result: **{result}**")
        if guess == result:
            st.success("You guessed right!")
        else:
            st.error("You guessed wrong!")

# ----------------- 7. Hangman -----------------
elif choice == "Hangman":
    st.subheader("🪢 Hangman")
    word = random.choice(["apple", "banana", "cherry", "grapes"])
    hint = word[0] + "_"*(len(word)-2) + word[-1]
    st.write(f"Hint: {hint}")
    guess = st.text_input("Guess the word:")
    if st.button("Check Word"):
        if guess.lower() == word:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! The word was {word}")

# ----------------- 8. Trivia Quiz -----------------
elif choice == "Trivia Quiz":
    st.subheader("❓ Trivia Quiz")
    questions = {
        "What is the capital of France?": "paris",
        "Who developed Python?": "guido van rossum",
        "Which planet is known as the Red Planet?": "mars"
    }
    q, a = random.choice(list(questions.items()))
    st.write(q)
    ans = st.text_input("Your Answer:")
    if st.button("Check Trivia"):
        if ans.lower() == a:
            st.success("Correct! 🎉")
        else:
            st.error(f"Wrong! Correct answer: {a}")

# ----------------- 9. Dice Roll -----------------
elif choice == "Dice Roll":
    st.subheader("🎲 Dice Roll")
    if st.button("Roll Dice"):
        roll = random.randint(1, 6)
        st.write(f"You rolled: **{roll}**")

# ----------------- 10. Score Tracker -----------------
elif choice == "Score Tracker":
    st.subheader("📊 Score Tracker")
    if "score" not in st.session_state:
        st.session_state.score = 0
    add = st.button("Increase Score")
    sub = st.button("Decrease Score")
    reset = st.button("Reset Score")

    if add:
        st.session_state.score += 1
    if sub:
        st.session_state.score -= 1
    if reset:
        st.session_state.score = 0

    st.success(f"Your current score: {st.session_state.score}")
