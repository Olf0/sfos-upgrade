Name:          sfos-upgrade
Summary:       Scripts for safe and automated upgrading of SailfishOS with logging
Version:       3.0
Release:       2
Group:         System/Base
Distribution:  SailfishOS
Vendor:        olf
Packager:      olf
License:       MIT
URL:           https://github.com/Olf0/%{name}
Source:        %{name}-%{version}-%{release}.tar.gz
Source1:       https://github.com/Olf0/%{name}/archive/%{version}-%{release}.tar.gz
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
%setup -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp usr/bin/* %{buildroot}%{_bindir}/

%files
%defattr(0755,root,root,-)
%{_bindir}/%{name}
%{_bindir}/post_%{name}
%{_bindir}/tidy_log-dupes

