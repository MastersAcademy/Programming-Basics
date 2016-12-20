from User import User


class Subscriber(User):
    def __init__(self, email, first_name, last_name):
        User.__init__(self, email, first_name, last_name, 'admin')

    def comment_article(self):
        return "Yay! I can comment an article"
