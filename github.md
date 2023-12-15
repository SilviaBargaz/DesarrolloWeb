PASO 1: CREAR REPOSITORIO EN GITHUB Y CLONAR

github.com

Botón + Nuevo repositorio

Escribir un nombre que esté libre

Crear un archivo README.md

Copiar la url del repositorio:

https://github.com/alansastre/curso_java

En Visual Studio Code, lo clonamos: Opción 1: Ctrl + Shift + P y buscar clon Opción 2: Abrir un nuevo vscode y aparece Welcome y Clone git repository

Pegar la url con Ctrl + V

Se abre una ventana y le seleccionamos el escritorio para que clone el repositorio en el Escritorio.

PASO 2: SUBIR CÓDIGO A GITHUB (PUSH)

git push

En Visual Studio Code una vez hechos los commits, el botón de source control permite hacer un push.

Otra opción sería en la esquina inferior izquierda se puede sincronizar.

El objetivo es subir el código a un repositorio remoto (GitHub).

PASO 3: DESCARGAR CÓDIGO DESDE GITHUB A LOCAL (PULL)

Crear cambios en archivos directamente sobre GitHub y hacerles commit allí mismo.

PAra descargar a vscode esos cambios podemos volver a pulsar la ruleta de la esquina inferior izquierda.

Pull: descargar los cambios

Fetch: comprobar si hay cambios pero sin descargarlos.

PASO 4: CONFLICTOS LOCAL VS GITHUB

Cuando hacemos push y pull lo que ocurre es git fusiona los cambios automáticamente.

Si existen cambios en los mismos archivos en las mismas líneas entonces git no es capaz de fusionarlos y nos pide a nosotros resolverlos a través de la UI.

vscode colorea en verde los cambios locales y en azul los cambios entrantes, el desarrollador decide el cambio.

Esto puede ocurrir en varios archivos, se deben resolver de uno en uno.

PASO 5: CLONAR EL REPOSITORIO DE CLASE

Aceptar la invitación.

Clonar el repositorio.

No introducir cambios.

Un consejo abrir mi repositorio en GitHub y abrir vuestro propio proyecto en vscode.

PASO 6: PRUEBAS DE COLABORACIÓN EN UN REPOSITORIO

curso_java_pruebas

Cada uno se clona el proyecto

Escribe un archivo con su nombre, por ejemplo:

alan.md

PASO 7: GitHub Desktop

https://desktop.github.com/

REQUISITOS PREVIOS

Cuenta en GitHub
Git
Visual Studio Code con extensiones:
GitLens
Git Graph
vscode icons (opcional): al instalarla pide activarla
GitHub Desktop
INSTALACIÓN GITHUB DESKTOP

https://desktop.github.com/

Al abrir tiene 3 opciones:

Clone a repository from the Internet: usar esta para clonar un repositorio de GitHub o algún otro sitio.

Create a New Repository on your hard drive: crea un nuevo proyecto con git y lo sube a GitHub.

Add an Existing Repository from your hard drive: esta opción la usamos cuando ya tenemos un repositorio en local. Esto abre un repositorio que ya exista, no crea uno nuevo.

GITHUB DESKTOP CLONAR REPOSITORIO

Pulsar botón clonar, aparece una ventana con 3 pestañas:

Pestaña github.com ahí se puede buscar el nombre y ya lo encuentra

Pestaña URL, deja pegar la URL del repositorio.

En ambos casos hay un botón Choose que permite elegir donde guardar.

GITHUB DESKTOP AÑADIR REPOSITORIO LOCAL EXISTENTE

Add an Existing Repository from your hard drive

Seleccionar la carpeta donde está el proyecto en Local Path.

CUIDADO: se abre la carpeta del proyecto, no la carpeta .git

Pulsar Add repository

GITHUB DESKTOP: COMMIT Y PUSH

Si sale 0 changed files entonces no aparece nada, es decir, no hay cambios y por tanto no podemos hacer commit.

Editar código y crear más archivos desde vscode.

Pero hacer commit y push y pull desde GitHub Desktop.

GITHUB DESKTOP: PULL

En Github desktop el botón de sincronizar permite descargar los cambios.

Fetch Origin: comprueba si hay cambios
Pull Origin: descarga cambios
GITHUB DESKTOP: CREAR NUEVO REPOSITORIO

Desde GitHub Desktop cuando se abre la primera vez una opción es crear nuevo repositorio.

Abre un modal similar a GitHub que permite crear el proyecto e indicar donde se guarda.

El botón de sincronizar aparece con el texto: Publish que significaría publicar en GitHub.

GITHUB DESKTOP: CONFLICTO

Newer commits on remote

Desktop is unable to push commits.

Sale una ventana:

Resolve conflicts before Merge

Open in Visual Studio Code

No conflicts remaining en verde.

Pulsamos Continue merge.

GITHUB: OTRAS FUNCIONALIDADES:

Issues: permite crear tareas con un identificador único.

Ese identificador, por ejemplo #3, si lo usamos en un commit, se vincula el commit a esa tarea.

CONCEPTOS BÁSICOS

Instalación git
Cuenta GitHub
Visual Studio Code
GitHub Desktop
Add y Commit
Push
Fetch y Pull
Sincronizar: hacer pull y push
Clonar
por git bash:

git init
git add .
git commit -m "mensaje"
git push
git pull
git clone

PASO 8: Ramas

Una rama sería como una copia del workspace.

Es como si creamos una copia del proyecto entero en este momento y podemos introducir cambios en esa copia sin alterar el proyecto original.

¿Para qué se usa?

Para desarrollar nuevas funcionalidades de forma separada a lo que es el trabajo principal, y mejorar la estabilidad del proyecto.

main

alansastre --> commit --> commit --> commit --> commit --> push --> merge

fregilberto --> commit --> commit

main

funcionalidad1 --> commit1a --> commit2a --> commit3 --> commit4 -- merge

funcionalidad2 --> commit1b --> commit2b -->

CREAR RAMA

Desde Visual Studio Code hay varias opciones:

Opción 1: en la statusbar (barra inferior) seleccionar donde pone main y se abre un panel que pone Create New branch.
Opción 2: En source Control, en la pestaña Branches (hay que tener GitLens), tiene un botón +
Opción 3: Ctrl + Shift + P y buscar branch y seleccionar Create Git Branch
Una vez seleccionada la opción de añadir Rama pedirá un nombre.

Desde GitHub Desktop:

La segunda opción del menú superior, la que pone current branch.

Hacemos click en New Branch

FUSIONAR RAMA

Resultado:

main --> commit1 --> commit2

alansastre --> commit1 --> commit2

orderstatus --> commit1

products --> commit2 --> commit3

Se puede fusionar una rama en cualquier otra rama.

Fusionar es copiar los commits de una rama a otra. (merge)

Lo primero es decidir qué rama queremos fusionar en qué rama:

Rama origen
Rama destino
Ejemplo:

Rama origen: alansastre o order-status
Rama destino: main
Hay que situarse en la rama destino.

En GitHub desktop, en el panel de ramas, aparece el botón abajo del todo para fusionar.

BORRAR RAMA EN LOCAL

En GitHub Desktop, en el panel de ramas, clic derecho da la opción Delete.

NOTA: fusionar la rama antes de borrarla.

BORRAR EN GITHUB

Cuando se borra una rama en local, no se borra automáticamente de github.

https://github.com/alansastre/java_pruebas/branches

Aparece el listado de ramas y sobre cada una un botón de borrar.

Otra opción sería renombrarlas. Pero es habitual borrar y crear una nueva.

RAMAS

En GitHub desktop, pulsar el segundo botón del menú superior donde pone Current Branch.

Pulsar botón nueva rama y poner nuestro nombre y apellido todo junto.

Probar a realizar 3 commits y push.

Mirar Git Graph y ver como se mueve la posición donde estamos

Fusionar desde GitHub Desktop. Para fusionar nos cambiamos a la rama destino primero.

GIT STASH

Si estamos en una rama y tenemos cambios, pero no queremos hacer commit entonces podemos cambiar de rama desde github desktop y da la opción de conservar cambios en main. Esto sería un Git Stash.

Eso significa que se guardan los cambios y luego los podemos recuperar.

Te cambias de rama

Vuelves a la rama main y aparece la opción de restaurar esos cambios.

hay que pulsar el botón azul de Restore.

REPOSITORIO ESPECIAL EN GITHUB CON USERNAME

Si en Github creamos un repositorio con el mismo nombre que nuestro username es un repositorio especial donde añadir un README que aparecerá

username: alansastre

repositorio: alansastre

BORRAR REPOSITORIO

En settings, hacer scroll hacia abajo del todo, en Danger zone permite borrar.

MOSTRAR IMAGENES EN MARKDOWN

Pegar una imagen en la carpeta de nuestro proyecto.

Desde un archivo md podemos mostrarla escribiendo esta sintaxis:

Hola mundo

GIT FLOW

Modelo Git Glow

Modelo sencillo:

main --> --> --> --> --> --> -->
alan --> --> --> -->
carlos --> --> -->
Modelo Git Flow:

main --> 1.0.0 --> 1.1.0
develop
alan
carlos
Instalar extensión gitflow OK

Cerrar y volver a abrir Visual Studio Code OK

Crear nuevo proyecto con GitHub Desktop OK

Open in visual studio code OK

Ctrl + Shift + P: Gitflow Initialize repository for gitflow

main
develop
bugfix/
feature/
release/
hotfix/
support
Esto crea ramas y nos coloca en develop

Crear una feature para hacer un nuevo desarrollo

Ctrl + Shift + P : GitFlow Feature Start
Hacer commits y push
Ctrl + Shift + P: GitFlow Feature Finish
SOLUCION PROBLEMAS GITFLOW

Si sale un cuadro rojo entonces:

Ctrl + Shift + P: Gitflow Feature start te saca un panel que dice Enable now

Entonces comienza automaticamente a inicializar: main, develop, bugfix...

PROCESO COMPLETO DE DESARROLLO

FEATURES

develop --> feature/desarrollo1

Para introducir nuevos desarrollos en develop:

Gitflow feature start: crea una nueva rama por ejemplo feature/product-list
nuevos cambios, commit y push
Gitflow feature finish: fusiona la rama feature en develop y cierra la rama feature automáticamente.
RELEASES

develop --> release/v1.0.0 --> main

Para mover los desarrollos de develop a main:

Gitflow release start: crea nueva rama por ejemplo release/v1.0.0
nuevos cambios , commit y push
Gitflow release finish: fusiona la rama release en main y develop y la cierra