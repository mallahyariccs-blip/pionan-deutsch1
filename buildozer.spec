[app]

title = PIONAN Deutsch Courses
package.name = pionan_deutsch
package.domain = org.pionan
version = 1.0.0

source.dir = .
source.main = main.py
source.include_exts = py,html,txt,json,jpg,png

requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 0

[android]

# نسخه Buildozer 1.5.0
p4a.branch = stable
android.sdk = 24
android.ndk = 10e
android.minapi = 21
android.maxapi = 29
android.targetapi = 29
android.arch = armeabi-v7a

# دسترسی‌ها
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.wakelock = True
android.accept_sdk_license = True

# ویژگی‌ها
android.allow_backup = True

[buildozer]

log_level = 2