from User import User


class UserQuery():
    
    def __init__(self):
        self.makeUser()

    def makeUser(self):
        self.user1 = User()
        self.user1.setName("Admin")
        self.user1.setPassword("12345")
        self.user1.setUserID(1)
        self.user1.setRole("Cashier")
        
        self.user2 = User()
        self.user2.setName("Cashier")
        self.user2.setPassword("12345")
        self.user2.setUserID(2)
        self.user2.setRole("Cashier")

        
        self.user3 = User()
        self.user3.setName("Pharmacist")
        self.user3.setPassword("65432")
        self.user3.setUserID(3)
        self.user3.setRole("Pharmacist")

        
        self.list = [self.user1, self.user2, self.user3]

    def getAllUser(self):
        return self.list
    
    def getLogin(self, name, password):
        self.role = None
        for user in self.list:
            
            if name == user.name and password == user.password:
                self.role = user.role
                break
            
        return self.role
            
            
        
            