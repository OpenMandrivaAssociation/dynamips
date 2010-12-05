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


