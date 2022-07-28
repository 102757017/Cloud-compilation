[app]

# (str) Title of your application
title = WICO

# (str) Package name
package.name = WICO

# (str) Package domain (needed for android/ios packaging)
package.domain = org.kivymd

# (str) Source code where the main.py live
source.dir = .

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/assets/images/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/assets/images/logo.png

# (string) Presplash background color (for new android toolchain)
#android.presplash_color = #000000

# (list) Source files to include (let empty to include all the files)
#source.include_exts = py, gif, png, jpg, jpeg, ttf, kv, json, txt, md

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
# contains an 'androidx' package, or any package from Kotlin source.
# android.enable_androidx requires android.api >= 28
# android.enable_androidx = True

# (str) Application versioning (method 2)
version = 0.0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3, \
               kivy==2.1.0, \
               git+https://github.com/102757017/KivyMD.git@master, \
               pillow, \
               sqlite3, \
               sdl2_ttf==2.0.15, \
               android, \
               #opencv-python, \
               xcamera, \
               pyzbar, \
               mariadb

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = all

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 30

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only. If set to False,
# the default, you will be shown the license when first running
# buildozer.
android.accept_sdk_license = True

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = armeabi-v7a

android.release_artifact = apk

# (str) python-for-android branch to use, defaults to master
p4a.branch = develop

# (list) Permissions
android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
