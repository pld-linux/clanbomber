Summary:	ClanBomber, the cool game that uses ClanLib
Summary(pl):	ClanBomber, super gierka wykorzystuj±ca ClanLib
Name:		clanbomber 
Version:	1.01
Release:	1
License:	GPL
Group:		Games
Group(pl):	Gry
Source0:	http://www.clanbomber.de/files/%{name}-%{version}.tar.gz
Source1:	clanbomber.desktop
Patch1:		clanbomber-CXXFLAGS.patch
Patch2:		clanbomber-DESTDIR.patch
URL:		http://www.clanbomber.de/
Requires:	ClanLib >= 0.4.3
BuildRequires:	ClanLib-devel >= 0.4.3
BuildRequires:	Hermes-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClanBomber is very nice and playable Bomberman/Dynablaster clone. It
has multiplayer support (8 players), but not yet network support. You
must have try it! :-)

%description -l pl
ClanBomber to bardzo fajna i wci±gaj±ca gierka, zbli¿ona do
Bombermana/Dynablastera. Mo¿na graæ w kilku (max. 8) graczy, ale
niestety nie poprzez sieæ (jeszcze!). Koniecznie musisz j± wypróbowaæ!

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
aclocal
automake
autoconf
CXXFLAGS="$RPM_OPT_FLAGS -fno-implicit-templates" # note: RTTI is needed --- clanbomber uses exceptions!
LDFLAGS="-s"
export CXXFLAGS LDFLAGS
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games

gzip -9nf AUTHORS ChangeLog QUOTES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/clanbomber
%{_datadir}/clanbomber
%{_applnkdir}/Games/clanbomber.desktop
