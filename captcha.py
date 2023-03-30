import streamlit as st
import random

def generate_captcha():
    captcha = ""
    for i in range(6):
        captcha += str(random.randint(1,9))
    return captcha

def contact_form():
    if "captcha" not in st.session_state:
        st.session_state.captcha = generate_captcha()
    st.write("# Contact Form")
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    captcha_input = st.text_input("Enter the captcha shown below")
    st.write(f"Captcha: {st.session_state.captcha}")
    if captcha_input == st.session_state.captcha and name and email and message:
        # code to send email goes here
        st.success("Your message has been sent!")
    elif captcha_input == st.session_state.captcha:
        st.warning("Please fill in all the fields")
    else:
      if not st.empty():
        st.error("Incorrect captcha. Please try again.")
        st.session_state.captcha = generate_captcha()
      
        

    # Generate new captcha button
    if st.button("Generate new captcha"):
        st.session_state.captcha = generate_captcha()

    # Submit button with unique key
    if st.button("Submit", key="submit_button") and captcha_input == st.session_state.captcha:
        # code to submit form goes here
        st.success("Your message has been sent!")

if __name__ == '__main__':
    contact_form()
