from cx_Freeze import setup, Executable

setup(
    name="O Mundo Mágico das Letras - Júlia Bianchi",
    options={
        "build_exe": {
            "packages": ["pygame"],
            "include_files":["assets"]
        }},
    executables= [Executable (script="game.py", icon="assets/mestre.ico")],
)