Summary:	ClanBomber, the cool game that uses ClanLib.
Summary(pl):	ClanBomber, super gierka wykorzystuj±ca ClanLib.
Name:		clanbomber
Version:	0.98
Release:	1
Copyright:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Source:		http://www.fischlustig.de/clanbomber/%{name}-%{version}.tar.gz
Patch:		clanbomber-paths.patch
URL:		http://www.fischlustig.de/clanbomber/
Requires:	ClanLib
BuildRequires:	ClanLib-devel = 0.1.16
BuildRequires:	Hermes-devel
BuildRequires:	zlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
ClanBomber is very nice and playable Bomberman/Dynablaster clone. It has multiplayer
support (8 players), but not yet network support. You must have try it! :-)

%description -l pl
ClanBomber to bardzo fajna i wci±gaj±ca gierka, zbli¿ona do
Bombermana/Dynablastera. Mo¿na graæ w kilku (max. 8) graczy, ale niestety nie 
poprzez sieæ (jeszcze!). Koniecznie musisz j± wypróbowaæ!

%define _prefix	$RPM_BUILD_ROOT/usr/X11R6

%prep
%setup -q
%patch -p1

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install 

strip --strip-unneeded $RPM_BUILD_ROOT/usr/X11R6/bin/*
gzip -9nf AUTHORS ChangeLog QUOTES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/clanbomber
/usr/X11R6/share/clanbomber
%doc AUTHORS.gz ChangeLog.gz QUOTES.gz README.gz TODO.gz
