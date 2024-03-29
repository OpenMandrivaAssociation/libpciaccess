# libpciaccess is used by libdrm, libdrm is used by wine and steam
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major 0
%define libname %mklibname pciaccess %major
%define devname %mklibname pciaccess -d
%define lib32name libpciaccess%{major}
%define dev32name libpciaccess-devel

%global optflags %{optflags} -O3

Summary:	Generic PCI access library (from X.org)
Name:		libpciaccess
Version:	0.18
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:	hwdata >= 0.314
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(zlib)
%if %{with compat32}
BuildRequires:  devel(libz)
%endif

%description
A generic PCI access library from X.org.

%package -n %{libname}
Summary:	Generic PCI access library (from X.org)
Group:		Development/X11
Requires:	hwdata >= 0.314

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	Generic PCI access library (from X.org) (32-bit)
Group:		Development/X11
Requires:	hwdata >= 0.314
BuildRequires:	libc6

%description -n	%{lib32name}
A generic PCI access library from X.org.

%package -n %{dev32name}
Summary:	Development headers and libraries for %{name} (32-bit)
Group:		Development/X11
Requires:	%{devname} = %{version}
Requires:	%{lib32name} = %{version}

%description -n %{dev32name}
A generic PCI access library from X.org. Development headers and
libraries.
%endif

%prep
%autosetup -p1
%if %{with compat32}
%meson32 --debug \
%endif
%meson

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%meson_build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%meson_install

%files -n %{libname}
%{_libdir}/libpciaccess.so.%{major}*

%files -n %{devname}
%{_libdir}/libpciaccess.so
%{_includedir}/pciaccess.h
%{_libdir}/pkgconfig/pciaccess.pc

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libpciaccess.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libpciaccess.so
%{_prefix}/lib/pkgconfig/pciaccess.pc
%endif
