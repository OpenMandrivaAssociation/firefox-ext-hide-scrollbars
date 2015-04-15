Summary:	Firefox extension for hiding scrollbars
Name:		firefox-ext-hide-scrollbars
Version:	0.2
Release:	1
License:	GPLv2+
Group:		Networking/WWW
Url:		https://addons.mozilla.org/en-US/firefox/addon/hidescrollbars
Source0:	https://addons.mozilla.org/firefox/downloads/latest/494068/addon-494068-latest.xpi
Buildarch:	noarch

BuildRequires:	firefox-devel
Requires:	firefox >= %{firefox_version}

%description
Firefox extension for hiding scrollbars

%prep
%setup -qc

%install
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
	hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
	echo "Failed to find plugin hash."
	exit 1
fi
extdir="%{firefox_extdir}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%files
%{firefox_extdir}/*
