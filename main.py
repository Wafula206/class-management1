import tkinter as tk
from tkinter import scrolledtext, messagebox
import datetime
import random
import json

# Sample student data
students = {
    "brian wafula": {"attendance": 90, "assignments": {"Math": "Submitted", "Science": "Pending"}},
    "malvo": {"attendance": 70, "assignments": {"Math": "Submitted", "Science": "Submitted"}},
}

schedule = {
    "monday": "Math, Science, Physical Education",
    "tuesday": "English, History, Chemistry",
    "wednesday": "Math, Art, Biology",
    "thursday": "Physics, Computer Science",
    "friday": "Sports, Club Activities",
}

assignments = {
    "Math": "Homework on linear motion due next week Monday.",
    "Science": "Project on the solar system due today midnight.",
}

# Chatbot Logic
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        return random.choice(["Hello! How can I assist you with class management today?",
                              "Hi! How can I help with your class tasks?"])

    # List All Students
    elif "list students" in user_input:
        student_names = ", ".join([name.title() for name in students])
        return f"Registered Students: {student_names}"

    # Attendance Management
    elif "attendance" in user_input:
        if "for" in user_input:
            name = user_input.split("for ")[1].strip()
            if name in students:
                return f"{name.title()} has {students[name]['attendance']}% attendance."
            else:
                return f"Student '{name}' not found."
        else:
            return "Please specify the student's name (e.g., 'attendance for Brian Wafula')."

    # Assignment Status
    elif "assignments" in user_input:
        if "for" in user_input:
            name = user_input.split("for ")[1].strip()
            if name in students:
                status = students[name]["assignments"]
                return f"{name.title()}'s assignments:\n" + "\n".join([f"{k}: {v}" for k, v in status.items()])
            else:
                return f"Student '{name}' not found."
        else:
            return "Please specify the student's name (e.g., 'assignments for Malvo')."

    # View All Assignments
    elif "all assignments" in user_input:
        return "Here are the current assignments:\n" + "\n".join([f"{k}: {v}" for k, v in assignments.items()])

    # Class Schedule
    elif "schedule" in user_input:
        if "for" in user_input:
            day = user_input.split("for ")[1].strip()
            if day in schedule:
                return f"Schedule for {day.title()}:\n{schedule[day]}"
            else:
                return "I couldn't find a schedule for that day."
        else:
            return "Please specify a day (e.g., 'schedule for Monday')."

    # Add New Student
    elif "add student" in user_input:
        try:
            name = user_input.split("add student ")[1].strip()
            if name not in students:
                students[name] = {"attendance": 0, "assignments": {}}
                return f"Student '{name.title()}' added successfully."
            else:
                return f"Student '{name}' already exists."
        except:
            return "Please specify the student's name."

    # Mark Attendance
    elif "mark attendance" in user_input:
        if "for" in user_input:
            name = user_input.split("for ")[1].strip()
            if name in students:
                students[name]["attendance"] += 1
                return f"Marked attendance for {name.title()}."
            else:
                return f"Student '{name}' not found."
        else:
            return "Please specify the student's name (e.g., 'mark attendance for Brian Wafula')."

    # Help / Available Commands
    elif user_input in ["help", "commands"]:
        return (
            "Available Commands:\n"
            "1. 'attendance for [student name]'\n"
            "2. 'assignments for [student name]'\n"
            "3. 'all assignments'\n"
            "4. 'schedule for [day]'\n"
            "5. 'add student [name]'\n"
            "6. 'mark attendance for [student name]'\n"
            "7. 'list students'\n"
            "8. 'exit' to quit the application."
        )

    # Exit
    elif user_input in ["exit", "quit"]:
        root.quit()
        return "Goodbye! Have a productive day."

    # Default Response
    else:
        return "I'm sorry, I don't understand that. Type 'help' to see available commands."


# GUI Setup
def send_message():
    user_input = user_entry.get()
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n")
    bot_response = chatbot_response(user_input)
    chat_window.insert(tk.END, f"Bot: {bot_response}\n\n")
    chat_window.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)


def clear_chat():
    chat_window.config(state=tk.NORMAL)
    chat_window.delete(1.0, tk.END)
    chat_window.config(state=tk.DISABLED)


# Initialize The Interface
root = tk.Tk()
root.title("CLASS MANAGEMENT SYSTEM for WAFULA and MALVO")

# Chat Window
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, state=tk.DISABLED)
chat_window.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# User Entry
user_entry = tk.Entry(root, width=50)
user_entry.grid(row=1, column=0, padx=10, pady=10)

# Send Button
send_button = tk.Button(root, text="Send", width=10, command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Clear Chat Button
clear_button = tk.Button(root, text="Clear Chat", width=10, command=clear_chat)
clear_button.grid(row=1, column=2, padx=10, pady=10)

# Run the GUI loop
root.mainloop()
