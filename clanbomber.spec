Summary:	ClanBomber, the cool game that uses ClanLib.
Summary(pl):	ClanBomber, super gierka wykorzystuj±ca ClanLib.
Name:		clanbomber 
Version:	0.98c
Release:	1
Copyright:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	http://www.clanbomber.de/files/%{name}-%{version}.tar.gz
Source1:	clanbomber.desktop
Patch0:		clanbomber-paths.patch
URL:		http://www.clanbomber.de/
Requires:	ClanLib >= 0.2.2
BuildRequires:	ClanLib-devel >= 0.2.2
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
ClanBomber to bardzo fajna i wci±gaj±ca gierka, zbli¿ona do
Bombermana/Dynablastera. Mo¿na graæ w kilku (max. 8) graczy, ale 
niestety nie poprzez sieæ (jeszcze!). Koniecznie musisz j± wypróbowaæ!

%prep
%setup -q
%patch0 -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS -fno-implicit-templates"
LDFLAGS="-s"
export CXXFLAGS LDFLAGS
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT%{_prefix}

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
