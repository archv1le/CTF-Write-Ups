# Obedient Cat
- Tags: picoCTF 2021, Reverse Engineering, android
- Author: LOIC SHEMA
- Description: You will find the flag after analysing this apk. Download here.
- Link to the question: https://play.picoctf.org/practice/challenge/381

# Solution
- To solve this question you need to download the following file and open it using JADX or another tool to decompile APK file.
- There you will see a lot of directories. Go to "com", then to "example.timer" and then to BuildConfig file.
```
package com.example.timer;

/* loaded from: classes3.dex */
public final class BuildConfig {
    public static final String APPLICATION_ID = "com.example.timer";
    public static final String BUILD_TYPE = "debug";
    public static final boolean DEBUG = Boolean.parseBoolean("true");
    public static final int VERSION_CODE = 1;
    public static final String VERSION_NAME = "picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}";
}
```
- Flag is in the string VERSION_NAME.

```
picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}
```
