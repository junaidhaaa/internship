class Student:
    name="sam"
    age=20
    def __init__(self,n1,a1):
        self.name=n1
        self.age=a1
    def set_data(self,n,a):
        self.name=n
        self.age=a
    def display_data(self):
        print(self.name)
        print(self.age)
    def __del__(self):
        print('This is destructor')    
st=Student("Thaswin",22)
st.display_data()       
#st.set_data("Kiran","21")
#st.display_data()       
 