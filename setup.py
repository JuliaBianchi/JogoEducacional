import cx_Freeze
executables = [cx_Freeze.Executable{
    script="jogo.py", icon="assets/mestre-dos-magos.jpg"}]
cx_Freeze.setup(
    nome = "O Mundo Mágico das Letras",
    options ={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }},
        executables=executables
)