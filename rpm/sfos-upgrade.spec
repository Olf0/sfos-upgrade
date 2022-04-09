Name:          sfos-upgrade
Summary:       Scripts for fail-safe upgrading of SailfishOS at the command line with logging
Version:       3.9.4
# Stop evaluating the Release tag content (only set it) and cease including it
# in git tags since v3.6.0, in order to satisfy SailfishOS-OBS' tar_git, see:
# https://github.com/MeeGoIntegration/obs-service-tar-git/blob/master/tar_git
# Consequently switch to a three field semantic versioning scheme for releases
# and their git tags.  Hence any changes to the spec file now always trigger an
# increase of the bug fix release number, i.e., the third field of the Version.
# The Release tag is now (ab)used to merely indicate the estimated release
# quality by setting it to {alpha,beta,rc,release} with a natural number >= 1
# directly appended (e.g. "beta3").  Note that no other identifiers shall be
# used.
Release:       release1
Group:         Applications/System
Distribution:  SailfishOS
License:       LGPL-2.1-only
URL:           https://github.com/Olf0/%{name}
# The "Source:" line requires that the value of %{name} is also the project
# name at GitHub and the value of %{version} is also the name of a
# correspondingly set git-tag.
# Alternative link, which also downloads ${projectname}-${tagname}.tar.gz:
# Source:      https://github.com/Olf0/%{name}/archive/%{version}.tar.gz
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

