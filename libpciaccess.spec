%define major 0
%define libname %mklibname pciaccess %major
%define devname %mklibname pciaccess -d

Summary:	Generic PCI access library (from X.org)
Name:		libpciaccess
Version:	0.13.5
Release:	7
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:	pciids
BuildRequires:	pkgconfig(xorg-macros)

%description
A generic PCI access library from X.org.

%package -n %{libname}
Summary:	Generic PCI access library (from X.org)
Group:		Development/X11

%description -n	%{libname}
A generic PCI access library from X.org.

%package -n %{devname}
Summary:	Development headers and libraries for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
A generic PCI access library from X.org. Development headers and
libraries.

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-static \
	--with-pciids-path=%{_datadir}
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libpciaccess.so.%{major}*

%files -n %{devname}
%{_libdir}/libpciaccess.so
%{_includedir}/pciaccess.h
%{_libdir}/pkgconfig/pciaccess.pc
