# sfos-upgrade
**Scripts for safe and automated upgrading of SailfishOS with logging**

Upgrading SailfishOS at the GUI (per *Settings -> SailfishOS updates*) provides very little information about its progress / process / success, beyond reading `/var/log/systemupdate.log` after the upgrade.  This can make troubleshooting issues hard.
Furthermore the GUI offers no control which SailfishOS version to upgrade to.Upgrading SailfishOS at the GUI (per *Settings -> SailfishOS updates*) provides very little information about its progress / process / success, beyond reading `/var/log/systemupdate.log` after the upgrade.  This can make troubleshooting issues hard.
Furthermore the GUI offers no control which SailfishOS version to upgrade to.

In contrast to that, Jolla's [guide how to upgrade SailfishOS at the command line]() offers full control, while lacking any logs or safety checks.
Furthermore it is tedious and error prone to issue critical commands manually at the command line.

**SFOS-upgrade** performs the steps to upgrade SailfishOS at the command line in an automated manner, while providing extensive safety measures plus full log output at the screen and in a log file.

**Safety measures:**
* Check for free space on root filesystem.
* Check for BTRFS allocation, if the root filesystem uses BTRFS.
* Check for correct and available SailfishOS versions.
* Automatically unapply all Patches, if Patchmanager is installed.
* Emit a warning when downgrading.

**Usage** (as root user):
* **sfos-upgrade.sh [<version>]**
   Without a version number as parameter it uses the one set per `ssu re <version>` (one can query the version set by using a simple `ssu re`).
   With a version number provided it always sets `ssu` to this version and in release mode.
* **sfos-upgrade.sh -h|--help**
   Emits a brief usage description.

When an upgrade succeeded, reboot and do not miss to run `post_sfos-upgrade` (as root) then!
Not running it will result in the huge upgrade log files (containing many duplicated lines) and may result in RPMs failing to install ("unmet dependency" errors) plus annoying messages from the store-client that an upgrade to the installed version is available.
In contrast to that, Jolla's [guide how to upgrade SailfishOS at the command line]() offers full control, while lacking any logs or safety checks.
Furthermore it is tedious and error prone to issue critical commands manually at the command line. 
**SFOS-upgrade** performs the steps to upgrade SailfishOS at the command line in an automated manner, while providing extensive safety measures plus full log output at the screen and in a log file. 
**Safety measures:**
* Check for free space on root filesystem.
* Check for BTRFS allocation, if the root filesystem uses BTRFS.
* Check for correct and available SailfishOS versions.
* Automatically unapply all Patches, if Patchmanager is installed.
* Emit a warning when downgrading. 
**Usage** (as root user):
* **sfos-upgrade.sh [<version>]**    Without a version number as parameter it uses the one set per `ssu re <version>` (one can query the version set by using a simple `ssu re`).    With a version number provided it always sets `ssu` to this version and in release mode.
* **sfos-upgrade.sh -h|--help**    Emits a brief usage description. 
When an upgrade succeeded, reboot and do not miss to run `post_sfos-upgrade` (as root) then!
Not running it will result in the huge upgrade log files (containing many duplicated lines) and may result in RPMs failing to install ("unmet dependency" errors) plus annoying messages from the store-client that an upgrade to the installed version is available.
