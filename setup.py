import cx_Freeze

executables = [cx_Freeze.Executable (script="jogo.py", icon="assets/mestre.ico")]

cx_Freeze.setup(
    name="O Mundo Mágico das Letras",
    options={
        "build_exe": {
            "packages": ["pygame","random","time"],
            "include_files":["assets"]
        }},
    executables=executables
)