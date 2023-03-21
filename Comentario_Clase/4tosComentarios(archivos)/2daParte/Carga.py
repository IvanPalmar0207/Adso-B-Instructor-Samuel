from Vehiculo import * #Con la palabra reservada from se hace un llamado del archivo que se quiere importar en este caso es Vehiculo, y con la palabra import se dice que se requiere del archivo Vehiculo en este caso todo, ya que con la instruccion '*' se refiere a todo.
class Carga(Vehiculo): #La palabra reservada class sirve para crear una clase nueva, su nombre es 'Cargar' pero es una subclase osea hereda todo de una clase princiapal en este caso su superclase es 'Vehiculo'.
    def __init__(self,placa,conductor,capacidad,ejes): #Se instancia el constructor de la clase cargo, en su lista de parametros contiene 5 parametros, el primero es self que es el parametro obligatorio para indicar que el constructor se enceuntra en la clase Carga, los otros cuatro son paramtros que finalmente seran atributos, los paametros son; placa, conductor, cpacidad y ejes.
        Vehiculo.__init__(self,placa,conductor) #Aqui se hace un llamada de los atrbutos o varaibles de instancias y de sus metodos, primero se llama el nombre de la super clase 'Vehiculo' y despues se hace el constructor que tiene los parametros de la clase vehiculo osea, self el parametro obligatorio, placa y conductor. 
        self.__capacidad=capacidad #Se crea una nueva variable de instancia, que es self.__capacidad y contiene lo del parametro capacidad que esta en la lista de parametros del constructor de esta mima clase.
        self.__ejes=ejes #Se crea una nueva variable de instancia, que es self.__ejes y contiene lo del parametro capacidad que esta en la lista de parametros del constructor de esta mima clase.
    def getCapacidad(self): #Se crea un metodo que es getCapacidad() que seguramente servira para retornar lo que contenga el atributo self.__capacidad, en su lista de parametros esta el parametro obligatorio self que es para indicar que el metodo se encuentra dentro de la clase.
        return self.__capacidad #El return en este caso devolvera y mostrara por pantalla cuando se llame con ell objeto creado para la clase, o retornara lo que contenga el atributo self.__capacidad y lo mostrara por pantalla.
    def getEjes(self):
        return self.__ejes