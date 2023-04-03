
# CLASS VARIABLE

class school:
    batch="Python"
    batch2="Java"
    def __init__(self):
        self.name="NIrdesh Kumar"
        self.age=21
        self.batch3="c# Language"
t1=school()
t2=school()
t1.batch="C++"
school.batch="C++"
print("\n\n",t1.batch)
print(school.batch)
print("\n",t2.batch)
