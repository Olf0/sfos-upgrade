Name:       	sfos-upgrade
Summary:    	Scripts for safe and automated upgrading of SailfishOS with logging
Version:    	0.1
Release:    	1
Group:      	System/Base
Distribution:	SailfishOS
Vendor:     	olf
Packager:   	olf
License:    	MIT
URL:        	https://github.com/Olf0/%{name}
Source0:    	%{name}-%{version}-%{release}.tar.gz
Source1:    	https://github.com/Olf0/%{name}/archive/%{version}-%{release}.tar.gz
BuildArch:  	noarch
Requires:   	ssu
Requires:   	sailfish-version

%description
%{summary}

%prep
%setup -T -b 0 -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp usr/bin/* %{buildroot}%{_bindir}/

%files
%defattr(-,root,root,0754)
%{_bindir}/sfos-upgrade
%{_bindir}/post_sfos-upgrade
%{_bindir}/tidy_log-dupes
