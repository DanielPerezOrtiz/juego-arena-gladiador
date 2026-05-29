### Arena de combate RPG en python 
Esto es un projecto de aprendizaje en python donde a medida que avanzo en el aprendizaje de python, optimizo y mejoro el codigo de mi proyecto. Por ahora el juego cuenta con clases, metodos, bucles y un sistema de combate por turnos
tambien cuento con una ia basica en el enemigo, pues esta decide, dependiendo de la situacion, si curarse e incluso esquivar, cuenta con un sistema de dificultad y segunda fase en la ultima dificultad para  crear un reto descente
### Ejecución :
Para ejecutar el juego asegurate de tener python instalado en tu sistema. Como el  proyecto solo usa librerias estandars como 'random' y 'json' no se necesita instalar nada mas 
simplemente, abre tu terminal o consola, navega hasta la carpeta del proyecto y ejecuta el script principal (class.py) con el comando correspondiente
### Mecanica de juego
al iniciar el programa, se encotraran con un menu con tres opciones:
1.*** Nuevo juego:*** comienzas desde cero, creas a tu gladiador con sus stats que elijas dentro de los valores dados
2.*** Cargar partida:*** te permite continuar con tu gladiador guardado
3.*** salir:*** Cierra el programa 
en la opcion uno pasas por la creacion de personaje con su nombre, los hp, puntos de defensa, puntos de ataque, surte y pociones, luego pasas al slector de dificultad cada uno con enemigos con stats diferentes y sorpresa en el ultimo enemigo
una ves pasado esto comienza un combate por turnos donde elijes entre atacar o curarte, teniendo en cuenta de que ambos pueden atacr, curarse o esquivar si tienes suerte
en la ultima dificultad si el enemigo alcanza cierto umbral de vida activa su segunda fase donde sus stats crecen abismal mente y se convierte en un reto imposible como dice su dificultad 
### Problemas Conocidos 
Actualmente la funcion de cargar partdida no hace nada pues estoy trabajando en ello para arreglarlo lo antes pocible
### Mejoras futuras 
* implementar un sistema de niveles para el personaje, donde se pueda progresar al superar ciertos umbrales y jefes
* añadir un sistema de inventario para gestionar objetos durante y despues del combate
* mejorar el sistema de dificultad para hacer un reto aun mayor y equilibrar el sistema con los niveles del personaje
* añadir un sistema de idiomas para elejir entre español y otros idiomas en proximas actualizaciones 
