## Note; I have not yet verified whether the ufw setting is a enough security measure.

## How to use this

1. Enter the settings up to line 17 in "ApSetup.py" as you like.
1. Run "ApSetup.py" as root user.
```bash
sudo su -
python3 ApSetup.py
```

## How to activate the Wifi access point
- After you run "ApSetup.py", restart Raspberry PI.
- You can use following command to activate the Wifi access point in both Raspberry Pi OS and Ubuntu.
```bash
sudo systemctl restart hostapd
```
