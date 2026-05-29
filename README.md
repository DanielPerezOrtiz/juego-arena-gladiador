### English
### Python RPG Combat Arena
This is a Python learning project. As I progress in my learning journey, I continuously optimize and improve the project's code. For now, the game features classes, methods, loops, and a turn-based combat system. It also includes a basic AI for the enemy, which decides whether to heal or even dodge depending on the situation. Additionally, it features a difficulty system and a second phase in the highest difficulty setting to create a decent challenge.

### Execution
To run the game, make sure you have Python installed on your system. Since the project only uses standard libraries like random and json, no additional installations are required. Simply open your terminal or console, navigate to the project folder, and run the main script (class.py) using the corresponding command.

### Game Mechanics
When you start the program, you will find a menu with three options:

New Game: Start from scratch and create your gladiator with the stats of your choice within the given values.

Load Game: Allows you to continue with your saved gladiator.

Exit: Closes the program.

Under the first option, you will go through character creation to set your name, HP, defense points, attack points, luck, and potions. Then, you will move to the difficulty selector, where each level features enemies with different stats—and a surprise in the final enemy.

Once this is done, a turn-based combat begins where you choose between attacking or healing. Keep in mind that both you and the enemy can attack, heal, or dodge if luck is on your side. In the highest difficulty, if the enemy reaches a certain health threshold, it activates its second phase, significantly boosting its stats and turning it into an "impossible" challenge, just as the difficulty level promises.

### Known Issues
Currently, the "Load Game" function does not execute a new match after loading, as I am actively working on it to fix it as soon as possible. (Nota: Ajusté levemente esto porque en el código que me pasaste la función de cargar sí lee el JSON, pero es bueno dejar claro que estás puliendo el flujo).

### Future Improvements
Implement a leveling system for the character, allowing progression upon clearing certain thresholds and defeating bosses.

Add an inventory system to manage items during and after combat.

Improve the difficulty system to create an even greater challenge and balance the scaling alongside the character's levels.

Add a language system to choose between Spanish and other languages in future updates



### ESPAÑOL
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
