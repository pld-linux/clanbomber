Summary:	ClanBomber, the cool game that uses ClanLib
Summary(pl):	ClanBomber, super gierka wykorzystuj±ca ClanLib
Name:		clanbomber
Version:	1.02a
Release:	3
License:	GPL
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/clanbomber/%{name}-%{version}.tar.gz
# Source0-md5:	1f0347807ca70b7f9b48dd7972aea8d5
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:		%{name}-CXXFLAGS.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-DESTDIR2.patch
Patch4:		%{name}-hardcoded_paths.patch
URL:		http://clanbomber.sourceforge.net/
Requires:	ClanLib >= 0.5.0
BuildRequires:	ClanLib-devel >= 0.5.0
BuildRequires:	Hermes-devel
BuildRequires:	autoconf
BuildRequires:	automake
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
%patch3 -p0
%patch4 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
# note: RTTI is needed --- clanbomber uses exceptions!
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
%configure --datadir=/usr/share/games
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/games/clanlib

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog QUOTES README TODO
%attr(755,root,root) %{_bindir}/clanbomber
%{_datadir}/games/clanbomber
%{_applnkdir}/Games/Arcade/clanbomber.desktop
%{_pixmapsdir}/*
