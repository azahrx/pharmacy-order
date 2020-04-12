from MedicineQuery import MedicineQuery

class MedicineController():
    
    def __init__(self):
        self.query = MedicineQuery()

        
    def getAllMed(self):
        return self.query.getAllMed()
    
    def increaseStock(self, idMed, stock):
        self.query.increaseStock(idMed, stock)
        
    def orderMedicine(self,idMed,stock):
        return self.query.orderMedicine(idMed,stock)
        
        
    
        