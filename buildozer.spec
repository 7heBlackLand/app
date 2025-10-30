[app]
title = MyKivyApp
package.name = mykivyapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
osx.python_version = 3
fullscreen = 0
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = ~/.buildozer/android/platform/android-sdk
android.arch = arm64-v8a
android.permissions = INTERNET
log_level = 2
android.build_tools_version = 36.0.0
p4a.branch = master
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
android.enable_androidx = True
