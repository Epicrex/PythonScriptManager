⚠ Still being worked on

# Table Of Content
- [About PSM](#about-psm-)
- [PSM Setup](#psm-setup-)
- [Features](#features-)
- [Change PSM call command](#change-psm-call-command-)
- [Libraries used in PSM](#libraries-used-in-psm-)

PSM = Python Script Manager

# About PSM [^](#table-of-content-)


_All the rights to this code are owned fully by its author, Sidney._

# PSM Setup [^](#table-of-content-)
_~ 3 min setup time_

```
ℹ Nothing is required for PSM to work.
I built it in such a way, that it doesn't require things like:

Installing Python, Admin Rights and Installing or starting any exe.
```


### Download PSM
1. Download the PSM zip and unzip it
2. Move the unzipped folder to any desired location on your computer

### Add Environment Variable
1. Press `Win + R` and enter `rundll32.exe sysdm.cpl,EditEnvironmentVariables` (You can also open th Environment Variables window per Windows search bar)
2. Inside the top box also known as the User variables, select the variable called `Path` and click `Edit`
3. Click `New` and paste the path to the "py_scripts" folder you noted down before
4. Finally, click `Ok` and `Ok` again

### You're Done
PSM is ready. You can now open a terminal form anywhere on your computer and type the command `psm`, which will start the script.

# Features [^](#table-of-content-)

# Change PSM call command [^](#table-of-content-)
If you want to change the command that calls the PSM script which is `psm` per default, simply rename the `psm.bat` file. This file is located at `PSM\psm_work_directory\py_scripts`.

# Libraries used in PSM [^](#table-of-content-)
These are all the libraries used in PSM (In total they are only 3 mb big)
```
asgiref==3.5.2
async-timeout==4.0.2
atlassian-python-api==3.25.0
certifi==2022.5.18.1
charset-normalizer==2.0.12
colorama==0.4.4
Deprecated==1.2.13
Django==4.1
idna==3.3
image==1.5.33
oauthlib==3.2.0
packaging==21.3
Pillow==9.2.0
pyparsing==3.0.9
pyping==0.0.6
pytesseract==0.3.10
pytube==12.1.0
PyYAML==6.0
redis==4.3.4
requests==2.27.1
requests-oauthlib==1.3.1
six==1.16.0
spotipy==2.20.0
sqlparse==0.4.2
tzdata==2022.1
urllib3==1.26.9
wrapt==1.14.1
```
