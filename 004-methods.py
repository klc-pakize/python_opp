
#! Regular Method(Sıradan Metod): 
#? Regular Methodlar, sınıf içinde tanımlanmış ve genellikle nesne ile ilgili işlemleri gerçekleştirmek üzere tasarlanmış yöntemlerdir. 
#  Bu yöntemlerin ilk argümanı "self" olarak belirtilir ve nesneyi temsil eder. 
#? Bu sayede nesnenin özelliklerine (attributes) ve diğer yöntemlerine erişebilir ve üzerinde işlem yapabilirsiniz.
#  Regular Methodlar, sınıfın özelliklerini manipüle etmek, sınıfın yapısını değiştirmek, nesne yaratmak, nesne özelliklerine erişmek gibi çeşitli işlemler yapmak için kullanılabilir. 
#? Regular Methodlar, genellikle def anahtar kelimesi ile tanımlanırlar.

class Personel:
    
    raise_rate = 1.05  # ===> class variables (class değişkeni)
    personel_count = 0  # ===> class variables (class değişkeni)

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

        Personel.personel_count += 1

    #? REGULAR METHOD
    def full_name(self):  #* self = objelerin(nesne, instance) kendisini ifade ediyor. | self = refers to the objects(instance) themselves.
        return  f"{self.name} {self.surname}"

    #? REGULAR METHOD
    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate  # self.raise_rate == Personel.raise_rate 

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)


#! Class Method(Sınıf Metodları):
#? Class Methodlar, sınıfın kendisine özgü olan metodlardır. 
#  Yani, bir sınıfın herhangi bir örneği(instance) oluşturulmadan da kullanılabilirler.
#? Class Methodlar, @classmethod dekoratörü kullanılarak tanımlanır ve ilk parametreleri sınıfın kendisini ifade eden cls parametresidir. 
#  Class Methodlar, sınıfın özellikleriyle ilgili işlemler yapmak için kullanılır

class Personel:
    
    raise_rate = 1.05  # ===> class variables (class değişkeni)
    personel_count = 0  # ===> class variables (class değişkeni)

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

        Personel.personel_count += 1

    #? REGULAR METHOD
    def full_name(self):  #* self = objelerin(nesne, instance) kendisini ifade ediyor. | self = refers to the objects(instance) themselves.
        return  f"{self.name} {self.surname}"

    #? REGULAR METHOD
    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate  # self.raise_rate == Personel.raise_rate

    #? CLASS METHOD
    @classmethod
    def set_raise_rate(cls, rate):
        cls.raise_rate = rate

per_1 = Personel(surname="vEli", name="Ali", wage=50000)
per_2 = Personel("ayşe", "Yılmaz", 25000)

Personel.set_raise_rate(1.4)
print(Personel.raise_rate)  # 1.4
print(per_1.raise_rate)  # 1.4
print(per_2.raise_rate)  # 1.4

#? Classtan oluşturulmuş herhangi bir obje ilede çağrılıp değiştirebiliriz, cls ile sınıfın üzerinden git dediğimiz için class ulaşıp değişiklik yaptık.
#? We can call and change any object created from the class. Since we said go over the class with cls, we reached the class and made changes.
per_1.set_raise_rate(1.3)
print(Personel.raise_rate)  # 1.3
print(per_1.raise_rate)  # 1.3
print(per_2.raise_rate)  # 1.3

#! Class Method yapılandırma metodu olarakta kullanılır, class metodu ile bir sınıftan nesne yaratabiliriz:

"""
Senoryada bazı değişiklikler yapalım, bir yönetici tarafından yeni personeller bir mail ile tarafımıza new_personel = "Sam-Wish-5000" şeklinde geldiğini ve uygulamaya girilmesinin istendiğini düşünelim:

Let's make some changes in the scenario, let's assume that a new staff member came to us with an e-mail as new_personel = "Sam-Wish-5000" and asked to enter the application:
"""
per_str_1 = "Sam-Wish-5000"
per_str_2 = "Babby-Singer-8000"
per_str_3 = "Cansu-Canan-9000"

name, surname, wage = per_str_1.split("-")
new_per_1 = Personel(name, surname, wage)
print(new_per_1.name)  # Sam

#* Kod tekrarına düşmemek için bir düzenleme yapalım, yukarıdaki tanımlama gibi bir çok tanımlamamaız olabilir
#* Let's make an edit to avoid code duplication, we may have many definitions like the definition above.
class Personel:
    
    raise_rate = 1.05  # ===> class variables (class değişkeni)
    personel_count = 0  # ===> class variables (class değişkeni)

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

        Personel.personel_count += 1

    #? REGULAR METHOD
    def full_name(self):  #* self = objelerin(nesne, instance) kendisini ifade ediyor. | self = refers to the objects(instance) themselves.
        return  f"{self.name} {self.surname}"

    #? REGULAR METHOD
    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate  # self.raise_rate == Personel.raise_rate

    #? CLASS METHOD
    @classmethod
    def set_raise_rate(cls, rate):
        cls.raise_rate = rate

    @classmethod
    def from_string(cls, per_str):
        name, surname, wage = per_str.split("-")
        return cls(name, surname, wage)
    
per_str_1 = "Sam-Wish-5000"
per_str_2 = "Babby-Singer-8000"
per_str_3 = "Cansu-Canan-9000"

new_per_1 = Personel.from_string(per_str_1)
new_per_2 = Personel.from_string(per_str_2)
new_per_3 = Personel.from_string(per_str_3)
print(new_per_1.name)  # Sam
print(new_per_2.name)  # Babby
print(new_per_3.name)  # Cansu


#! Static Method
#? Static methodlar, sınıfın bir örneği(objesi) olmadan çağrılabilen metodlardır. 
#  Bu metodlar sınıfın herhangi bir özelliğine veya örneğine erişemezler, sadece sınıf içinde kullanılabilecek işlemleri gerçekleştirirler.
#? Static methodların tanımlanması için @staticmethod dekoratörü kullanılır. 
#  Dekoratör, metodun statik olduğunu belirtir ve metodu sınıfın bir örneği olmadan doğrudan çağrılabilir hale getirir. 

#? Static methods are methods that can be called without an instance (object) of the class.
#  These methods cannot access any property or instance of the class, they only perform operations that can be used within the class.
#? The @staticmethod decorator is used to define static methods.
#  Decorator specifies that the method is static and makes the method directly callable without an instance of the class.
class Personel:
    
    raise_rate = 1.05  # ===> class variables (class değişkeni)
    personel_count = 0  # ===> class variables (class değişkeni)

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

        Personel.personel_count += 1

    #? REGULAR METHOD
    def full_name(self):  #* self = objelerin(nesne, instance) kendisini ifade ediyor. | self = refers to the objects(instance) themselves.
        return  f"{self.name} {self.surname}"

    #? REGULAR METHOD
    def apply_a_raise(self):
        self.wage = self.wage * self.raise_rate  # self.raise_rate == Personel.raise_rate

    #? CLASS METHOD
    @classmethod
    def set_raise_rate(cls, rate):
        cls.raise_rate = rate

    @classmethod
    def from_string(cls, per_str):
        name, surname, wage = per_str.split("-")
        return cls(name, surname, wage)

    #? STATIC METHOD
    @staticmethod
    def work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return "weekend"
        else:
            return "weekday"
        
import datetime
date = datetime.date(2023, 4, 6)
print(Personel.work_day(date))  # weekday