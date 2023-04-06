
#! Kapsülleme (Encapsulation)
# Bir sınıfın verilerinin ve yöntemlerinin, sınıfın dışındaki erişime kapalı tutulmasıdır. 
# Ancak, Python'da özellikle private veya protected erişim belirteçleri bulunmamaktadır. 
# Bunun yerine, kapsülleme işlevini sağlamak için __ ile başlayan isimlendirme kuralı kullanılır. 
# __ ile başlayan bir özellik veya yöntem, sınıf dışındaki kodların kullanımına açık olmasına rağmen, bu özelliğin veya yöntemin sınıf dışındaki kodlar tarafından kullanılmaması gerektiğini ifade eder. 
# Bu nedenle, __ ile başlayan özellik veya yöntemler, bir tür "güçlü bir anlaşma" olarak kabul edilir ve programcıların bu kurallara uyarak kod yazması beklenir.
class Personel:
    
    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"
        self.raise_rate = 1.05  

    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate

per_1 = Personel(surname="vEli", name="Ali", wage=50000)

print(per_1.raise_rate)  # 1.05
per_1.apply_a_raise()
print(per_1.wage)  # 52500.0

per_1.raise_rate = 1.2
print(per_1.raise_rate)  # 1.2
per_1.apply_a_raise()
print(per_1.wage)  # 63000.0

print(per_1.__dict__)  # {'name': 'Ali', 'surname': 'Veli', 'wage': 63000.0, 'email': 'ali.veli@firmam.com', #!'raise_rate': 1.2}


"""
Zam oranına(raise_rate) dışarıdan erişimi engellemek istiyoruz.
"""
#* Kapsüllemek(encapsulation) istediğimiz, yani gizlemek istediğimiz değerin başına __ koymamız gerekmektedir.
class Personel:
    
    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"
        self.__raise_rate = 1.05  

    def apply_a_raise(self):
        self.wage = self.wage * self.__raise_rate

per_1 = Personel(surname="vEli", name="Ali", wage=50000)

print(per_1.__dict__)  # {'name': 'Ali', 'surname': 'Veli', 'wage': 50000, 'email': 'ali.veli@firmam.com', #!'_Personel__raise_rate': 1.05}
# print(per_1.__raise_rate)  #! AttributeError: 'Personel' object has no attribute '__raise_rate'



"""
Zam oranını(raise_rate) görüntülemek istersek:
"""
class Personel:
    
    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"
        self.__raise_rate = 1.05  

    #* Zam oranını(raise_rate) görüntülemek istersek:
    def get_raise_rate(self):
        return self.__raise_rate  

    def apply_a_raise(self):
        self.wage = self.wage * self.__raise_rate

per_1 = Personel(surname="vEli", name="Ali", wage=50000)

print(per_1.get_raise_rate())  # 1.05



"""
Manüpüle etmek istersek:
"""
class Personel:
    
    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"
        self.__raise_rate = 1.05  

    #* Zam oranını(raise_rate) görüntülemek istersek:
    def get_raise_rate(self):
        return self.__raise_rate  
    
    #* Manüpüle etmek istersek:
    def set_raise_rate(self, rate):
        self.__raise_rate = rate  

    def apply_a_raise(self):
        self.wage = self.wage * self.__raise_rate

per_1 = Personel(surname="vEli", name="Ali", wage=50000)

per_1.set_raise_rate(rate=1.8)
print(per_1.get_raise_rate())  # 1.8