import json
import os
from datetime import datetime

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(CURR_DIR, "project_data.json")

project_data = {}

def save_data():
    with open(DATA, "w", encoding="utf-8") as file:
        # json.dump is cleaner than file.write(json.dumps(...))
        json.dump(project_data, file, ensure_ascii=False, indent=4)
    
        
def load_data():
    # Access the global variable so changes persist
    global project_data
    
    # Check if the file exists first to prevent a Crash on the very first run
    if os.path.exists(DATA):
        try:
            with open(DATA, "r", encoding="utf-8") as file:
                project_data = json.load(file)
                print("Data loaded successfully.")
        except json.JSONDecodeError:
            print("JSON file is empty or corrupted")
            project_data={}
    else:
        print("No previous data found. Starting fresh.")
        project_data = {}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def print_error(msg):
    print(f"\n❌ Error: {msg}")

def print_success(msg):
    print(f"\n✅ {msg}")

# 1. Load the data
load_data()
print("Current Data:", project_data)


#Nill implementing main dash bord

def print_header():
    print("\n" + "=" * 50)
    print(" " * 19 + "SOCIAL MEDIA")
    print("=" * 50)


def print_menu():
    print('''
Choose an option:

[1] Login
[2] Resister
[3] Exit
''')



def login_dashbord():
    print("\n"+"="*50)
    print(" "*15+"Varify Login")
    print("="*50)
    global username1
    username1=input("Enter your username= ").strip().lower()
        
    while True:

        if "users" in project_data:
            if username1 in project_data["users"]:
                print_success("username varify succesfull")
                break
                
            else :
                print_error("username not exist pless recheck username or creat a account")
                username1=input("Enter your username again= ").strip().lower()
                
                
        else:
                print_error("creat account first")
                input("\nPress Enter to continue... ")
                clear_screen()
                app()
                break
                
                
    while True:
        check_password=input("Enter your password= ").strip()

        if check_password == project_data["users"][username1]["password"]:
            print_success("passeord varifyed succesfull")
            input("\nPress Enter to continu... ")
            clear_screen()
            print("\n"+"="*50)
            print(" "*15 + f"Loged to =  {username1}     ")
            print("="*50)
            
            print('''
    Choose an option:
        
[1] View Feed
[2] View Profile
[3] Creat a Post
[4] Discover User
[5] Recommendation
[6] Logout
    ''')

            logic_userinterface()
            break
            
        else:
            print_error("password do not mach retry")



def create_post(username1):
    clear_screen()
    print("=== CREATE POST ===")

    post_text = input("Write your post: ").strip()
    
    if "posts" not in project_data:
        project_data["posts"]={}
        
    if username1 not in project_data["posts"]:
        project_data["posts"][username1]={}

    post_id = len(project_data["posts"][username1]) + 1
    current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")
    
    if "posts" in project_data:
        project_data["posts"][username1][str(post_id)]={
        "username":username1,
        "post_id":post_id,
        "content":post_text,
        "datetime":current_time,
        "Likes":0,
        "Liker list":{}
        }
  

    save_data()
    print_success("Post created successfully!")


def view_posts():
    print("=== ALL POSTS ===")
    
    if "posts" not in project_data:
        print_error("No posts yet.")
        return
    else:
        if username1 not in project_data["posts"]:
            print("No posts yet.")
            return
        
        for post in project_data["posts"][username1].values():
            print("-" * 40)
            print(f"Post ID : {post['post_id']}")
            print(f"User    : @{post['username']}")
            print(f"Date    : {post['datetime']}")
            print(f"Post    : {post['content']}")
            print(f"like    : {post['Likes']}")
            print('''
        [1] Like
        [2] Unlike
''')
            while True:
                user_input=input("Enter Your choise:")
                if user_input=="1":
                    if username1 not in post['Liker list']:
                        post['Liker list'][username1]=0
                        post['Likes']=len(post['Liker list'])
                        save_data()
                        break
                    elif user_input=="2":
                        post['Liker list'].pop(username1)
                        post['Likes']=len(post['Liker list'])
                        save_data()
                        break
                    #elif user_input=="3":
                        #logic_userinterface()
                        #break

                    else:
                        print_error("invalid choise")
                break
        
def feed():
    clear_screen()
    print("=== ALL POSTS ===")

    if "posts" not in project_data:
        print_error("No posts yet.")
        return
    else:
        if username1 not in project_data["posts"]:
            print("No posts yet.")
            return
        for i in project_data["posts"].values():
            for post in i.values():
                print("-" * 40)
                print(f"Post ID : {post['post_id']}")
                print(f"User    : @{post['username']}")
                print(f"Date    : {post['datetime']}")
                print(f"Post    : {post['content']}")
                print(f"Like    : {post['Likes']}")
                print('''
        [1] Like
        [2] Unlike

''')
                while True:
                    user_input=input("Enter Your choise:")
                    if user_input=="1":
                        if username1 not in post['Liker list']:
                            post['Liker list'][username1]=0
                            post['Likes']=len(post['Liker list'])
                            save_data()
                            break
                        elif user_input=="2":
                            post['Liker list'].pop(username1)
                            post['Likes']=len(post['Liker list'])
                            save_data()
                            break
                        #elif user_input=="3":
                           # logic_userinterface()
                           # break

                        else:
                            print_error("invalid choise")
                    break
                

    


def who_to_follow(username):

    clear_screen()
    print("=" * 50)
    print(" "*16,"WHO TO FOLLOW")
    print("=" * 50)

    all_users = set(project_data["users"].keys())

    following = set(project_data["users"][username].get("following", []))

    suggestions = list(all_users - following - {username})

    if not suggestions:
        print("No suggestions available.")
    else:
        for user in suggestions:
            print(f"@{user} ({project_data['users'][user]['display_name']})")

    

    input("\nPress Enter...")


def profile(username1):
    clear_screen()
    print("\n","="*50)
    print(" "*20,"PROFILE")
    print("="*50)
    
    print(f"Display Name : {project_data['users'][username1]['display_name']}")
    print(f"Username : {username1}")
    print(f"Bio : {project_data['users'][username1]['Bio']}")
    print(f"Follower Count : {project_data['users'][username1]['Follower Count']}")
    print(f"Following Count : {project_data['users'][username1]['Following Count']}")
    print("Post : ")
    view_posts()
    
    

def view_profile(current_user, target):
    clear_screen()

    if target==username1:
        profile()

    else:

        print("=" * 50)
        print("PROFILE")
        print("=" * 50)

        print(f"Display Name : {project_data['users'][target]['display_name']}")
        print(f"Username     : @{target}")
        print(f"Bio          : {project_data['users'][target]['Bio']}")
        print(f"Followers    : {project_data['users'][target]['Follower Count']}")
        print(f"Following    : {project_data['users'][target]['Following Count']}")
        print('''
            [1] Follow
            [2] Unfollow
            [3] Go Back

    ''')

        print("\nPosts:\n")

        if "posts" in project_data and target in project_data["posts"]:
            for post in project_data["posts"][target].values():
                print("-" * 40)
                print(post["content"])

        

        while True:
            user_input=input("Enter Your Choise... ")
            if user_input == '1':
                user_input=input("Do You want to follow (yes/no):").lower().strip()
                if user_input=="yes":
                    if username1 not in project_data['users'][target]['Follower']:
                        
                        project_data['users'][target]['Follower'][username1]=0
                        project_data['users'][target]['Follower Count']=len(project_data['users'][target]['Follower'])
                        project_data['users'][username1]['Following'][target]=0
                        project_data['users'][username1]['Following Count']=len(project_data['users'][target]['Follower'])
                        save_data()
                        print_success("Follow succesfull..")
                        break

                    else:
                        print_error("Alrady followed")
                        break

                break

            elif user_input =='2':
                user_input=input("Do You want to unfollow (yes/no):").lower().strip()
                if user_input=="yes":
                    if username1 in project_data['users'][target]['Follower']:
                        
                        project_data['users'][target]['Follower'].pop(username1)
                        project_data['users'][target]['Follower Count']=len(project_data['users'][target]['Follower'])
                        project_data['users'][username1]['Following'].pop(target)
                        project_data['users'][username1]['Following Count']=len(project_data['users'][target]['Follower'])
                        save_data()
                        print_success("Follow succesfull..")
                        break

                    else:
                        print_error("you do not follow this user..")
                        break
                break

            elif user_input =='3':
                user_input=input("Do You want to exit (yes/no):").lower().strip()
                break

            else :
                print_error("invalid choise")
                

def logic_userinterface():
    while True:
        clear_screen()
        print("\n"+"="*50)
        print(" "*15 + f"Loged to =  {username1}     ")
        print("="*50)
            
        print('''
    Choose an option:
        
[1] View Feed
[2] View Profile
[3] Creat a Post
[4] Discover User
[5] Recommendation
[6] Logout
    ''')

    
        user_input=input("select option (1~6)=")
        input("\nPress Enter to continue... ")
        if user_input=="1":
            clear_screen()
            feed()
            

            
            continue
        
        elif user_input=="2":
            clear_screen()
            profile(username1)
            input("\nPress Enter to continue... ")
            save_data()
            
            continue
        
        elif user_input=="3":
            clear_screen()
            create_post(username1)
            input("\nPress Enter to continue... ")
            save_data()
            
            continue
            
        elif user_input=="4":
            clear_screen()
            print("USER DIRECTORY\n")
            for u in project_data["users"]:
                        #print(f"- @{u}")
                        target = input("\nEnter username to view profile: ").strip()
                        if target in project_data["users"]:
                             view_profile(username1, target)
                             input("\nPress Enter for going back... ")
                             
                             break
    
                        else:
                            print_error("user not exist")
                            input("Press Enter to go Back... ")
                             
                           
                            break

        elif user_input=="5":
            clear_screen()
            who_to_follow(username1)
            
            continue
            
        elif user_input=="6":
            clear_screen()
            app()
            return
            
        else:
            print_error("invalid choice please try again")




def register_user():
    clear_screen() 
    print("== REGISTER USER ==")
    
    while True:
        username = input("Enter a unique username: ").strip().lower()
        if "users" in project_data:
            if username in project_data["users"]:
                print_error("username allrady exist try another username")
            else:
                break
                
        else:
            break
            
            
    display_name = input("Enter a unique name: ").strip().lower()
    password = input("Enter a unique password: ").strip().lower()
    bio=input("Enter your bio= ").strip()
    if "users" in project_data:
        project_data["users"].update({username:{"username":username,
                                               "display_name":display_name,
                                               "password":password,
                                               "Bio":bio,
                                               "Follower Count":0,
                                               "Following Count":0,
                                               "Follower":{},
                                               "Following":{}}})
                                           
                                               
                                             
    else:
        project_data["users"]={username:{"username":username,
                                               "display_name":display_name,
                                               "password":password,
                                               "Bio":bio,
                                               "Follower Count":0,
                                               "Following Count":0,
                                               "Follower":{},
                                               "Following":{}}}
    print_success(f"register successful @{username}, @{display_name}, @{password}")
    
   
def app():
    while True:
        clear_screen()
        print_header()
        print_menu()
        
        user_input = input("Enter your choice: ")
        if user_input == "1":
              input("\nPress Enter to continue... ")
              clear_screen()
              login_dashbord()
              break
        elif user_input =="2":
           input("\nPress Enter to continue... ")
           clear_screen()
           register_user()
           input("\nPress Enter to continue... ")
           save_data()
           clear_screen()
           
           
        elif user_input == "3":
           clear_screen()
           print("\n👋 Exiting Social Media App. Goodbye!")
           save_data()
           input("\nPress Enter to continue... ")
          # clear_screen()
          # print("Thank you for visit")
           #return to profile page
           return
        else:
            print_error("Invalid choice. Please select a valid option.")

app()