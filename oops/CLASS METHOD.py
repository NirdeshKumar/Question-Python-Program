
# 2. CLASS METHOD


class school:
    batch="python"
    @classmethod
    def stu(cls,value):
        cls.batch=value
        
obj2=school()
obj=school()
obj.stu("Java")
print(obj.batch)
print(school.batch)
print(obj2.batch)
