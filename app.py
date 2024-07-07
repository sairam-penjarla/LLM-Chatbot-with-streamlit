import streamlit as st
import streamlit.components.v1 as components
from main import chatbot

# The `EchoBotApp` class is a Python class that creates a simple chatbot application in Streamlit for
# echoing user input.
class EchoBotApp:
    def __init__(self):
        """
        The `__init__` function initializes an Echo Bot web page with chat history, custom styling, and
        user input handling.
        """
        
        self.ALIGNMENT_CSS_PATH = "./script/alignment.css"
        self.STYLE_CSS_PATH = "./script/style.css"
        self.SCROLL_JS_PATH = "./script/scroll.js"


        st.set_page_config(page_title="chatbot", page_icon=":robot_face:")
        self.initialize_chat_history()
        st.title("chatbot")
        self.load_js()
        self.add_custom_css()
        self.display_chat_history()
        self.bot = chatbot
        self.handle_user_input()

    
    def load_js(self):
        """
        The `load_js` function contains JavaScript code that scrolls multiple text areas to the bottom
        when executed.
        """
        with open(self.SCROLL_JS_PATH) as f:
            self.js = f"<script>{f.read()}</script>"
    
    def initialize_chat_history(self):
        """
        This Python function initializes a chat history in the session state if it does not already
        exist.
        """
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def add_custom_css(self):
        """
        The `add_custom_css` function adds custom CSS styles to adjust the alignment of chat messages in
        a Streamlit app.
        """
        with open(self.STYLE_CSS_PATH) as f:
            css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        with open(self.ALIGNMENT_CSS_PATH) as f:
            css = f.read()
            st.html(f"<style>{css}</style>")

    def get_avatar(self, role):
        """
        The function `get_avatar` returns an avatar emoji based on the role provided.
        
        :param role: The `role` parameter in the `get_avatar` function is used to determine the type of
        avatar to return based on the role specified. If the role is "user", the function returns the
        avatar for a user, and if the role is "assistant", it returns the avatar for an assistant
        :return: If the `role` parameter is "user", the function will return ":material/person:". If the
        `role` parameter is "assistant", the function will return ":material/robot_2:".
        """
        if role == "user":
            return ":material/person:"
        if role == "assistant":
            return ":material/robot_2:"
    
    def display_chat_history(self):
        """
        The function `display_chat_history` iterates through messages in the session state and displays
        them in a chat format with avatars and content.
        """
        for message in st.session_state.messages:
            avatar = self.get_avatar(message["role"])
            with st.chat_message(message["role"], avatar=avatar):
                st.html(f"<span class='chat-{message["role"]}'></span>")
                st.markdown(message["content"])

    def handle_user_input(self):
        """
        The function `handle_user_input` prompts the user for input, adds the user's message to the
        chat, generates a response, and adds the response to the chat.
        """
        if prompt := st.chat_input("Hi! How can I assist you today?"):
            self.add_message("user", prompt)
            response = self.generate_response(prompt)
            self.add_message("assistant", response)

    def add_message(self, role, content):
        """
        The function `add_message` adds a chat message with specified role and content to the session
        state messages list.
        
        :param role: Role refers to the specific role or identity of the user sending the message. It
        could be something like "user", "admin", "bot", etc., indicating who the sender of the message
        is
        :param content: The `content` parameter in the `add_message` function represents the message
        content that you want to add to the chat. This could be text, images, links, or any other type
        of content that you want to display in the chat message
        """
        avatar = self.get_avatar(role)
        with st.chat_message(role, avatar=avatar):
            st.html(f"<span class='chat-{role}'></span>")
            st.markdown(content)
            components.html(self.js)
        st.session_state.messages.append({"role": role, "content": content})

    def generate_response(self, prompt):
        """
        The function `generate_response` takes a prompt as input and returns a string that echoes the
        prompt.
        
        :param prompt: The `generate_response` function takes in two parameters: `self` and `prompt`.
        The `prompt` parameter is the input text that the function will echo back with the prefix "Echo:
        "
        :return: The `generate_response` method returns a string that echoes the input prompt. The
        returned string is formatted as "Echo: {prompt}".
        """
        return self.bot(prompt)

if __name__ == "__main__":
    app = EchoBotApp()
