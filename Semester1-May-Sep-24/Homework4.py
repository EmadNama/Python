class Author:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.posts = []

    def __repr__(self):
        return f"Author Name: {self.name}, Email: {self.email}"

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
        return f"Blog Name: {self.name}, Description: {self.description}"

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

print(author1)
print(blog1)

print(author1.display_posts()) #Empty posts of Author
print(blog1.display_posts()) #Empty blog

author1.write_post("Test Post", "Content of the Test Post", blog1, "24/07/1996")

print(author1.display_posts()) #author posts after method author.write_post
print(blog1.display_posts()) #blog posts after author.write_post

blog1.posts[0].edit_content("New Content")

print(blog1.display_posts()) #blog posts after editing a post

blog1.remove_post(blog1.posts[0])
print(blog1.display_posts()) #blog posts after removing a post