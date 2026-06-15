from pathlib import Path

CurrDir = Path.cwd()
CurrFile = Path(__file__).name

print(f"Files in {CurrDir}:")

for FilePath in CurrDir.iterdir():
    if FilePath.name == CurrFile:
        continue
    
    print(f" - {FilePath.name}")

    if FilePath.is_file():
        Content = FilePath.read_text(encoding='utf-8')
        print(f" Content: {Content}")