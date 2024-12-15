import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
qrc_file = os.path.join(parent_dir, "src","data","images.qrc")
result_parent = os.path.join(parent_dir,"src","py", "images_rc.py")

print(f"pyside6-rcc {qrc_file} -o {result_parent}")
os.system(f"pyside6-rcc {qrc_file} -o {result_parent}")

# pyside6-uic /경로/파일이름.ui -o /경로/파일이름.py
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ui_path = os.path.join(parent_dir, "src","data","ui")
ui_files = os.listdir(ui_path)
print(ui_files)
for ui_file in ui_files:
    if ui_file.endswith(".ui"):
        result_file = os.path.join(ui_path,ui_file.replace(".ui", ".py"))
        print(f"result_file: {result_file}")
        print(f"pyside6-uic {os.path.join(ui_path, ui_file)} -o {result_file}")
        os.system(f"pyside6-uic {os.path.join(ui_path, ui_file)} -o {result_file}")