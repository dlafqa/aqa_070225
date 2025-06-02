import xml.etree.ElementTree as ET
from pathlib import Path

xml_path = Path(__file__).parent / "group.xml"

tree = ET.parse(xml_path)
root = tree.getroot()

# Читання та виведення даних з елементів XML-документу
for child in root:
    print("P", child.tag, child.attrib, child.text)
    for subchild in child:
        print("c", subchild.tag, subchild.attrib, subchild.text)

for group in root.findall('group'):
    timing_exbytes = group.find('timingExbytes')
    if timing_exbytes is not None:
        bbo = timing_exbytes.find('bbo')
        if bbo is not None:
            print(f"Group: {group.find('name').text}, bbo: {bbo.text}")
        else:
            print(f"Group: {group.find('name').text}, bbo: Не знайдено")


# for group in root.findall("*//bbo"):
#     if bbo is not None:
#         print(f"bbo: {bbo.text}")
#     else:
#         print(f"bbo: Не знайдено")
