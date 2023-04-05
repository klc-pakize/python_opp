
#? Class Variables: Class(sınıf) içerisinde sabit kalan, oluşturulan nesneler(obje, instance) arasında paylaşılan değerler ve nesneden nesenye değişiklik göstermeyen değerledir.
#?                  Remaining constant in Class, The values that are shared among the created objects (instance) and the values that do not change from object to object.

"""
Tüm çalışanların maaşına aynı oranda zam yapmak için:

To increase the salary of all employees at the same rate:
"""
class Personel:
    
    raise_rate = 1.05  # ===> class variables (class değişkeni)

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{name.lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  #* self = objelerin(nesne, instance) kendisini ifade ediyor. | self = refers to the objects(instance) themselves.
        return  f"{self.name} {self.surname}"

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate  # self.raise_rate == Personel.raise_rate 

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(per_1.wage)  # 50000
per_1.apply_a_raise()
print(per_1.wage)  # 52500.0

#* Class Variables Ulaşmak için 2 seçenek vardır: | There are 2 options to Access Class Variables:
# 1- Class Üzerinden | via class
# 2- self ifadesi ile nesne üzerinden | with self statement over object

print(Personel.raise_rate)  # 1.05
print(per_1.raise_rate)  # 1.05
print(per_2.raise_rate)  # 1.05

#* hem sınıf(class) üzerinden hemde classtan ürettiğimiz objenin üzerinde raise_rate ulaştık, peki neden ?
#* We reached raise_rate both on the class and on the object we produced from the class, so why ?
#  - Önce nesneye bakar ve bu değişkeni (raise_rate) nesnede bulamazsa nesnenin oluşturulduğu yani inherit edildiği sınıfı (class) bulur ve bu değişkeni sınıftan alır, varsa.
# - First, it looks at the object and if it cannot find this variable (raise_rate) in the object, it finds the class in which the object was created, that is, inherited, and takes this variable from the class, if any.1

from pprint import pprint
pprint(per_1.__dict__)  # {'email': 'ali.veli@firmam.com',
#                          'name': 'Ali',
#                          'surname': 'Veli',
#                          'wage': 52500.0}

pprint(Personel.__dict__)  # mappingproxy({'__dict__': <attribute '__dict__' of 'Personel' objects>,
#                                          '__doc__': None,
#                                          '__init__': <function Personel.__init__ at 0x0000017C6B748DC0>,
#                                          '__module__': '__main__',
#                                          '__weakref__': <attribute '__weakref__' of 'Personel' objects>,
#                                          'apply_a_raise': <function Personel.apply_a_raise at 0x0000017C6B748EE0>,
#                                          'full_name': <function Personel.full_name at 0x0000017C6B748E50>,
#!                                         'raise_rate': 1.05})


#? Class variables değerini tekrarda güncelledik.
Personel.raise_rate = 1.1
print(Personel.raise_rate)  # 1.1
print(per_1.raise_rate)  # 1.1
print(per_2.raise_rate)  # 1.1


per_1.raise_rate = 1.3
print(Personel.raise_rate)  # 1.1
print(per_1.raise_rate)  # 1.3
print(per_2.raise_rate)  # 1.1

pprint(per_1.__dict__)  # {'email': 'ali.veli@firmam.com',
#                          'name': 'Ali',
#!                         'raise_rate': 1.3,
#                          'surname': 'Veli',
#                          'wage': 52500.0}

#? Neden raise_rate değişkeni per_1 objesinde de var ?
#? Why is the variable raise_rate also in the per_1 object?
#  - per_1 nesnesinin yaratıldığı classtaki değişkeni nesne üzerinden değiştirdiğimiz zaman python sınıf(class) içersindeki class variable çekti 
#    nesne tarafından müdahele edildiği için müdahele eden nesne içersinde bu raise_rate eklendi.
#  - When we changed the variable in the class in which the per_1 object was created, python pulled the class variable in the class
#    This raise_rate has been added in the interfering object because it is being tampered with by the object.


"""
Bir tane data class variables ekleyelim ve bu sefer bu değişken oluşturulan herhangi bir nesne tarafından müdahele edilmeyecek ve etkilenmeyecek bir değişken olsun:

Let's add one data class variables and this time it will be a variable that will not be interfered with and affected by any created object:
"""
class Personel:
    
    raise_rate = 1.05  # ===> class variables (class değişkeni)
    personel_count = 0  # ===> class variables (class değişkeni)

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

        Personel.personel_count += 1

    def full_name(self):  #* self = objelerin(nesne, instance) kendisini ifade ediyor. | self = refers to the objects(instance) themselves.
        return  f"{self.name} {self.surname}"

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate  # self.raise_rate == Personel.raise_rate 

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(Personel.personel_count)  # 2