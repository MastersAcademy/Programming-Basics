class User(object):
    def __init__(self, email, first_name, last_name, user_role):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.user_role = user_role

    def __str__(self):
        return "email: %s, first_name: %s, last_name: %s, user_role: %s" % (self.email, self.first_name, self.last_name, self.user_role)

    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
