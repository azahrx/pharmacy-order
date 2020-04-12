from UserQuery import UserQuery

class UserController():
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def checkLogin(self):
        query = UserQuery()
        return query.getLogin(self.username, self.password)