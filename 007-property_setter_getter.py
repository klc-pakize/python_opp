
#! Property Decorators: 
# @property decorator'ü, bir metodun, nesne özelliği gibi kullanılmasına olanak tanıyan bir özelliktir. 
# Bu özellik sayesinde, bir metoda erişmek, nesne özelliği gibi çağrılabilir ve . işareti ile erişilebilir hale gelir.

class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage
        self.email = f"{''.join(name.split()).lower()}.{surname.lower()}@firmam.com"

    def full_name(self):  
        return  f"{self.name} {self.surname}"
    
per_1 = Personel(surname="vEli", name="Ali", wage=50000)

print(per_1.name)  # Ali 
print(per_1.email)  # ali.veli@firmam.com 
print(per_1.full_name())  # Ali Veli 



"""
Diyelimki per_1 personelimizin adını yanlış girmişiz ve takım arkadaşımız bu fark edip düzeltmek istedi:
"""
per_1.name = "Ahmet"
print(per_1.name)  # Ahmet 
print(per_1.email)  #! ali.veli@firmam.com  ===> ali yerine ahmet yazılmadı, Neden ?
                    #! email değişkeni __init__ fonksiyonu ile tetiklediğimizde çalışan bir metoddur.
                    #! Nesneyi oluşturulurken tetiklenen bu method sonradan name değişkenine yeni bir değer verdiğimizde tetiklenmez!!

print(per_1.full_name())  # Ahmet Veli
                          #! Burda hata almadık, çünkü bu method tetiklendiği zaman devreye girer, kalıcı olarak değer saklamaz.
                          #! name değişkeni güncellendikten sonra tetiklendiği için güncel veriyi sundu.



"""
Yukarıdaki durumu düzeltmek için email'i de bir regural method yapabiliriz. 
"""
class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage

    def email(self):  
        return  f"{''.join(self.name.split()).lower()}.{self.surname.lower()}@firmam.com"
    
    def full_name(self):  
        return  f"{self.name} {self.surname}"
    
per_1 = Personel(surname="vEli", name="Ali", wage=50000)

per_1.name = "Ahmet"
print(per_1.name)  # Ahmet 
print(per_1.email())  # ahmet.veli@firmam.com 
print(per_1.full_name())  # Ahmet Veli 



"""
Ama şimdide objeyi oluşturduğumda direkt email nesne değişkeni oluşmayacak method ne zaman tetiklenirse o zaman oluşucak.
Peki metodu nesne değişkeni gibi kullanılmasına olanak tanıyan bir özellik var mıdır?
Evet, @property decorator ile.
"""
class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage

    @property
    def email(self):  
        return  f"{''.join(self.name.split()).lower()}.{self.surname.lower()}@firmam.com"
    
    @property
    def full_name(self):  
        return  f"{self.name} {self.surname}"
    
per_1 = Personel(surname="vEli", name="Ali", wage=50000)

per_1.name = "Ahmet"
print(per_1.name)  # Ahmet 
print(per_1.email)  # ahmet.veli@firmam.com 
print(per_1.full_name)  # Ahmet Veli 



#! Setter Method: 
# Bir nesne özelliğinin değerini değiştirmek için kullanılan bir özelliktir. 
# Bu method, bir nesne özelliği için yeni bir değer atanmasına olanak tanır.
# setter methodu, özellikle @property decorator'ü ile birlikte kullanıldığında, bir nesne özelliği için okuma ve yazma işlemlerini kontrol etmek için kullanılabilir.
"""
Başka bir yazılımcı arkadaşımız objenin name ve surname değişkenlerini değişmek istiyor ve bunu full_name değişkeni ile yapabileceğini düşünüp atama yapıyor.
Bu durumda python bize hata verir. #! AttributeError: can't set attribute 'full_name'


"""
class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage

    @property
    def email(self):  
        return  f"{''.join(self.name.split()).lower()}.{self.surname.lower()}@firmam.com"
    
    @property
    def full_name(self):  
        return  f"{self.name} {self.surname}"
    
    @full_name.setter
    def full_name(self, fullname):
        name, surname = fullname.split(' ')
        self.name = name
        self.surname = surname
    
per_1 = Personel(surname="vEli", name="Ali", wage=50000)

per_1.full_name = "Ahmet Yılmaz"
print(per_1.name)  # Ahmet 
print(per_1.email)  # ahmet.veli@firmam.com 
print(per_1.full_name)  # Ahmet Yılmaz



#! Deleter Method: 
# Bir sınıfın özelliklerinin silinmesini sağlayan bir özelliktir. 
# Bir özellik üzerinde bir deleter methodu tanımlamak, del anahtar kelimesi ile özelliğin silinmesini sağlar.
class Personel:
    
    raise_rate = 1.05  

    def __init__(self, name, surname, wage):
        self.name = name.title()
        self.surname = surname.title()
        self.wage = wage

    @property
    def email(self):  
        return  f"{''.join(self.name.split()).lower()}.{self.surname.lower()}@firmam.com"
    
    @property
    def full_name(self):  
        return  f"{self.name} {self.surname}"
    
    @full_name.setter
    def full_name(self, fullname):
        name, surname = fullname.split(' ')
        self.name = name
        self.surname = surname

    @full_name.deleter
    def full_name(self):
        print("Object variable deleted")
        self.name = None
        self.surname = None
    
per_1 = Personel(surname="vEli", name="Ali", wage=50000)

print(per_1.name)  # Ali 
print(per_1.full_name)  # Ali Veli
del per_1.full_name
print(per_1.name)  # None 
print(per_1.full_name)  # None None
