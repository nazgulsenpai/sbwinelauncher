# Scarlet Blade Vendetta WINE Launcher for Linux or MacOS
Launcher for logging in and booting Scarlet Blade Vendetta on WINE using Linux or MacOS. The script logs in through HTTP (like the official launcher), automatically patches XignCode with sbxigncode (code found https://github.com/nazgulsenpai/sbxigncode) with a x3.xem built to be compatible with WINE.

Tested on WINE 4.0 on Mint 19 and works flawlessly.  
![Screenshot](https://github.com/nazgulsenpai/sblinuxlauncher/raw/master/sbv_on_mint.png)
![Screenshot](https://github.com/nazgulsenpai/sblinuxlauncher/raw/master/sbv_on_macos_sierra.png)

# 1) Install WINE (tested 4.0)
Setup WINE using your distro's package manager, as well as winetricks. Use winetricks to install VC++2015 runtime:  
winetricks vcrun2015

# 2) Download the Scarlet Blade Vendetta Installer
http://sb.vendettagn.com

# 3) Run the Stock Launcher
Run the stock launcher to patch all of your files to the latest versions

# 4) Place sb.py in your Scarlet Blade Vendetta installation folder
On my system it was  
/home/username/.wine/drive_c/Vendetta Gaming Network/Scarlet Blade Vendetta/

# 5) Run sb.py
chmod +x ./sb.py  
./sb.py [username] [password]  
If you don't provide a username or password you will be prompted.


