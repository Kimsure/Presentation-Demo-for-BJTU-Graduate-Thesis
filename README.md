# BJTU Graduate Thesis/Design Presentation System

> ## This Project is totally based on PyDracula. Consider Donate (Gumroad): https://gum.co/mHsRC
> ### Install
> - Python==3.9
> - Pyside6
> **Warning**: using previous versions can cause compatibility problems.
> ### Tutorial
> 🔗 **Yotube**: https://youtu.be/9DnaHg4M_AM
> 
> 🔗 **Bilibili**: https://www.bilibili.com/video/BV1ww411Z7Np/?spm_id_from=333.337.search-card.all.click&vd_source=1e0a15618f3d86b448a0be782b0ea479

## Multiple Themes
![PyDracula_Default_Dark](https://user-images.githubusercontent.com/60605512/112993874-0b647700-9140-11eb-8670-61322d70dbe3.png)
![PyDracula_Light](https://user-images.githubusercontent.com/60605512/112993918-18816600-9140-11eb-837c-e7a7c3d2b05e.png)


## Running
> Inside your preferred terminal run the commands below depending on your system, remembering before installing Python 3.9> and PySide6 "pip install PySide6".
> ### **Windows**:
```console
python main.py
```
> ### **MacOS and Linux**:
```console
python3 main.py
```
## Compiling
> ### **Windows**:
```console
python setup.py build
```

## Project Files And Folders
> **main.py**: application initialization file.

> **main.ui**: Qt Designer project.

> **resouces.qrc**: Qt Designer resoucers, add here your resources using Qt Designer. Use version 6 >

> **setup.py**: cx-Freeze setup to compile your application (configured for Windows).

> **themes/**: add here your themes (.qss).

> **modules/**: module for running PyDracula GUI.

> **modules/app_funtions.py**: add your application's functions here.
Up
> **modules/app_settings.py**: global variables to configure user interface.

> **modules/resources_rc.py**: "resource.qrc" file compiled for python using the command: ```pyside6-rcc resources.qrc -o resources_rc.py```.

> **modules/ui_functions.py**: add here only functions related to the user interface / GUI.

> **modules/ui_main.py**: file related to the user interface exported by Qt Designer. You can compile it manually using the command: ```pyside6-uic main.ui> ui_main.py ```.
After expoting in .py and change the line "import resources_rc" to "from. Resoucers_rc import *" to use as a module.

> **images/**: put all your images and icons here before converting to Python (resources_re.py) ```pyside6-rcc resources.qrc -o resources_rc.py```.

## Other Impressive Designs Using PySide

**Explore the projects available for your presentation demo.**
> YoloSide6: https://github.com/Jai-wei/YOLOv8-PySide6-GUI
> 
> FluentDesign: https://qfluentwidgets.com/zh/
>
> FluentUI: https://github.com/zhuzichu520/PySide6-FluentUI-QML
>
> SiliconUI: https://github.com/ChinaIceF/PyQt-SiliconUI



