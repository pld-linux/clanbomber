Summary:	ClanBomber, the cool game that uses ClanLib
Summary(pl):	ClanBomber, super gierka wykorzystuj�ca ClanLib
Name:		clanbomber 
Version:	1.02a
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://prdownloads.sourceforge.net/clanbomber/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch1:		%{name}-CXXFLAGS.patch
Patch2:		%{name}-DESTDIR.patch
URL:		http://clanbomber.sourceforge.net/
Requires:	ClanLib >= 0.5.0
BuildRequires:	ClanLib-devel >= 0.5.0
BuildRequires:	Hermes-devel
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ClanBomber is very nice and playable Bomberman/Dynablaster clone. It
has multiplayer support (8 players), but not yet network support. You
must have try it! :-)

%description -l pl
ClanBomber to bardzo fajna i wci�gaj�ca gierka, zbli�ona do
Bombermana/Dynablastera. Mo�na gra� w kilku (max. 8) graczy, ale
niestety nie poprzez sie� (jeszcze!). Koniecznie musisz j� wypr�bowa�!

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
rm -f missing
aclocal
autoconf
automake -a -c
# note: RTTI is needed --- clanbomber uses exceptions!
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Games/Arcade,%{_pixmapsdir}}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/Arcade
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS ChangeLog QUOTES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/clanbomber
%{_datadir}/clanbomber
%{_applnkdir}/Games/Arcade/clanbomber.desktop
%{_pixmapsdir}/*
