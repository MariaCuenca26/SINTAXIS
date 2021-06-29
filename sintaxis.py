""" num=10
num=20
if type(num)==int:
    num = num*2
else:
  print("el valor no es numerico")
  
def mensaje(msg):
    print(msg)
               

mensaje("bienbenido a python")
mensaje("Mi primir programa") """

class sintaxix:
  
 #_init_Metodo constructor se ejecuta cuando se instancia la clase cuyo objeto es crear
 # e inicializar los atributos de la clase, Self es un objeto que representa la clase creada 
  def _init_(self,dato= "instancia la clase"):
    self.frase=dato
    
  def usoVariables(self):
    edad, _peso = 19, 60.5
    nombre = 'Maria Cuenca'
    #          012345678910
    Tipo_sexo = 'F'
    civil = True
    # print("civil:{} y su tipo es:{}".format(civil,type(civil)))
     # tuplas = () son colecciones de datos de cualquier tipo inmutables
    usuario=()
    usuario=('dchiki', 1234, 'chiki@gmail.com',True)
    #            0       1          2            3
    #usuario[4]="milagro"
    x = usuario[0]
    # lista = [] colecciones mutables
    materias = ['Programacion web', 'PHP', 'POOD']
    #                   0              1      2
    materias[1]="Python"
    materias.append("GO")
    #diccionario = {} colecciones de objetos clave: valor tipo json
    estudiante={}
    estudiante = {'nombre': 'Maria', 'edad': 19, 'fac': 'faci'}
    estudiante = ["edad"] =21
    estudiante= ["cargo"] ="estudiante"
    y=estudiante["cargo"]
    # print(nombres,nombres[0],nombres[0:2],nombres[-1])
    # print(usuario,usuario[0],usuario[0:2],usuario[-1])
    # print(materias,materias[2:],materias[:2],materias[:-1],materias[:-2])
    print(x,y)
    print(estudiante,estudiante['nombre'])   
  def mostrar(self):
      print("mostrar")
      print(self.frase)
    
ejer1 = sintaxix () #instancia la clase y se crea el objeto1 con todos los atributos y metodos de la clase sintaxix
ejer1.usoVariables()


    
    