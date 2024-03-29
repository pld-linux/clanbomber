Summary:	ClanBomber, the cool game that uses ClanLib
Summary(pl.UTF-8):	ClanBomber, super gierka wykorzystująca ClanLib
Name:		clanbomber
Version:	1.02a
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/clanbomber/%{name}-%{version}.tar.gz
# Source0-md5:	1f0347807ca70b7f9b48dd7972aea8d5
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:		%{name}-CXXFLAGS.patch
Patch2:		%{name}-DESTDIR.patch
Patch3:		%{name}-DESTDIR2.patch
Patch4:		%{name}-hardcoded_paths.patch
Patch5:		%{name}-assert.patch
Patch6:		%{name}-gcc33.patch
URL:		http://clanbomber.sourceforge.net/
BuildRequires:	ClanLib-devel >= 0.5.0
BuildRequires:	Hermes-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
Requires:	ClanLib >= 0.5.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClanBomber is very nice and playable Bomberman/Dynablaster clone. It
has multiplayer support (8 players), but not yet network support. You
must have try it! :-)

%description -l pl.UTF-8
ClanBomber to bardzo fajna i wciągająca gierka, zbliżona do
Bombermana/Dynablastera. Można grać w kilku (max. 8) graczy, ale
niestety nie poprzez sieć (jeszcze!). Koniecznie musisz ją wypróbować!

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
# note: RTTI is needed --- clanbomber uses exceptions!
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
%configure \
	--datadir=/usr/share/games
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_datadir}/games/clanlib

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog QUOTES README TODO
%attr(755,root,root) %{_bindir}/clanbomber
%{_datadir}/games/clanbomber
%{_desktopdir}/clanbomber.desktop
%{_pixmapsdir}/*
