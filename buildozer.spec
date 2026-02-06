[app]
title = PIONAN Deutsch
package.name = pimon
package.domain = org.test

source.dir = .
source.main = main.py
source.include_exts = py, png, jpg, kv, atlas

version = 1.0
requirements = python3, kivy

orientation = portrait
fullscreen = 0

[android]
# نسخه‌های SDK/NDK پایدار که مشکل license ندارند
android.sdk = 34
android.ndk = 25b
android.minapi = 21
android.targetapi = 34
android.arch = arm64-v8a

# مجوزهای مورد نیاز
android.permissions = INTERNET

# خط زیر مهم است: به Buildozer می‌گوید SDK را خودش نصب نکند
# (ما در workflow دستی نصب می‌کنیم)
# android.auto_sdk = False

[buildozer]
log_level = 2
warn_on_root = 1
