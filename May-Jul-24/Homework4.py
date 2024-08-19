class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.posts = []

    def __repr__(self):
        return f"Name: {self.name}, Email: {self.email}"

    def write_post(self, title, content, blog, publish_date):
        post = Post(title, content, self.name, publish_date)
        blog.add_post(post)
        self.posts.append(post)

    def display_posts(self):
        if not self.posts:
            return "Author has no posts yet!"
        else:
            return [post.display_content() for post in self.posts]


class Post:
    def __init__(self, title, content, author, publish_date):
        self.title = title
        self.content = content
        self.author = author
        self.publish_date = publish_date

    def edit_content(self, new_content):
        self.content = new_content

    def display_content(self):
        return (self.title, self.author, self.content, self.publish_date)


class Blog:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.posts = []

    def __repr__(self):
        return f"Name: {self.name}, Description: {self.description}"

    def add_post(self, post):
        self.posts.append(post)

    def remove_post(self, post):
        self.posts.remove(post)

    def display_posts(self):
        if not self.posts:
            return "Blog has no posts yet!"
        else:
            return [post.display_content() for post in self.posts]


author1 = Author("Emad", "emadna@ac.sce.ac.il")
blog1 = Blog("Test Blog", "That's the description of the test blog")

print(author1.display_posts())
print(blog1.display_posts())

author1.write_post("Test Post", "That's the content of the test post", blog1, "12/09/2013")

print(author1.display_posts())
print(blog1.display_posts())
print(Post.edit_content("Test Post", "Edited Content"))