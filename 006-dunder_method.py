
#! Sınıflarda Kullanılan Özel Metodlar(Dunder Method):
class Personel:
    
    raise_rate = 1.05  

    #! __init__: 
    #* Bu metod, sınıfın bir örneği (instance) oluşturulduğunda otomatik olarak çağrılır ve örneğin başlatılması için kullanılır. 
    #* self parametresi, oluşturulan örneği temsil eder ve __init__ metodunda örneğin özellikleri (attribute) tanımlanır.
    #? This method is called automatically when an instance of the class is created and is used to initialize the instance.
    #? The self parameter represents the created instance and the __init__ method defines the instance's attributes.
    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  
        return  f"{self.name} {self.surname}"

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate  

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(per_1)  # <__main__.Personel object at 0x00000175B2145300>



class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  
        return  f"{self.name} {self.surname}"

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate


    #! __repr__: 
    #* Bu metod, bir nesnenin "string temsili" (string representation) olarak bilinen bir metin çıktısı döndürür. 
    #* Bu metod, print() veya str() gibi işlemler yapıldığında çağrılır.
    #? This method returns a text output known as a "string representation" of an object.
    #? This method is called when performing operations like print() or str()
    def __repr__(self):
        return f"Personel('{self.name}', '{self.surname}', '{self.wage}')" 

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(per_1)  # Personel('Ali', 'Veli', '50000')



class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  
        return  f"{self.name} {self.surname}"

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate

    def __repr__(self):
        return f"Personel('{self.name}', '{self.surname}', '{self.wage}')" 
    

    #! __str__: 
    #* Bu metod, bir nesnenin string temsili (string representation) olarak kullanılacak bir metin çıktısı döndürür. 
    #* Bu metod, print() veya str() fonksiyonları gibi yerlerde kullanıldığında otomatik olarak çağrılır. 
    #* Genellikle, bir nesnenin kullanıcı tarafından okunabilir bir şekilde temsil edilmesi gerektiğinde __str__ metodunu kullanırız.
    #? This method returns a text output to be used as the string representation of an object.
    #? This method is called automatically when used in places like print() or str() functions.
    #? Usually we use the __str__ method when an object needs to be represented in a user-readable way.
    def __str__(self):
        return f"{self.full_name()} - {self.email}"

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(per_1)  # Ali Veli - ali.veli@firmam.com

print(repr(per_1))  # Personel('Ali', 'Veli', '50000')
print(per_1.__repr__())  #  Personel('Ali', 'Veli', '50000')

print(str(per_1))  # Ali Veli - ali.veli@firmam.com
print(per_1.__str__())  # Ali Veli - ali.veli@firmam.com



"""
Aynı departmanda çalışan personellerin maaşını toplayalım:

Let's sum up the salary of the staff working in the same department:
"""
class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  
        return  f"{self.name} {self.surname}"

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate

    def __repr__(self):
        return f"Personel('{self.name}', '{self.surname}', '{self.wage}')" 
    
    def __str__(self):
        return f"{self.full_name()} - {self.email}"
    

    #! __add__: 
    #* Bu metod, iki nesnenin toplama işlemi yapılması durumunda çağrılır. 
    #* Sınıfın özel bir metodudur ve + operatörü ile kullanılır.
    #? This method is called when two objects are added.
    #? It is a private method of the class and is used with the + operator.
    def __add__(self, other):
        return self.wage + other.wage

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(per_1 + per_2)  # 75000
print(Personel.__add__(per_1, per_2))  # 75000
print(per_1.__add__(per_2))  # 75000



"""
Bir sebepten dolayı personellerin tam isimlerinin uzunluklarına ihtiyaç vardır.

There is a need for the lengths of the staff's full names for some reason.
"""
class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  
        return  f"{self.name} {self.surname}"

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate

    def __repr__(self):
        return f"Personel('{self.name}', '{self.surname}', '{self.wage}')" 
    
    def __str__(self):
        return f"{self.full_name()} - {self.email}"
    
    def __add__(self, other):
        return self.wage + other.wage
    

    #! __len__: 
    #* Bu metod, bir nesnenin uzunluğunu döndürür. 
    #* Örneğin, bir dize (string) için karakter sayısını, bir listedeki öğelerin sayısını veya bir sözlükteki anahtar sayısını döndürebilir.
    #? This method returns the length of an object.
    #? For example, it can return the number of characters for a string, the number of items in a list, or the number of keys in a dictionary.
    def __len__(self):
        return len(self.full_name())


per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(per_2.__len__())  # 11
print(Personel.__len__(per_2))  # 11
print(len(per_2))  # 11