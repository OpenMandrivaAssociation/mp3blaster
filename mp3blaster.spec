Summary: 	Console based MP3 player
Name: 		mp3blaster
Version: 	3.2.3
Release: 	%mkrel 4
License: 	GPL
Group: 		Sound
URL:		http://mp3blaster.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/mp3blaster/%{name}-%{version}.tar.bz2
Requires:	mysql-client
Requires:	mysql-shared
BuildRequires:	mysql-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lirc-devel
BuildRequires:	ncurses-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	sidplay-devel
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot

%description
MP3Blaster is a text console based program for playing mainly mp3
audio files. It is very interactive, and has a great list of
features. Its playlist can be divided in albums or categories
(called 'groups'), which allows for very sophisticated playback
orders.

%prep

%setup -q

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export LDFLAGS=" -I%{_includedir} -I%{_includedir}/mysql -lmysqlclient"

%configure2_5x \
    --with-mysql \
    --with-mysql-includes=%{_includedir}/mysql \
    --with-mysql-libs=%{_libdir} \
    --with-lirc \
    --with-oggvorbis \
    --with-sidplay \

%make

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall

# cleanup
rm -f %{buildroot}%{_datadir}/mp3blaster/charmap/chargen.c
rm -f %{buildroot}%{_datadir}/mp3blaster/charmap/maketbl.c

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS CREDITS ChangeLog FAQ INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
