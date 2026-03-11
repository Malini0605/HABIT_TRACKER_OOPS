from datetime import date

class Reminder:
    def __init__(self, reminder_id, time):
        self.reminder_id = reminder_id
        self.time = time

    def display(self):
        print(f"Reminder ID: {self.reminder_id}, Time: {self.time}")


class HabitProgress:
    def __init__(self):
        self.streak = 0
        self.last_completed = None

    def update_progress(self):
        today = date.today()

        if self.last_completed == today:
            print("Habit already completed today.")
            return False

        if self.last_completed:
            gap = (today - self.last_completed).days
            if gap == 1:
                self.streak += 1
            else:
                self.streak = 1
        else:
            self.streak = 1

        self.last_completed = today
        print(f"Habit completed! Current streak: {self.streak}")
        return True


class Habit:
    def __init__(self, habit_id, name, category, frequency):
        self.habit_id = habit_id
        self.name = name
        self.category = category
        self.frequency = frequency
        self.reminders = []
        self.progress = HabitProgress()

    def add_reminder(self, reminder_id, time):
        reminder = Reminder(reminder_id, time)
        self.reminders.append(reminder)
        print("Reminder added.")

    def complete_habit(self):
        return self.progress.update_progress()

    def display(self):
        print("\nHabit ID:", self.habit_id)
        print("Name:", self.name)
        print("Category:", self.category)
        print("Frequency:", self.frequency)
        print("Current Streak:", self.progress.streak)


class Journal:
    def __init__(self, mood, note):
        self.mood = mood
        self.note = note
        self.date = date.today()

    def display(self):
        print(self.date, "| Mood:", self.mood, "| Note:", self.note)


class Reward:
    def __init__(self, badge):
        self.badge = badge
        self.date = date.today()

    def display(self):
        print(self.date, "| Badge:", self.badge)


class CommunityPost:
    def __init__(self, post_id, content):
        self.post_id = post_id
        self.content = content
        self.date = date.today()

    def display(self):
        print(self.date, "|", self.content)


class User:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.habits = []
        self.journals = []
        self.rewards = []
        self.posts = []

    def add_habit(self, name, category, frequency):
        habit_id = len(self.habits) + 1
        habit = Habit(habit_id, name, category, frequency)
        self.habits.append(habit)
        print("Habit added successfully.")

    def show_habits(self):
        if not self.habits:
            print("No habits found.")
        for h in self.habits:
            h.display()

    def complete_habit(self, habit_id):
        for h in self.habits:
            if h.habit_id == habit_id:
                success = h.complete_habit()

                if success:
                    streak = h.progress.streak
                    if streak == 3:
                        self.add_reward("Beginner Badge")
                    elif streak == 7:
                        self.add_reward("Consistency Badge")
                    elif streak == 30:
                        self.add_reward("Champion Badge")

                return
        print("Habit not found.")

    def add_journal(self, mood, note):
        self.journals.append(Journal(mood, note))
        print("Journal entry added.")

    def show_journals(self):
        if not self.journals:
            print("No journal entries.")
        for j in self.journals:
            j.display()

    def add_reward(self, badge):
        reward = Reward(badge)
        self.rewards.append(reward)
        print("Reward unlocked:", badge)

    def show_rewards(self):
        if not self.rewards:
            print("No rewards yet.")
        for r in self.rewards:
            r.display()

    def add_post(self, post_id, content):
        self.posts.append(CommunityPost(post_id, content))
        print("Community post created.")

    def show_posts(self):
        if not self.posts:
            print("No community posts.")
        for p in self.posts:
            p.display()

# Application Controller

class HabitTrackerApp:
    def __init__(self):
        self.users = []
        self.current_user = None

    def register_user(self):
        uid = len(self.users) + 1
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")

        user = User(uid, username, email, password)
        self.users.append(user)

        print("User registered successfully.")

    def login(self):
        email = input("Email: ")
        password = input("Password: ")

        for user in self.users:
            if user.email == email and user.password == password:
                self.current_user = user
                print("Login successful!")
                return

        print("Invalid email or password.")

    def logout(self):
        self.current_user = None
        print("Logged out.")

# Main Program

app = HabitTrackerApp()

while True:

    if app.current_user is None:

        print("\n==== MAIN MENU ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choice: ")

        if choice == "1":
            app.register_user()

        elif choice == "2":
            app.login()

        elif choice == "3":
            break

    else:

        user = app.current_user

        print("\n==== HABIT MENU ====")
        print("1. Add Habit")
        print("2. View Habits")
        print("3. Complete Habit")
        print("4. Add Journal")
        print("5. View Journals")
        print("6. View Rewards")
        print("7. Create Community Post")
        print("8. View Posts")
        print("9. Logout")

        choice = input("Choice: ")

        if choice == "1":
            name = input("Habit Name: ")
            category = input("Category: ")
            freq = input("Frequency: ")
            user.add_habit(name, category, freq)

        elif choice == "2":
            user.show_habits()

        elif choice == "3":
            hid = int(input("Enter Habit ID: "))
            user.complete_habit(hid)

        elif choice == "4":
            mood = input("Mood: ")
            note = input("Journal note: ")
            user.add_journal(mood, note)

        elif choice == "5":
            user.show_journals()

        elif choice == "6":
            user.show_rewards()

        elif choice == "7":
            pid = len(user.posts) + 1
            content = input("Post content: ")
            user.add_post(pid, content)

        elif choice == "8":
            user.show_posts()

        elif choice == "9":
            app.logout()