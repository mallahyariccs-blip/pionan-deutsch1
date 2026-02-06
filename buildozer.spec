[app]
title = PIONAN Deutsch
package.name = pimon
package.domain = org.test
source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv
version = 0.1
requirements = python3, kivy
orientation = portrait

[android]
# این خط کلیدی است: به Buildozer می‌گوید SDK را خودش نصب نکند
android.auto_sdk = 0
# تنظیم مسیر SDK به یک مسیر خیالی تا دانلود نشود
# android.sdk_path = /fake/path
# android.ndk_path = /fake/path

# تعیین نسخه هدف (ضروری است)
android.minapi = 21
android.maxapi = 34
android.targetapi = 34
android.arch = arm64-v8a
android.permission = INTERNET

[buildozer]
log_level = 2
