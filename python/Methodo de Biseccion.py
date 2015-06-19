import math

class Filtra_datos:

    aux =""
    numero=[]
    expnentes=[]
    signos=[]
    f1=0
    other_f = []
      
    def __init__(self,funcion):
        self.funcio_ingre = funcion

    def Limpiar_esp(self):
        self.funcio_ingre = self.funcio_ingre.replace(" ","")

    def Determina_F(self):
        for x in self.funcio_ingre:

            if x.isalpha() and (x != "x" or x != "y" or x != "(" or x != ")"):
                self.aux = self.aux + x

            if x == ")":
                self.other_f.append(self.aux)
                self.aux=""
                
              
              
        
        
        

   
    def Depurar_Funcion_Polin(self):
        
        
        for x in range(0,len(self.funcio_ingre)):
            
            if self.funcio_ingre[x].isdigit():
                self.aux = self.aux + self.funcio_ingre[x]
                if x ==len(self.funcio_ingre) - 1 and (self.funcio_ingre[x-1] == "+" or self.funcio_ingre[x-1] == "-"):
                    self.numero.append(self.aux)
                    
            if self.funcio_ingre[x] == "x" or self.funcio_ingre[x] == "y":
                if self.funcio_ingre[x-1] == "+" or self.funcio_ingre[x-1] == "-":
                    self.aux= '1'
                if x < 1:
                    self.aux= '1'            
            
                self.numero.append(self.aux)                  
                self.aux=""

            if self.funcio_ingre[x] == "+" or self.funcio_ingre[x] == "-":
                self.signos.append(self.funcio_ingre[x])
                self.aux=""

            if self.funcio_ingre[x] == "^":
                self.expnentes.append(self.funcio_ingre[x+1])

        
                
                
                
                
            


        

    def Convertir(self):
        for x in range(0,len(self.numero)):
            self.numero[x]=int(self.numero[x])

        for x in range(0,len(self.expnentes)):
            self.expnentes[x] = int(self.expnentes[x])

    def Procesa_datos(self,num):
        self.f1=0 
        self.xi=num

        for x in range(0,len(self.funcio_ingre)):

            if (self.funcio_ingre[x] == "x" or self.funcio_ingre[x] == "y") and x < len(self.funcio_ingre)- 3 :
                self.numero[self.f1] = self.numero[self.f1] * (pow(self.xi,self.expnentes[self.f1]))
                self.f1=self.f1 + 1

        self.f1 = self.numero[0]

        for x in range(0,len(self.signos)):
            if self.signos[x] == "+":
                self.f1 = self.f1 + self.numero[x+1]
            else:
                self.f1 = self.f1 - self.numero[x+1]

        return self.f1

        

    def Biseccion(self,xi,xu,e_ab):
        self.x_inicio = xi
        self.x_fin = xu
        self.x_error_d = e_ab
            
                      
        while True:

            self.xm = (float(self.x_inicio) + self.x_fin)/2
            
            if float(self.Procesa_datos(self.xm)) == 0.0:
                break
            if (self.Procesa_datos(self.x_inicio) * self.Procesa_datos(self.xm)) < 0:
                self.x_fin = self.xm
            else:
                self.x_inicio = self.xm

            self.x_error= abs(self.x_fin - self.x_inicio)

            if self.x_error < self.x_error_d:
                break         
                 
        
        
    def Mostrar(self):
        #print self.f1
        print self.other_f



ecuacion = raw_input('Escriba la funcion a REsolver: ')
#x1=float(input('de el extremo inferior del intervalo aproximado: '))
#x2=float(input('de el extremo superior del intervalo aproximado: '))
#errordeseado=float(input('De el error deseado: '))

Filtrar = Filtra_datos(ecuacion)
Filtrar.Limpiar_esp()
Filtrar.Determina_F()

#Filtrar.Depurar_Funcion_Polin()
#Filtrar.Convertir()
#Filtrar.Biseccion(x1,x2,errordeseado)
Filtrar.Mostrar()
input('Presione Enter para Finalizar')





