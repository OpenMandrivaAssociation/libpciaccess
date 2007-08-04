%define name	libpciaccess
%define version	0.8.0
%define git	20070804
%if %git
%define release	%mkrel 0.%git.2
%else
%define release	%mkrel 1
%endif

%define major		0
%define libname		%mklibname pciaccess %major
%define develname	%mklibname pciaccess -d

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Generic PCI access library (from X.org)
Group:		Development/X11
URL:		http://xorg.freedesktop.org
%if %git
# git clone git://anongit.freedesktop.org/git/xorg/lib/libpciaccess
Source0:	libpciaccess-%{git}.tar.bz2
%else
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
%endif
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	pciids

%description
A generic PCI access library from X.org.

%package -n %{libname}
Summary:	Generic PCI access library (from X.org)
Group:		Development/X11

%description -n %{libname}
A generic PCI access library from X.org.

%package -n %{develname}
Summary:	Development headers and libraries for %{name}
Group:		Development/X11
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
A generic PCI access library from X.org. Development headers and
libraries.

%prep
%if %git
%setup -q -n %{name}
%else
%setup -q -n %{name}-%{version}
%endif

%build
%if %git
./autogen.sh
%endif
%configure2_5x	--with-pciids-path=/usr/share
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/*.*a
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc

