class M12:
    time='2:30'
    course="python full stack"
    def __init__(self,name,mobno,gender,aadhar):
        self.name=name
        self.mobno=mobno
        self.gender=gender
        self.aadhar=aadhar
student1=M12("Abhisek Samal",8114860650,'Male',98765123412)
student2=M12("Aditya Rath",8156789012,'Male',98765432412)
print(student1.name,student1.mobno,student1.gender,student1.aadhar)
print(student2.name,student2.mobno,student2.gender,student2.aadhar)