[app]

# (str) Title of your application
title = ZBarCam Demo

# (str) Package name
package.name = zbarcamdemo

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivymd

# (str) Source code where the main.py live
source.dir = src

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,jpeg,ttf,kv,json,txt

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (str) Application versioning (method 2)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/kivy_garden/zbarcam/version.py

android.numeric_version = 1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = 
    python3,
    #kivy[base] @ https://github.com/102757017/kivy/archive/master.zip,
    kivy,
    git+https://github.com/102757017/KivyMD.git@master,
    sdl2_ttf==2.0.15,
    pillow,
    android,
    #opencv-python,
    xcamera,
    pyzbar


# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#requirements.source.zbarcam = %(source.dir)s/kivy_garden/zbarcam

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/assets/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/assets/kivymd.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
#android.presplash_color = #FFFFFF

# (list) Permissions
android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE


# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) Android logcat filters to use
# android.logcat_filters = *:S python:D

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a



[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
bin_dir = ./bin
