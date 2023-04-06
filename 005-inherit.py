
#! Alt Sınıf Üretme ve Çalışma (Inherit)
"""
Personel uygulamamızı büyütme kararı aldık. Müdür, yazılımcı gibi farklı sınıflarda oluşturacağız.
Yapmış olduumz planan göre her sınıfta tekrar eden bazı nesne değişkenleri mevcut isim, soyisim, maaş gibi.
Bizim en büyük kuralımız olan DRY bu yüzden miras alma(inherit) işimizi oldukça kolaylaştırıyor.

We decided to enlarge our personnel application. We will create different classes such as manager, software developer.
According to the plan we have made, there are some object variables that repeat in each class, such as name, surname, salary.
DRY, which is our biggest rule, makes our job of inheriting a lot easier.
"""

class Personel:
    
    raise_rate = 1.05  # ===> class variables (class değişkeni)

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  #* self = objelerin(nesne, instance) kendisini ifade ediyor. | self = refers to the objects(instance) themselves.
        return  f"{self.name} {self.surname}"

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate  # self.raise_rate == Personel.raise_rate 


class Developer(Personel):  # ===> Miras almak istediğimiz class'ın ismini parantez içinde belirtmemiz gerekiyor. 
#                                  We need to specify the name of the class we want to inherit in parentheses.
    pass




yaz_1 = Developer(surname="vEli", name="Ali", wage=50000)
yaz_2 = Developer("ayşe", "Yılmaz", 25000)

print(yaz_1.full_name())  # Ali Veli
print(yaz_1.name)  # Ali
#! Developer classının içi boş olmasına rağmen sonuç aldık, sebebi:
#  İlk Developer classını kontrol eder boş olduğunu gördü,
#  Parantez içersinde Personel classını gördü ve Personel Classına çıktı, init metodunu devreye soktu ve sonuç verdi
#  Bu olay Method Resolution Order yani miras zinciri diyebiliriz.

#! We got results even though the developer class is empty, the reason is:
# Checks the first Developer class and sees it's empty.
# He saw the Personnel class in parentheses and went to the Personnel Class, activated the init method and gave results
# This event can be called the Method Resolution Order, that is, the inheritance chain.

print(help(Developer))  
"""
class Developer(Personel)
 |  Developer(name, surname, wage)
 |
 |  Method resolution order:
 |      Developer
 |      Personel
 |      builtins.object
 |
 |  Methods inherited from Personel:
 |
 |  __init__(self, name, surname, wage)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  apply_a_raise(self)
 |
 |  full_name(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Personel:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from Personel:
 |
 |  raise_rate = 1.05
"""

print(help(Personel))
"""
class Personel(builtins.object)
 |  Personel(name, surname, wage)
 |
 |  Methods defined here:
 |
 |  __init__(self, name, surname, wage)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  apply_a_raise(self)
 |
 |  full_name(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  raise_rate = 1.05
"""

class Developer(Personel):  # ===> Miras almak istediğimiz class'ın ismini parantez içinde belirtmemiz gerekiyor. 
#                                  We need to specify the name of the class we want to inherit in parentheses.
    raise_rate = 1.2

print(yaz_1.wage)  # 50000
yaz_1.apply_a_raise()
print(yaz_1.wage)  # 52500.0

print(help(Developer))  
"""
class Developer(Personel)
 |  Developer(name, surname, wage)
 |
 |  Method resolution order:
 |      Developer
 |      Personel
 |      builtins.object
 |
 |  Data and other attributes defined here:
 |
 |  raise_rate = 1.2
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Personel:
 |
 |  __init__(self, name, surname, wage)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  apply_a_raise(self)
 |
 |  full_name(self)
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Personel:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
"""

#? Senaryoya Developer için uzman programlama dili ekleyelim
class Developer(Personel):  # ===> Miras almak istediğimiz class'ın ismini parantez içinde belirtmemiz gerekiyor. 
#                                  We need to specify the name of the class we want to inherit in parentheses.
    raise_rate = 1.2
    
    def __init__(self, name, surname, wage, language):
        super().__init__(name, surname, wage)
        self.language = language


yaz_1 = Developer(surname="vEli", name="Ali", wage=50000, language="Python")
yaz_2 = Developer("ayşe", "Yılmaz", 25000, "Java")

print(yaz_1.language)  # Python
print(yaz_2.language)  # Java


#? Manager class ekleyip, manager bağlı olduğu çalışanlarında gözükmesini aynı zamanda çalışanı olmayan manager olduğunda hata almamak istiyoruz
#? We want to add a manager class so that the manager appears in his employees, and we do not get an error when he is a non-employee manager.

class Manager(Personel):
    def __init__(self, name, surname, wage, personel = None):
        super().__init__(name, surname, wage)
        if personel == None:
            self.personel = []
        else:
            self.personel = personel

    
    def personel_add(self, per):
        if per not in self.personel:
            self.personel.append(per)

    def personel_del(self, per):
        if per in self.personel:
            self.personel.remove(per)

    def personel_list(self):
        for per in self.personel:
            print(per.full_name())


mng_1 = Manager("Atakan", "Ata", 40000, [yaz_1])
mng_2 = Manager("Şahin", "Ata", 80000)

print(mng_1.full_name())
mng_1.personel_list()  # Ali Veli

mng_1.personel_add(yaz_2)
mng_1.personel_list()  # Ali Veli
                       # Ayşe Yılmaz

mng_1.personel_del(yaz_1)
mng_1.personel_list()  # Ayşe Yılmaz

