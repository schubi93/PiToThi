# Script to check for ping on dorm room

## Dependencies

If needed, install `pip3` via `sudo apt install python3-pip`

Afterwards, install dependencies:

```shell
pip3 install thingspeak
pip3 install pythonping
```

## Autostart

Edit ` /etc/xdg/autostart/RPi-infoscreen.desktop` with

```
[Desktop Entry]
Type=Application
Name=RPi-ping
Comment=Testing ping and sending it to Thingspeak
NoDisplay=false
Exec=/usr/bin/lxterminal -e $(GIT_ROOT_DIR)/src/start_app.sh
NotShowIn=GNOME;KDE;XFCE;
```

## Authors

* **Philipp Schubaur** - *Initial work*

## License

This project is licensed under the GNU GPLv3 License