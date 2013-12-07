%define major	0
%define libname	%mklibname pciaccess %major
%define devname	%mklibname pciaccess -d
%bcond_without	uclibc

Summary:	Generic PCI access library (from X.org)
Name:		libpciaccess
Version:	0.13.2
Release:	4
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:	pciids
%if %{with uclibc}
BuildRequires:	uClibc-devel >= 0.9.33.2-14
%endif

%description
A generic PCI access library from X.org.

%package -n	%{libname}
Summary:	Generic PCI access library (from X.org)
Group:		Development/X11

%description -n	%{libname}
A generic PCI access library from X.org.

%package -n	uclibc-%{libname}
Summary:	Generic PCI access library (from X.org) (uClibc build)
Group:		Development/X11

%description -n	uclibc-%{libname}
A generic PCI access library from X.org.

%package -n	%{devname}
Summary:	Development headers and libraries for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
%if %{with uclibc}
Requires:	uclibc-%{libname} = %{version}
%endif
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
A generic PCI access library from X.org. Development headers and
libraries.

%prep
%setup -q

%build
CONFIGURE_TOP="$PWD"
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
%uclibc_configure \
	--disable-static \
	--with-pciids-path=%{_datadir}
%make
popd
%endif

mkdir -p system
pushd system
%configure2_5x \
	--disable-static \
	--with-pciids-path=%{_datadir}
%make
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc
rm %{buildroot}%{uclibc_root}%{_libdir}/pkgconfig/pciaccess.pc
%endif

%makeinstall_std -C system

%files -n %{libname}
%{_libdir}/libpciaccess.so.%{major}*

%if %{with uclibc}
%files -n uclibc-%{libname}
%{uclibc_root}%{_libdir}/libpciaccess.so.%{major}*
%endif

%files -n %{devname}
%{_libdir}/libpciaccess.so
%if %{with uclibc}
%{uclibc_root}%{_libdir}/libpciaccess.so
%endif
%{_includedir}/pciaccess.h
%{_libdir}/pkgconfig/pciaccess.pc

