
#? Class: Sınıflar(class), nesnelerin(Instance) özelliklerini ve davranışlarını tanımlayan şablonlardır.
#?        Classes are templates that define the properties and behavior of objects.

#? Instance: Bir sınıftan oluşturulan her bir örneğe "instance" veya "nesne" denir.
#?           Each instance created from a class is called an "instance" or "object".

#* Sytnax:
#           class ClassName:  ===> Python'da class isimleri büyük harfle başlamak zorunda değildir, | Class names in Python don't have to start with a capital letter,
#               code blog          ancak genel olarak kabul edilen bir yazım şeklidir. | is only a generally accepted syntax.
#                                  PEP 8 Python stil kılavuzuna göre, sınıf isimleri genellikle CamelCase olarak yazılır. | According to the PEP 8 Python style guide, class names are usually written as CamelCase.
#               


"""
Senaryo:
    Bir şirketimiz var ve bu şirkette çalışan personelin bilgilerini saklamak için bir uygulamamız var.

    We have a company and we have an application to keep the information of the personnel working in this company.
"""

class Personel:
    pass


per_1 = Personel()  #* Personel classının ilk instance (obje veya örenği) oluşturduk 
                    #* We created the first instance (object) of the personnel class

print(Personel)  # <class '__main__.Personel'>
print(per_1)  # <__main__.Personel object at 0x000002A0B39BF820> == objenin kimliğini (ID'sini) gösterir


per_1.name = "Ali"
per_1.surname = "Veli"
per_1.email = "Ali.Veli@firma.com"

print(per_1.name)  # Ali

"""
Yüzlerce personel olduğunu düşünürsek bunu bir otomasyona bağlamamız gerekmektedir.
Bu aşamada nesnelerin(instance) oluşturduğumuz class'ın yapısı üzerinde blue print oluşturursak ne istiğimizi bilgisayara daha net verirsek otomasyone çevirebiliriz:

Considering that there are hundreds of personnel, we need to automate this.
At this stage, if we create a blue print on the structure of the class we created, we can turn it into automation if we give what we want more clearly to the computer:
"""
class Personel:
    def __init__(self, name, surname, wage):
        self.name = name
        self.surname = surname
        self.wage = wage


#? __init__() fonksiyonu, 
#* bir sınıfın(class) instance(obje) oluşturulduğunda çağrılan özel bir yöntemdir. 
#  Bu fonksiyon, sınıfın özelliklerini tanımlar ve örnek oluşturulurken bu özelliklere başlangıç değerleri atar.
#* self sınıfımızdan oluşturacağımız objeleri(nesne, instance) ifade eder.
#  self.wage kısımları instance variable(nesne değişkenleri) temsil eder.


#? Instance oluşturma | Creating Instance

per_1 = Personel(surname="Veli", name="Ali", wage=50000)
per_2 = Personel("Ayşe", "Yılmaz", 25000)

print(per_1.name)  # Ali
print(per_1.surname)  # Veli
print(per_1.wage)  # 50000

print(per_2.name)  # Ayşe
print(per_2.surname)  # Yılmaz
print(per_2.wage)  # 25000


"""
Bu şekilde yüzlerce kişi oluşturduktan sonra, e-posta adreslerini oluşturmadığımızı fark ettik:

After creating hundreds of contacts this way, we realized we didn't generate their email addresses:
"""
class Personel:
    def __init__(self, name, surname, wage):
        self.name = name
        self.surname = surname
        self.wage = wage
        self.email = f"{name}.{surname}@firmam.com"

per_1 = Personel(surname="Veli", name="Ali", wage=50000)
per_2 = Personel("Ayşe", "Yılmaz", 25000)

print(per_1.email)  # Ali.Veli@firmam.com
print(per_2.email)  # Ayşe.Yılmaz@firmam.com


"""
Mesela objelerde(instance) isimleri soyisimleri oluştuturken küçük hark büyük hark dikkat etmemiş olabiliriz. 
Aynı zamanda mail adreslerinde küçük harf kullanılması gerektiğini fark etmiş olabiliriz.

For example, we may not have paid attention to upper and lower case letters when creating names and surnames on objects.
At the same time, we may have noticed that lowercase letters should be used in e-mail addresses.
"""
class Personel:
    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{name.lower()}.{surname.lower()}@firmam.com"

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(per_1.surname)  # Veli
print(per_1.email)  # ali.veli@firmam.com

print(per_2.name)  # Ayşe
print(per_2.email)  # ayşe.yılmaz@firmam.com


"""
Bazı durumlarda personellerin tam isimiyle işlem yapmamız gerekebilir:

In some cases, we may need to process the full name of staff:
"""
per_1_full_name = f"{per_1.name} {per_1.surname}"
per_2_full_name = "{} {}".format(per_2.name, per_2.surname)

print(per_1_full_name)  # Ali Veli
print(per_2_full_name)  # Ayşe Yılmaz


"""
Bu şekilde yüzlerce personel için tek tek yazmamız gerekecek, bunun yerine bir method tanımlayabiliriz:

This way we will have to write for hundreds of staff one by one, instead we can define a method:
"""
class Personel:
    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{name.lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  #* self = objelerin(nesne, instance) kendisini ifade ediyor. | self = refers to the objects(instance) themselves.
        return  f"{self.name} {self.surname}"

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

print(per_1.full_name())  # Ali Veli
print(Personel.full_name(per_1))  # Ali Veli