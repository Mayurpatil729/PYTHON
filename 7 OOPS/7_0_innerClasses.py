class Outer:
    def m1(self):
        print("Outer class method")
    class Inner:
        def m2(self):
            print("Inner Class Method ")

o=Outer()
o.m1()
i=o.Inner()
i.m2()

#########################################

i=Outer().Inner()
i.m2()

#########################################

Outer().Inner().m2()

##########################################


