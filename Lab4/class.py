class vehicles:
    def __init__(self,model,color):
          self.model = model
          self.color = color
    def seatingCapacity(self, capacity):
        self.capacity = capacity
    def display(self):
        print(self.model, " ", self.color, " " , self.capacity)
    
vehicles("aaa", "red")

