# sfos-upgrade
### Scripts for safe and automated upgrading of SailfishOS with logging
<br />

Upgrading SailfishOS at the GUI (per *Settings -> SailfishOS updates*) provides very little information about its progress / process / success, beyond reading `/var/log/systemupdate.log` after the upgrade.  This can make troubleshooting issues hard.<br />
Furthermore the GUI offers no control which SailfishOS version to upgrade to.

In contrast to that, Jolla's [guide how to upgrade SailfishOS at the command line](https://jolla.zendesk.com/hc/en-us/articles/360005795474) offers full control, while lacking any logs or safety checks.<br />
And it is tedious and error prone to issue multiple critical commands manually at the command line.

**sfos-upgrade** performs the steps to upgrade SailfishOS at the command line in an automated manner, while providing extensive safety measures plus full log output at the screen and in a log file.<br />
<br />

Safety measures:

* Check for free space on root filesystem.
* Check for BTRFS allocation, if the root filesystem uses BTRFS.
* Check for upgrading to a correct and available SailfishOS version.
* Check for "jumping over" a stop release (since v0.3).
* Automatically unapply all Patches, if Patchmanager is installed.
* Emit a warning when downgrading.
<br />

Usage (as root user):

* **sfos-upgrade [\<version\>]**<br />
   With a version number provided as parameter it sets SSU to this version and in release mode before upgrading.  This is the regular use case.<br />
   Without a version number provided it uses the one set per `ssu re <version>` to upgrade to (one can query the version set by using a simple `ssu re`).
* **sfos-upgrade -h|--help**<br />
   Emits a brief usage description.

When an upgrade succeeded, reboot and do not miss to run **post_sfos-upgrade** (as root) then!  
Not running it will result in the huge upgrade log files (containing many duplicated lines) and may result in RPMs failing to install ("unmet dependency" / "Fatal error: nothing provides X needed by Y" errors) plus annoying notifications from the store-client that an upgrade to the installed version is available.

Logs are originally written to `/var/log/systemupdate_*.log-dupes.txt` and tidied by **tidy_log-dupes** (which is called by **post_sfos-upgrade**) to `/var/log/systemupdate_*.log.txt`.
