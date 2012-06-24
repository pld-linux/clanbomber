Summary:	ClanBomber, the cool game that uses ClanLib.
Summary(pl):	ClanBomber, super gierka wykorzystuj�ca ClanLib.
Name:		clanbomber 
Version:	0.98
Release:	1
Copyright:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	http://www.fischlustig.de/clanbomber/%{name}-%{version}.tar.gz
Source1:	clanbomber.desktop
Patch0:		clanbomber-paths.patch
Patch1:		clanbomber-DESTDIR.patch
URL:		http://www.fischlustig.de/clanbomber/
Requires:	ClanLib
BuildRequires:	ClanLib-devel = 0.1.16
BuildRequires:	Hermes-devel
BuildRequires:	XFree86-devel
BuildRequires:	svgalib-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix 	/usr/X11R6

%description
ClanBomber is very nice and playable Bomberman/Dynablaster clone. 
It has multiplayer support (8 players), but not yet network support. 
You must have try it! :-)

%description -l pl
ClanBomber to bardzo fajna i wci�gaj�ca gierka, zbli�ona do
Bombermana/Dynablastera. Mo�na gra� w kilku (max. 8) graczy, ale 
niestety nie poprzez sie� (jeszcze!). Koniecznie musisz j� wypr�bowa�!

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-implicit-templates"
LDFLAGS="-s"
export CXXFLAGS LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/applnk/Games
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applnk/Games

gzip -9nf AUTHORS ChangeLog QUOTES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,QUOTES,README,TODO}.gz

%attr(755,root,root) %{_bindir}/clanbomber
%{_datadir}/clanbomber
%{_datadir}/applnk/Games/clanbomber.desktop
