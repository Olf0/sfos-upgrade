Name:          sfos-upgrade
Summary:       Scripts for safe and automated upgrading of SailfishOS with logging
Version:       3.6.4
# Stop evaluating the Release tag content (only set it) and cease including it in git tags since v3.6.0, 
# in order to satisfy OBS' git_tar.  Consequently switch to a three field semantic versioning scheme for
# releases and their git tags.
# Hence any changes to the spec file now always trigger an increase of the bug fix release number, i.e.
# the third field of the Version.
# But the Release tag is now (ab)used to merely indicate the estimated release quality by setting it
# to {alpha, beta, stable} with a natural number >= 1 directly appended (e.g. "beta3").  Note that
# no other identifiers shall be used.
Release:       stable4
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# rpmbuild (as of v4.14.1) handles the Icon tag awkwardly and in contrast to the Source tag(s):
# It only accepts a GIF or XPM file (successfully tested GIF89a and XPMv3) in the SOURCE directory
# (but not in the tarball)!  Hence only to be used, when the file is put there:
# Icon:         up.256x256.gif
BuildArch:     noarch
Requires:      ssu
Requires:      sailfish-version
Requires:      curl

%description
%{summary}
Usage: sfos-upgrade [<version>]
With a version number provided as parameter it sets SSU to this version and in release mode before upgrading.  This is the regular use case.
Without a version number it retrieves the one set for SSU to perform slightly relaxed checks, but does not alter SSU's settings for upgrading.

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp usr/bin/* %{buildroot}%{_bindir}/

%files
%defattr(0755,root,root,-)
%{_bindir}/%{name}
%{_bindir}/post_%{name}
%{_bindir}/tidy_log-dupes

