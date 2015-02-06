Summary: 	Console based MP3 player
Name: 		mp3blaster
Version: 	3.2.5
Release: 	8
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


%changelog
* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-7mdv2011.0
+ Revision: 645842
- relink against libmysqlclient.so.18

* Sat Jan 01 2011 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-6mdv2011.0
+ Revision: 627260
- rebuilt against mysql-5.5.8 libs, again

* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-5mdv2011.0
+ Revision: 626542
- rebuilt against mysql-5.5.8 libs

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-3mdv2011.0
+ Revision: 612941
- the mass rebuild of 2010.1 packages

* Thu Feb 18 2010 Oden Eriksson <oeriksson@mandriva.com> 3.2.5-2mdv2010.1
+ Revision: 507490
- rebuild

* Wed Jan 20 2010 Jérôme Brenier <incubusss@mandriva.org> 3.2.5-1mdv2010.1
+ Revision: 494384
- new version 3.2.5
- drop the no more necessary gcc43 patch
- sync patches with Debian

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-8mdv2009.1
+ Revision: 311308
- rebuilt against mysql-5.1.30 libs

* Sat Sep 20 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-7mdv2009.0
+ Revision: 286152
- added a gcc43 patch from gentoo

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Mar 07 2008 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-4mdv2008.1
+ Revision: 181387
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-3mdv2008.0
+ Revision: 83802
- rebuild


* Mon Sep 04 2006 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-1mdv2007.0
- rebuilt against MySQL-5.0.24a-1mdv2007.0 due to ABI changes

* Sun Aug 06 2006 Oden Eriksson <oeriksson@mandriva.com> 3.2.3-1mdv2007.0
- 3.2.3

* Tue Jan 31 2006 Oden Eriksson <oeriksson@mandriva.com> 3.2.2-1mdk
- 3.2.2 (Minor feature enhancements)

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 3.2.0-5mdk
- rebuilt against MySQL-5.0.15

* Mon Jan 24 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 3.2.0-4mdk
- rebuilt against MySQL-4.1.x system libs

* Sun Jun 06 2004 Austin Acton <austin@mandrake.org> 3.2.0-3mdk
- rebuild

* Mon Mar 01 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 3.2.0-2mdk
- Own dir

* Fri Nov 28 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 3.2.0-1mdk
- 3.2.0
- added lirc support
- fix explicit-lib-dependency
- fix invalid-build-requires
- fix devel-file-in-non-devel-package 
- misc spec file fixes

