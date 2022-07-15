Name:          sfos-upgrade
Summary:       Scripts for fail-safe upgrading of SailfishOS at the command line with logging
# The Git release tag format must adhere to just <version> since version 3.6.0.
# The <version> field adheres to semantic versioning and the <release> field 
# is comprised of {alpha,beta,rc,release} postfixed with a natural number
# greater or equal to 1 (e.g. "beta3").  For details and reasons, see
# https://github.com/Olf0/sfos-upgrade/wiki/Git-tag-format
Version:       3.9.11
Release:       release4
Group:         Applications/System
Distribution:  SailfishOS
License:       LGPL-2.1-only
URL:           https://github.com/Olf0/%{name}
# Altering the `Vendor:` field breaks the update path on SailfishOS, see
# https://en.opensuse.org/SDB:Vendor_change_update#Disabling_Vendor_stickiness
Vendor:        olf
# These "Source:" lines below require that the value of ${name} is also the
# project name at GitHub and the value of ${version} is also the name of a
# correspondingly set git-tag.
# Alternative links, which also download ${projectname}-${tagname}.tar.gz:
# Source:      https://github.com/Olf0/${name}/archive/${version}.tar.gz
# Source:      https://github.com/Olf0/${name}/archive/refs/tags/${version}.tar.gz
Source:        https://github.com/Olf0/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to
# the Source tag(s):
# It only accepts a GIF or XPM file (a path is stripped to its basename) in the
# SOURCES directory (but not inside a tarball there)!  Successfully tested GIF89a
# and XPMv3, but an XPM icon results in bad visual quality and large file size.
# Hence only to be used, when the file (or a symlink to it) is put there:
#Icon:          up.256x256.gif
BuildArch:     noarch
Requires:      ssu
Requires:      sailfish-version
Requires:      curl

%define orn_url https://openrepos.net/content/olf/sfos-upgrade

# This description section includes metadata for SailfishOS:Chum, see
# https://github.com/sailfishos-chum/main/blob/main/Metadata.md
%description
Scripts for fail-safe and semi-automated upgrading of SailfishOS at the command
line with logging

Usage: sfos-upgrade [<version>|--verify|--help]

With a version number provided as parameter it sets SSU to this version and in
release mode before upgrading.  This is the regular use case.

Without a version number it retrieves the one set for SSU to perform slightly
relaxed checks, but does not alter SSU's settings for upgrading.

%if "%{?vendor}" == "chum"
PackageName: sfos-upgrade
Type: console-application
DeveloperName: olf (Olf0)
Categories:
 - System
 - Utility
 - Settings
 - PackageManager
 - ConsoleOnly
Custom:
  Repo: %{url}
Icon: %{url}/raw/master/icon/up.256x256.png
Url:
  Homepage: %{orn_url}
  Help: %{orn_url}#comments
  Bugtracker: %{url}/issues
%endif

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp usr/bin/* %{buildroot}%{_bindir}/

%files
%defattr(0755,root,root,-)
%{_bindir}/%{name}
%{_bindir}/post_%{name}
%{_bindir}/tidy_log-dupes

