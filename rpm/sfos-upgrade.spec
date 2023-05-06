Name:           sfos-upgrade
Summary:        Scripts for fail-safe upgrading of SailfishOS at the command line with logging
# The Git release tag format must adhere to just <version> since version 3.6.0.
# The <version> tag must adhere to semantic versioning, for details see
# https://semver.org/
Version:        3.11.0
# The <release> tag comprises one of {alpha,beta,rc,release} postfixed with a
# natural number greater or equal to 1 (e.g., "beta3") and may additionally be
# postfixed with a plus character ("+"), the name of the packager and a release
# number chosen by her (e.g., "rc2+jane4").  `{alpha|beta|rc|release}`
# indicates the expected status of the software.  No other identifiers shall be
# used for any published version, but for the purpose of testing infrastructure
# other nonsensual identifiers as `adud` may be used, which do *not* trigger a
# build at GitHub and OBS, when configured accordingly; mind the sorting
# (`adud` < `alpha`).  For details and reasons, see
# https://github.com/Olf0/sfos-upgrade/wiki/Git-tag-format
Release:        beta1
# The Group tag should comprise one of the groups listed here:
# https://github.com/mer-tools/spectacle/blob/master/data/GROUPS
Group:          Applications/System
Distribution:   SailfishOS
License:        LGPL-2.1-only
URL:            https://github.com/Olf0/%{name}
# Altering the `Vendor:` field breaks the update path on SailfishOS, see
# https://en.opensuse.org/SDB:Vendor_change_update#Disabling_Vendor_stickiness
Vendor:         olf
# The "Source0:" line below requires that the value of %%{name} is also the
# project name at GitHub and the value of %%{version} is also the name of a
# correspondingly set git-tag.
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Note that the rpmlintrc file shall be named so according to
# https://en.opensuse.org/openSUSE:Packaging_checks#Building_Packages_in_spite_of_errors
Source99:       %{name}.rpmlintrc
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to
# the Source tag(s):
# It only accepts a GIF or XPM file (a path is stripped to its basename) in the
# SOURCES directory (but not inside a tarball there)!  Successfully tested GIF89a
# and XPMv3, but an XPM icon results in bad visual quality and large file size.
# Hence only to be used, when the file (or a symlink to it) is put there:
#Icon:           up.256x256.gif
BuildArch:      noarch
Requires:       ssu
Requires:       sailfish-version
Requires:       curl

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

%if 0%{?_chum}
Title: sfos-upgrade
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
PackageIcon: %{url}/raw/master/.icon/up.256x256.png
Links:
  Homepage: https://openrepos.net/content/olf/%{name}
  Help: %{url}/issues
  Bugtracker: %{url}/issues
  Donation: https://openrepos.net/donate
%endif

%define _binary_payload w6.gzdio
%define _source_payload w6.gzdio

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp bin/* %{buildroot}%{_bindir}/

%files
%defattr(0755,root,root,-)
%{_bindir}/%{name}
%{_bindir}/post_%{name}
%{_bindir}/tidy_log-dupes

# Changelog format: https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/SF4VVE4NBEDQJDJZ4DJ6YW2DTGMWP23E/#6O6DFC6GDOLCU7QC3QJKJ3VCUGAOTD24
%changelog
* Thu Sep  9 1999 olf <Olf0@users.noreply.github.com> - 99.99.99
- See %{url}/releases

