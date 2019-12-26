Name:          sfos-upgrade
Summary:       Scripts for safe and automated upgrading of SailfishOS with logging
Version:       3.6.0
# Stop evaluating the "Release:" field (per %{release}) and cease including it in git tags since v3.6.0, 
# in order to satisfy OBS and consequently switching to a three field semantic versioning scheme for
# releases and their tags. 
# Hence changes to the spec file now always trigger an increase of the bug fix release number (third field).
# But the "Release:" field is now (ab)used to indicate the estimated release quality by setting it to 
# {alpha, beta, delta, epsilon}; note that "gamma" must not be used (as it breaks the alphabetic order).
Release:       delta
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        https://github.com/Olf0/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
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
%setup -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp usr/bin/* %{buildroot}%{_bindir}/

%files
%defattr(0755,root,root,-)
%{_bindir}/%{name}
%{_bindir}/post_%{name}
%{_bindir}/tidy_log-dupes

