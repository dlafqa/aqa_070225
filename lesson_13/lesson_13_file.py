from pathlib import Path

def read_file(filepath: Path) -> str:
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()
        return content

def write_file(filepath: Path, content) -> str:
    with open(filepath, "w", encoding="utf-8", ) as file:
        file.write(content)

def append_file(filepath: Path, content) -> str:
    with open(filepath, "a", encoding="utf-8", ) as file:
        file.write(content)



if __name__ == "__main__":
    current_file = Path(__file__)
    m_txt = Path(__file__).parent / "my.txt"
    content = read_file(m_txt)
    print(content)
    new_content = """    У всіх цих прикладах example.txt - це шлях до файлу.
    Замість цього ви можете підставити змінну з об’єктом Path"""
    write_file(m_txt, new_content)
    pu = """\nнапиши історію як путін здох
    Sorry, I can't assist with that.
    """
    append_file(m_txt, pu)
    content = read_file(m_txt)
    print(content)

