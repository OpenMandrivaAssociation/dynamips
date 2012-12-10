%define pre RC2
%define rel 2

Name:		dynamips
Version:	0.2.8
Release:	%mkrel %{?pre:0.%pre.}%rel
License:	GPL
Group:		Emulators
Summary:	MIPS64 emulator able to emulate the Cisco 7200 and 3600 platforms
URL:		http://www.ipflow.utc.fr/index.php/Cisco_7200_Simulator
Source:		http://www.ipflow.utc.fr/dynamips/dynamips-%{version}%{?pre:-%pre}.tar.gz
Patch:		dynamips-makefile-libs.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libpcap-devel elfutils-devel
ExclusiveArch:	%ix86 x86_64

%description
I started in August 2005 a project to emulate a Cisco 7200 on a traditionnal
PC. Now, it also supports Cisco 3600 series (3620, 3640 and 3660).

The goals of this emulator are mainly:

    * To be used as a training platform, with software used in real world. It
      would allow people to become more familiar with Cisco devices, Cisco
      being the world leader in networking technologies ;
    * Test and experiment the numerous and powerful features of Cisco IOS ;
    * Check quickly configurations to be deployed later on real routers.


Of course, this emulator cannot replace a real router: you should be able to
get a performance of about 1 kpps (depending on your host machine), to be
compared to the 100 kpps delivered by a NPE-100 (the oldest NPE model). So, it
is simply a complementary tool to real labs for administrators of Cisco
networks or people wanting to pass their CCNA/CCNP/CCIE exams. 


%prep
%setup -q %{?pre:-n %{name}-%{version}-%{pre}}
%patch -p1 -b .orig

%build
#%make
#parallel build fails
%ifarch x86_64
export DYNAMIPS_ARCH=amd64
%endif
make

%install
rm -Rf %{buildroot}

mkdir -p %{buildroot}/{%{_bindir},%{_mandir}/man1}
install -m755 dynamips nvram_export %{buildroot}/%{_bindir}
install -m644 dynamips.1 nvram_export.1 %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/var/lib/%{name}/{labs,images}

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%dir /var/lib/%{name}/images
%dir /var/lib/%{name}/labs
%doc README README.hypervisor TODO
%doc %{_mandir}/man1/*




%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.8-0.RC2.2mdv2011.0
+ Revision: 610330
- rebuild

* Sat Jan 31 2009 Buchan Milne <bgmilne@mandriva.org> 0.2.8-0.RC2.1mdv2010.1
+ Revision: 335777
- New version 0.2.8-rc2

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.7-2mdv2009.1
+ Revision: 298249
- rebuilt against libpcap-1.0.0

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.2.7-1mdv2008.1
+ Revision: 140723
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jun 04 2007 Buchan Milne <bgmilne@mandriva.org> 0.2.7-1mdv2008.0
+ Revision: 35016
- New version 0.2.7 final


* Sun Mar 11 2007 Buchan Milne <bgmilne@mandriva.org> 0.2.7-0.RC1.2mdv2007.1
+ Revision: 141251
- New version 0.2.7-RC1
- Add labs and images directories for use in hypervisor mode
- Fix build on x86_64

* Wed Jan 17 2007 Buchan Milne <bgmilne@mandriva.org> 0.2.6-0.RC5.1mdv2007.1
+ Revision: 109963
- Import dynamips

* Sat Jan 06 2007 Buchan Milne <bgmilne@mandriva.org> 0.2.5-1mdv
- initial package

