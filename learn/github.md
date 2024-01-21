"Push" your work up to GitHub for backup. By creating "commits", which you can think of as versioned checkpoints in your workspace, you are not at risk of losing your work. It's easy to revert back to an old version or to restore your entire workspace on a different computer.
Select the View menu and then SCM (Source Control Management)
Notice the files listed under Changes. These are files you've made modifications to since your last backup.
Move your mouse's cursor over the word changes and notice the + symbol that appears. Click that plus symbol to add all changes to the next backup. You will now see these listed under "Staged Changes".
If you do not want to backup all changed files, you can select them individually. For this course you're encouraged to back everything up.
In the Message box, give a brief description of what you've changed and are backing up. This will help you find a specific backup (called a "commit") if needed.
Open the View menu and select Command Palette, the shortcut for this menu is: CTRL SHIFT P
Begin typing in: Git: Push to... and press Enter once it is the first option.
Select the backup remote that is your personal workspace on GitHub. If you do not see backup listed, see the instructions below on Setup Backup Course Material Repository.
You may see a spinning "refresh" icon in your status bar at the bottom of VSCode. Unless an error backing up occurs, you will not see any confirmation.