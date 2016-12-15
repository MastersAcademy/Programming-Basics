from User import User


class Admin(User):
    def __init__(self, email, first_name, last_name, can_create_users, can_edit_all_messages):
        User.__init__(self, email, first_name, last_name, 'admin')
        self.can_create_users = can_create_users if can_create_users else 'true'
        self.can_edit_all_messages = can_edit_all_messages if can_edit_all_messages else 'true'

    def create_user(self, user_email):
        return 'Ho-ho! User \'%s\' created' % user_email

    def edit_any_message(self):
        return 'Editing everything!'
