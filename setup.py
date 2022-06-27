from cx_Freeze import setup, Executable
base = None
#Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("the_survivor_HM40.py", base=base)]
#Renseignez ici la liste complète des packages utilisés par votre application
packages = ["idna","pygame","re","time","datetime","types","fr","en","random","os","Slider"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
#Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "The survivor - Game",
    options = options,
    version = "1.0",
    description = 'Jeu vidéo et platformer 2D, faites le meilleur score... si vous le pouvez ! ',
    executables = executables
)