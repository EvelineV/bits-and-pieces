#/bin/bash/
# slack not allowed to send notifications in the tray icon
sudo -i
cd /usr/lib/slack/resources/app.asar.unpacked/src/static
sudo mv slack-taskbar-highlight.png slack-taskbar-highlight-backup.png
sudo mv slack-taskbar-unread.png slack-taskbar-unread-backup.png
sudo cp slack-taskbar-rest.png slack-taskbar-highlight.png
sudo cp slack-taskbar-rest.png slack-taskbar-unread.png
cd
exit

