%define major	0
%define libname	%mklibname pciaccess %major
%define devname	%mklibname pciaccess -d
%define	static	%mklibname pciaccess -d -s

%bcond_with	uclibc
Name:		libpciaccess
Version:	0.13.1
Release:	2
Summary:	Generic PCI access library (from X.org)
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:	pciids
%if %{with uclibc}
BuildRequires:	uClibc-devel
%endif

%description
A generic PCI access library from X.org.

%package -n	%{libname}
Summary:	Generic PCI access library (from X.org)
Group:		Development/X11

%description -n	%{libname}
A generic PCI access library from X.org.

%package -n	%{devname}
Summary:	Development headers and libraries for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
A generic PCI access library from X.org. Development headers and
libraries.

%package -n	%{static}
Summary:	Static development library for %{name}
Group:		Development/X11
Requires:	%{devname} = %{version}
Provides:	pciaccess-static-devel

%description -n	%{static}
A generic PCI access library from X.org. Static library for development.

%prep
%setup -q

%build
CONFIGURE_TOP="$PWD"
%if %{with uclibc}
mkdir -p uclibc
pushd uclibc
%configure2_5x	CC="%{uclibc_cc}" \
		CFLAGS="%{uclibc_cflags}" \
		--disable-shared \
		--enable-static \
		--with-pciids-path=/usr/share
%make
popd
%endif

mkdir -p system
pushd system
%configure2_5x	--enable-static \
		--with-pciids-path=/usr/share
%make
popd

%install
%if %{with uclibc}
%makeinstall_std -C uclibc
%endif

%makeinstall_std -C system

%files -n %{libname}
%{_libdir}/libpciaccess.so.%{major}*

%files -n %{devname}
%{_libdir}/libpciaccess.so
%{_includedir}/pciaccess.h
%{_libdir}/pkgconfig/pciaccess.pc

%files -n %{static}
%{_libdir}/libpciaccess.a
%if %{with uclibc}
%{uclibc_root}%{_libdir}/libpciaccess.a
%endif
