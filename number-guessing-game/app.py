import streamlit as st
import random

def main():
    st.set_page_config(page_title="Number Guessing Game", page_icon="🎯", layout="centered")
    st.title("🎯 Number Guessing Game")
    
    # Initialize session state variables
    if 'target' not in st.session_state:
        st.session_state.target = random.randint(1, 100)
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'message' not in st.session_state:
        st.session_state.message = ""
    if 'game_over' not in st.session_state:
        st.session_state.game_over = False
    if 'max_attempts' not in st.session_state:
        st.session_state.max_attempts = 10  # Limit attempts to 10
    
    st.markdown("### Try to guess the number between 1 and 100!")
    
    # User input
    guess_input = st.text_input("Enter your guess:", placeholder="Type a number between 1 and 100", key="guess")
    
    if guess_input.isdigit():
        guess = int(guess_input)
    else:
        guess = None
        if guess_input:
            st.error("🚫 Please enter a valid number!")
    
    # Submit button
    if st.button("Submit Guess", use_container_width=True, disabled=st.session_state.game_over or guess is None):
        if guess is not None:
            st.session_state.attempts += 1
            if guess < st.session_state.target:
                st.session_state.message = "⬆️ Too low! Try again."
                if abs(guess - st.session_state.target) <= 5:
                    st.session_state.message += " (You're very close!)"
            elif guess > st.session_state.target:
                st.session_state.message = "⬇️ Too high! Try again."
                if abs(guess - st.session_state.target) <= 5:
                    st.session_state.message += " (You're very close!)"
            else:
                st.session_state.message = f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts."
                st.session_state.game_over = True
                st.balloons()
            
            # Check if attempts exceeded
            if st.session_state.attempts >= st.session_state.max_attempts and not st.session_state.game_over:
                st.session_state.message = f"❌ Game Over! The correct number was {st.session_state.target}."
                st.session_state.game_over = True
    
    # Display message
    if "Congratulations" in st.session_state.message:
        st.success(st.session_state.message)
    elif "Game Over" in st.session_state.message:
        st.error(st.session_state.message)
    else:
        st.warning(st.session_state.message)
    
    # Restart game
    if st.button("Restart Game", use_container_width=True):
        st.session_state.target = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.message = ""
        st.session_state.game_over = False
        st.rerun()
    
    # Display attempts counter
    st.markdown(f"**Attempts:** {st.session_state.attempts} / {st.session_state.max_attempts}")
    
    # Footer
    st.markdown("---")
    st.markdown("Made with ❤️ using Streamlit")

if __name__ == "__main__":
    main()