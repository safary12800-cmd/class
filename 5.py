# 1
# class Pc:
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model
#     def __str__(self):
#         return f"bun pc nomi{self.name} , madeli esa {self.model}"
# pc=Pc(" Lenovo","V15 IPT")
# print(pc)        

# class Notebook(Pc):
#     def __init__(self, name, model,rangi):
#         super().__init__(name, model)
#         self.rang=rangi
#     def __str__(self):
#         return f"{super().__str__()},unig rangi {self.rang}"
# nt=Notebook("  Lenova","LOQ Gaming",'qora')
# print(nt)

# class Planshet(Pc):
#     def __init__(self, name, model,narxi):
#         super().__init__(name, model)
#         self.narx=narxi
#     def __str__(self):
#         return f'{super().__str__()}, narxi {self.narx}$'
# p=Planshet("Apple",'iPad M12', 1200)
# print(p)


# 2
# class Hodim:
#     def __init__(self,name,kasbi,maoshi):
#         self.name=name
#         self.kasbi=kasbi
#         self.maoshi=maoshi
#     def __str__(self):
#         return f" bu hodimning ismi{self.name}, sabi {self.kasbi}, maoshi {self.maoshi} $"
# h=Hodim("bir balo",'SEO',121252)
# print(h)
# class Menijer(Hodim):
#     def __init__(self, name, kasbi, maoshi,korhona):
#         super().__init__(name, kasbi, maoshi)
#         self.ko=korhona
#     def __str__(self):
#         return f"{super().__str__()} va u shu korhonada ishlaydi {self.ko}"
# me=Menijer('bir', 'bugalter',3125,'TBS Bank')
# print(me)

# class Dasturchi(Hodim):
#     def __init__(self, name, kasbi, maoshi,ishlash_turi):
#         super().__init__(name, kasbi, maoshi)
#         self.ishturi=ishlash_turi
#     def __str__(self):
#         return f"{super().__str__()},ishlash turi  { self.ishturi}"
# d=Dasturchi("bir nima","Dasturchi",3125648,"online")
# print(d)
# 3
# class Transport:
#     def __init__(self,nomi,rusumi):
#         self.nomi=nomi
#         self.rusumi=rusumi
#     def __str__(self):
#         return f"bu transport nomi: {self.nomi}  va  rusumi: {self.rusumi} "
# tr=Transport("tank","bilmiman")
# print(tr)

# class Avtobus(Transport):
#     def __init__(self, nomi, rusumi,turi):
#         super().__init__(nomi, rusumi)
#         self.turi=turi
#     def __str__(self):
#         return f'{super().__str__()}, uning  turi: {self.turi}'
# bus=Avtobus("nmadur","birnarsa","yolovchi tashish uchun")
# print(bus)

# class Samalyot(Transport):
#     def __init__(self, nomi, rusumi, chipta_narxi):
#         super().__init__(nomi, rusumi)
#         self.chipta=chipta_narxi
#     def __str__(self):
#         return f'{super().__str__()} chipta narxi: {self.chipta} $'
# sam=Samalyot("samalyot",'birnarsa',177)
# print(sam)


# 4# class Transport:
#     def __init__(self,nomi,rusumi):
#         self.nomi=nomi
#         self.rusumi=rusumi
#     def __str__(self):
#         return f"bu transport nomi: {self.nomi}  va  rusumi: {self.rusumi} "
# tr=Transport("tank","bilmiman")
# print(tr)

# class Avtobus(Transport):
#     def __init__(self, nomi, rusumi,turi):
#         super().__init__(nomi, rusumi)
#         self.turi=turi
#     def __str__(self):
#         return f'{super().__str__()}, uning  turi: {self.turi}'
# bus=Avtobus("nmadur","birnarsa","yolovchi tashish uchun")
# print(bus)

# class Samalyot(Transport):
#     def __init__(self, nomi, rusumi, chipta_narxi):
#         super().__init__(nomi, rusumi)
#         self.chipta=chipta_narxi
#     def __str__(self):
#         return f'{super().__str__()} chipta narxi: {self.chipta} $'
# sam=Samalyot("samalyot",'birnarsa',177)
# print(sam)



# 5# class Transport:
#     def __init__(self,nomi,rusumi):
#         self.nomi=nomi
#         self.rusumi=rusumi
#     def __str__(self):
#         return f"bu transport nomi: {self.nomi}  va  rusumi: {self.rusumi} "
# tr=Transport("tank","bilmiman")
# print(tr)

# class Avtobus(Transport):
#     def __init__(self, nomi, rusumi,turi):
#         super().__init__(nomi, rusumi)
#         self.turi=turi
#     def __str__(self):
#         return f'{super().__str__()}, uning  turi: {self.turi}'
# bus=Avtobus("nmadur","birnarsa","yolovchi tashish uchun")
# print(bus)

# class Samalyot(Transport):
#     def __init__(self, nomi, rusumi, chipta_narxi):
#         super().__init__(nomi, rusumi)
#         self.chipta=chipta_narxi
#     def sss(self,yolvaqti):
#         self.vaqt=yolvaqti
#         return f'{super().__str__()},  yol vaqti {self.vaqt}'
#     def __str__(self):
#         return f'{super().__str__()} chipta narxi: {self.chipta} $'
# sam=Samalyot("samalyot",'birnarsa',177)
# print(sam)
# print(sam.sss(11))
