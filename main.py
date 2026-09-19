
class User:

    def __init__(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
    
class Message:  

    def __init__(self, sender, message):
        self.sender = sender
        self.message = message

class ChatRoom:
    def __init__(self, chatroom_name):
        self.chatroom_name = chatroom_name
        self.users=[]
        self.messages=[]   
        self.activity_log=[]
         
    def join_user(self, u):
        self.users.append(u)
        self.activity_log.append(f"{u.user_name} with user_id {u.user_id} is joining the {self.chatroom_name} chatroom.")

    def leave_user(self, u):
        self.users.remove(u)
        self.activity_log.append(f"{u.user_name} with user_id {u.user_id} is leaving the {self.chatroom_name} chatroom.")
    
    def send_messages(self, sender, message):
        m = Message(sender, message)
        self.messages.append(m)
        self.activity_log.append(f"{m.sender.user_name} sending the message in the chatroom.")
    
    def show_activity(self):
        for h in self.activity_log:
         print(h)
      
    def show_message_history(self):
       for msg in self.messages:
        print(f"{msg.sender.user_name} :  {msg.message}")

print("*** SMALL CHATROOM ***")
name=input("Enter your chatroom name : ")
room = ChatRoom(name)
n=int(input("Enter the number of members you want to join in chatroom : "))
for i in range(n):
    while True:
      username = input(f"Enter {i+1} username: ")

      if username:
        break

    while True:
      userid = input("Userid: ")

      if userid:
        break

    user=User(username, userid)
    room.join_user(user)

while True:

    print("\n1. Send message")
    print("2. Leave group")
    print("3. Show activity log")
    print("4. Show message history")
    print("5. Show members")
    print("6. Exit chatroom")

    choice = int(input("Enter your choice : "))

    if choice == 1:

        username = input("Enter your name : ")

        current_user = None

        for u in room.users:
            if u.user_name == username:
                current_user = u
                break

        if current_user is None:
            print("User not found.")
            continue

        message = input("Enter your message : ")

        room.send_messages(current_user, message)

    elif choice == 2:

        username = input("Enter your name : ")

        current_user = None

        for u in room.users:
            if u.user_name == username:
                current_user = u
                break

        if current_user is None:
            print("User not found.")
            continue

        room.leave_user(current_user)


    elif choice == 3:

        room.show_activity()

    elif choice == 4:

        room.show_message_history()

    elif choice == 5:

        for u in room.users:
            print(u.user_name, "-", u.user_id)

    elif choice == 6:

        print("Exting the chatroom .......")
        break

    else:

        print("invalid choice")










