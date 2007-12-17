%define name xmms-scrobbler
%define version 0.4.0
%define release %mkrel 1

Summary:	A xmms plugin that builds a profile of your musical taste
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0: http://xmms-scrobbler.sommitrealweird.co.uk/download/%{name}-%{version}.tar.bz2
License:	GPL
Group:		Sound
Url:		http://xmms-scrobbler.sommitrealweird.co.uk/
BuildRequires:	musicbrainz-devel
BuildRequires:	curl-devel
BuildRequires:	xmms-devel
BuildRequires:	taglib-devel

%description
Audioscrobbler builds a profile of your musical taste using a plugin
for XMMS. Plugins send the name of every song you play to the
Audioscrobbler server, which updates your musical profile with the new
song. Every person with a plugin has their own page on this site which
shows their listening statistics. The system automatically matches you
to people with a similar music taste, and generates personalised
recommendations.


%prep
%setup -q

%build
%configure2_5x --disable-bmp-plugin
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f %buildroot%{_libdir}/*/General/lib*_scrobbler.la
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL KnownIssues NEWS README README.tags TODO
%{_libdir}/xmms/General/libxmms_scrobbler.so


