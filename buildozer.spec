[app]
title = Shield360
package.name = shield360
package.domain = com.shield360.app

source.dir =.
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True

p4a.branch = master

[buildozer]
log_level = 2
warn_on_root = 1
