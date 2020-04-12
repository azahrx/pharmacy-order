from Medicine import Medicine

class MedicineQuery():
    
    def __init__(self):
        self.makeMed()

    def makeMed(self):
        self.med1 = Medicine(1, "Redoxon", 250, 35000)
        self.med2 = Medicine(2, "Panadol", 600, 10000)
        self.med3 = Medicine(3, "Vitacimin", 700, 4000)
        
        self.list = [self.med1, self.med2, self.med3]

    def getAllMed(self):
        return self.list
    
    def increaseStock(self,medId,stock):
        medId = int(float(medId))
        for med in self.list:
            if medId == med.idMed:
                med.quantity = med.quantity + stock
                
    def orderMedicine(self,medId,stock):
        medId = int(float(medId))
        self.orderlist = []
        for med in self.list:
            if medId == med.idMed:
                med.quantity = med.quantity - stock
                med.setTotalPrice(stock)
                self.orderlist.append(med)
                
        return self.orderlist
    
 
            
        
    
