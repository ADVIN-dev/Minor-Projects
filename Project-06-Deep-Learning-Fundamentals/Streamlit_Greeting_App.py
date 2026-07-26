import streamlit as st

st.set_page_config(
    page_title="Greeting App",
    layout="centered"
)

st.title("Greeting App")
st.write("Fill in the details below and click **Show Message** to get your personalized greeting!")
st.divider()

st.subheader("Tell us about yourself")

name = st.text_input("What is your name?")

mood = st.selectbox(
    "How are you feeling today?",
    ["Happy", "Sad", "Excited", "Tired", "Confused"]
)

level = st.slider("Rate your learning interest level", min_value=1, max_value=10, value=5)

if level <= 3:
    st.caption("Low interest — that's okay, take it easy!")
elif level <= 6:
    st.caption("Moderate interest — keep going!")
else:
    st.caption("High interest — you're on fire!")

st.divider()

if st.button("Show Message", use_container_width=True):

    if name.strip() == "":
        st.warning("Please enter your name first!")

    else:
        st.success(f"Hello, **{name}**! Welcome to the Greeting App")

        st.subheader("Mood Response")

        if "Happy" in mood:
            st.success("Great to hear! Keep that positive energy going!")
            st.balloons()

        elif "Excited" in mood:
            st.success("Awesome! Channel that excitement into learning!")
            st.balloons()

        elif "Tired" in mood:
            st.info("No worries! Take a short break and come back stronger.")

        elif "Sad" in mood:
            st.warning("I'm here to cheer you up! Things will get better")

        else:
            st.info("Don't worry — confusion means you're learning something new!")

        st.subheader("Your Learning Interest")
        st.write(f"You rated your interest level as **{level}/10**")

        st.progress(level / 10)

        if level >= 8:
            st.success("Amazing dedication! You're going to go far!")
        elif level >= 5:
            st.info("Good effort! A little more push and you'll get there.")
        else:
            st.warning("Try to find what excites you about learning — it helps!")