# sfos-upgrade
### Scripts for fail-safe and semi-automated upgrading of SailfishOS at the command line with logging

<br />

Upgrading SailfishOS at the GUI (per *Settings -> SailfishOS updates*) provides very little information about its progress / process / success, beyond reading `/var/log/systemupdate.log` after an upgrade.  This can make troubleshooting issues hard.<br />
Furthermore the GUI offers no control which SailfishOS version to upgrade to.

In contrast to that, Jolla's [guide how to upgrade SailfishOS at the command line](https://docs.sailfishos.org/Support/Help_Articles/Updating_Sailfish_OS/#update-using-the-command-line) offers full control, while lacking any logs or safety checks.<br />
Furthermore it is tedious and error prone to issue multiple, critical commands manually at the command line.

**sfos-upgrade** performs the steps to upgrade SailfishOS at the command line in an automated manner, while providing extensive safety measures plus full log output at the screen and in a log file.<br />
<br />

Safety measures:

* Check free space on the root filesystem.
* Check BTRFS allocation, if the root filesystem uses BTRFS.
* Check battery state (since v1.0).
* Check if upgrading to a correct and available SailfishOS version.
* Check if omitting (i.e., "jumping over") a [stop release](https://docs.sailfishos.org/Support/Releases/) (since v0.3).
* Automatically unapply all Patches, if Patchmanager 2 is installed.
* Stop systemd services for cron, btrfs-balance-checker etc. (since v2.2).
* Terminate running processes, which may disturb upgrading SailfishOS (since v2.7).
* Disable all OpenRepos' repositories, when upgrading from a SailfishOS version below 1.0.4 (since v0.4).
* Emit a warning when downgrading.
* Prevent downgrades, which would likely break the SailfishOS installation (since v3).
<br />

Usage (as root user):

* **sfos-upgrade [\<version\>]**<br />
  With a version number provided as parameter, it sets SSU to this version and in release mode before upgrading to this SailfishOS version.  This is the regular use case.<br />
  Without a version number, it retrieves the one set for SSU to perform slightly relaxed checks, but does not alter SSU's settings for upgrading.  Hence the version to upgrade to and SSU's "release mode" have to be set (per e.g., `ssu re <version>`) *before* executing `sfos-upgrade` without a parameter.

* **sfos-upgrade --verify**<br />
  Performs a "samegrade" operation, i.e. checks if the recent versions of all available RPMs are installed and updates or installs them accordingly.<br />
  This option was introduced with v3.7.0.

* **sfos-upgrade -?|--help**<br />
  Emits a brief usage description.

When an upgrade succeeded, reboot, and do not miss to run **post_sfos-upgrade** (as root) then!<br />
When **sfos-upgrade** failed, run **post_sfos-upgrade** (as root) *before* rebooting and then run **sfos-upgrade** again.<br />
Not running **post_sfos-upgrade** (in either case) will result in an huge upgrade log file (containing many duplicate entries), plus may result (as any SailfishOS upgrade at the command line without tidying efforts afterwards) in RPMs failing to install (with "unmet dependency" / "Fatal error: nothing provides X needed by Y" errors) and annoying notifications from the store-client that an upgrade to the installed version is available.

Logs are originally written to `/var/log/systemupdate_*.log-dupes.txt` and tidied by **tidy_log-dupes** (which is called by **post_sfos-upgrade**) to `/var/log/systemupdate_*.log.txt`.<br />
<br />

Notes:

* Built RPMs are available in the [release section](https://github.com/Olf0/sfos-upgrade/releases) and for easy installation on SailfishOS at [OpenRepos](https://openrepos.net/content/olf/sfos-upgrade).
* All operations comprise the RPMs from *all* enabled repositories, because that is **version --dup**'s implicit behaviour (as with **pkcon upgrade-system** and **zypper dist-upgrade** / **zypper dup** too, all utilising **libzypp**).
* When upgrading from a long outdated SailfishOS version (e.g., after a "factory reset"), **sfos-upgrade** eases and speeds up the process of upgrading to a recent SailfishOS release via consecutively installing all "stop releases" on the way.<br />
Simply run `sfos-upgrade <intended version>`, reboot, and repeat: it will guide you through all [stop releases](https://docs.sailfishos.org/Support/Releases/).<br />
When upgrading to SailfishOS releases < 4.1.0, you may omit running `post_sfos-upgrade` between consecutive SailfishOS upgrades (but do reboot each time!).  But you shall run it after having upgraded to any SailfishOS release ≥ 4.1.0 or the ultimately intended version.
* To ensure that a SailfishOS installation is complete and up to date, use `sfos-upgrade --verify`; this will "samegrade" to the installed version, which is as close as one can get to the `version --verify` lost [since SailfishOS 2.2.1](https://together.jolla.com/question/187243/changelog-221-nurmonjoki/#187243-sailfish-version) (which only checked for missing or not up-to-date RPMs, while "samegrading" will also install them) without **zypper**.  With it (per `pkcon install zypper`), a `zypper refresh && zypper verify --dry-run` comes closer to what `version --verify` did (only checking).  While **zypper** can also be used for up-/down-/same-grading, that is [rather a "last resort"-measure than the primary recommendation](https://together.jolla.com/question/117335/verify-integrity-of-installed-packages-after-upgrade-or-later/?answer=214905#post-id-214905), hence use **sfos-upgrade** for that.
* **sfos-upgrade** supports [all public SailfishOS releases](https://coderus.openrepos.net/whitesoft/sailversion) and should work fine for upgrading from / to any release (it accepts only version numbers of at least 1.0.0.0 at the command line, but omits this check when called without a parameter after utilising **ssu** to pre-set a version to upgrade to).
* **sfos-upgrade** is simply a frontend for `ssu re` and `version --dup`, performing a multitude of checks before initiating the upgrade proper, while **post_sfos-upgrade** carries out the "Final clean up" steps from [Jolla's manual upgrade guide](https://docs.sailfishos.org/Support/Help_Articles/Updating_Sailfish_OS/#update-using-the-command-line) plus an also necessary `pkcon refresh`, which some seem to omit when upgrading manually at the command line (often running into aforementioned issues later, then).
