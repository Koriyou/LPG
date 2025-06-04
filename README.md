# LPG - Cyberpunk red Lifepath generator

a simple generator for lifepaths and role based lifepaths for cyberpunk red.

generates characters in a markdown folder that you can import in
Xmind

can generate characters at random if your players have a hard time picking what characters they would like to play.

## Running

Ensure you have Python 3 installed. The `LifepathGenerator.py` script is
executable and can be run directly:

```bash
./LifepathGenerator.py
```

The program guides you through a questionnaire and writes the generated
lifepath to `LP2.md`.

## Building a standalone executable

Install [PyInstaller](https://pyinstaller.org/) and run the helper script:

```bash
pip install pyinstaller
./build_exe.sh
```

This creates a self-contained executable in the `dist/` directory.
