import customtkinter as ctk

# Define the application class inheriting from CTk
class ChatApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the window title and geometry
        self.title("Chat Window")
        self.geometry("400x500")

        # Create a frame to hold the chat area
        self.chat_frame = ctk.CTkFrame(master=self)
        self.chat_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Create a textbox widget to display the chat conversation
        self.chat_area = ctk.CTkTextbox(master=self.chat_frame, width=380, height=350)
        self.chat_area.pack(pady=10, padx=10, fill="both", expand=True)
        self.chat_area.configure(state="disabled")  # Disable editing by users

        # Create a frame for input area and send button
        self.input_frame = ctk.CTkFrame(master=self, height=150, fg_color=self.cget("bg"))  # Set the frame color same as the window
        self.input_frame.pack(pady=10, padx=20, fill="x")

        # Entry box for user input
        self.input_box = ctk.CTkEntry(master=self.input_frame, placeholder_text="Type your message here", height=40, width=200)
        self.input_box.pack(side="left", pady=30, padx=(200, 10), fill="x")  # Adjust padding for better height

        # Create a send button with fixed width
        self.send_button = ctk.CTkButton(master=self.input_frame, text="Send", command=self.send_message, height=40, width=80)
        self.send_button.pack(side="left", padx=10, pady=10)  # Adjust padding to match input box

        # Bind the window resize event to dynamically resize the input box
        self.bind("<Configure>", self.resize_input_box)

        # Configure the tags for colors
        self.chat_area.tag_config("user", foreground="#A020F0")  # Color for user messages
        self.chat_area.tag_config("bot", foreground="#008000")   # Color for bot messages

    # Function to handle sending messages
    def send_message(self):
        # Get the message from the input box
        message = self.input_box.get()

        # If message is not empty, display it in the chat area
        if message.strip():
            self.display_message(message, is_user=True)
            self.display_message("Hello! I am Kairos.", is_user=False)

        # Clear the input box
        self.input_box.delete(0, "end")

    # Function to display the message in the chat area
    def display_message(self, message, is_user):
        # Enable editing to insert the message
        self.chat_area.configure(state="normal")

        # Determine the prefix for user and bot messages
        prefix = "You: " if is_user else "Bot: "
        formatted_message = f"{prefix}{message}"

        # Insert the message at the end of the chat area
        self.chat_area.insert("end", formatted_message + "\n")

        # Add extra gap after user message
        if is_user:
            self.chat_area.insert("end", "\n")  # Extra line for spacing after user message

        # Color the text based on the sender
        if is_user:
            self.chat_area.tag_add("user", "end-1c linestart", "end-1c lineend")
        else:
            self.chat_area.insert("end", "\n")  # Extra line for spacing after user message
            self.chat_area.tag_add("bot", "end-1c linestart", "end-1c lineend")

        # Scroll to the end of the chat area
        self.chat_area.yview("end")

        # Disable editing again after inserting the message
        self.chat_area.configure(state="disabled")

    # Function to dynamically resize the input box to half the window width
    def resize_input_box(self, event):
        new_width = int(self.winfo_width() * 0.5)  # Adjust width to be 50% of the window width
        if new_width > 200:  # Ensure minimum width to avoid shrinking too much
            self.input_box.configure(width=new_width)

# Initialize and run the chat app
if __name__ == "__main__":
    app = ChatApp()
    app.mainloop()
