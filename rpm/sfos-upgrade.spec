Name:       	sfos-upgrade
Summary:    	Scripts for safe and automated upgrading of SailfishOS with logging
Version:    	0.3
Release:    	1
Group:      	System/Base
Distribution:	SailfishOS
Vendor:     	olf
Packager:   	olf
License:    	MIT
URL:        	https://github.com/Olf0/%{name}
Source:     	%{name}-%{version}-%{release}.tar.gz
Source1:    	https://github.com/Olf0/%{name}/archive/%{version}-%{release}.tar.gz
BuildArch:  	noarch
Requires:   	ssu
Requires:   	sailfish-version

%description
%{summary}

%prep
%setup -n %{name}-%{version}-%{release}

%build

%install
mkdir -p %{buildroot}%{_bindir}
cp usr/bin/* %{buildroot}%{_bindir}/

%files
%defattr(0754,root,root,-)
%{_bindir}/sfos-upgrade
%{_bindir}/post_sfos-upgrade
%{_bindir}/tidy_log-dupes

