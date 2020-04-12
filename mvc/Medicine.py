class Medicine():
    
    def __init__(self,idMed, name, quantity,price):
        self.idMed = idMed
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def getID(self):
        return self.idMed
    
    def setID(self, idMed):
        self.idMed = idMed
        
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getQuantity(self):
        return self.quantity
    
    def setQuantity(self, quantity):
        self.quantity = quantity
        
    def getPrice(self):
        return self.price
    
    def setPrice(self, price):
        self.price = price
        
    def setTotalPrice(self, qty):
        self.totalprice = self.price*qty