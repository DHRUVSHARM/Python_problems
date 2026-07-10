"""
notes 


"""

class User:
    def __init__(self, username, display_name):
        self.username = username
        self.display_name = display_name

    def show_profile(self):
        print("User:", self.display_name, "(@" + self.username + ")")
    
    def create_post(self, content):
        post = Post(content, self)
        return post

    def like_post(self, post):
        post.like_post(self)
    
    # Add your code here
    def unlike_post(self, post):
        post.unlike_post(self)       

class Post:
    def __init__(self, content, author):
        self.content = content  
        self.author = author  
        self.likes = [ ]
    
    def like_post(self, user):
        if user not in self.likes:
            self.likes.append(user)
            print(user.display_name, "liked this post!")
        else:
            print(user.display_name, "has already liked this post!")
    
    # Add your code here
    def unlike_post(self , user):
        if user is self.likes:
            self.likes.remove(user)
            print("like has been removed !!!")
        else:
            print("not liked !!!")        

# Add you code here
user1 = User("alex123", "Alex")
user2 = User("cody8", "Cody")

post1 = user1.create_post("This is my first Chirp!!!")

print(user1.display_name + " posted a chirp: " + post1.content)
user2.like_post(post1)

# Add your code here