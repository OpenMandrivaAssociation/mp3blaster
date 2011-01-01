Summary: 	Console based MP3 player
Name: 		mp3blaster
Version: 	3.2.5
Release: 	%mkrel 6
License: 	GPLv2+
Group: 		Sound
URL:		http://mp3blaster.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/mp3blaster/%{name}-%{version}.tar.gz
Patch0:		mp3blaster-3.2.5-deb-02_bool.patch
Patch1:		mp3blaster-3.2.5-deb-03_endian.patch
Patch2:		mp3blaster-3.2.5-deb-04_memleak.patch
Patch3:		mp3blaster-3.2.5-deb-05_macro.patch
Patch4:		mp3blaster-3.2.5-deb-06_man.patch
Patch5:		mp3blaster-3.2.5-deb-07_fix_ogg.patch
Patch6:		mp3blaster-3.2.5-deb-08_fix_ftbfs_const_char.patch
Requires:	mysql-client
Requires:	mysql-shared
BuildRequires:	mysql-devel
BuildRequires:	libstdc++-devel
BuildRequires:	lirc-devel
BuildRequires:	ncurses-devel
BuildRequires:	oggvorbis-devel
BuildRequires:	sidplay-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
MP3Blaster is a text console based program for playing mainly mp3
audio files. It is very interactive, and has a great list of
features. Its playlist can be divided in albums or categories
(called 'groups'), which allows for very sophisticated playback
orders.

%prep

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

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
rm -rf %{buildroot}

%makeinstall

# cleanup
rm -f %{buildroot}%{_datadir}/mp3blaster/charmap/chargen.c
rm -f %{buildroot}%{_datadir}/mp3blaster/charmap/maketbl.c

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS CREDITS ChangeLog FAQ INSTALL NEWS README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*
