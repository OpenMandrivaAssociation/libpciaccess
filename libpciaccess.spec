%define major 0
%define libname %mklibname pciaccess %major
%define devname %mklibname pciaccess -d

Summary:	Generic PCI access library (from X.org)
Name:		libpciaccess
Version:	0.13.4
Release:	7
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Patch0:		0000-Include-config.h-before-anything-else-in-.c.patch
Patch1:		0001-Fix-quoting-issue.patch
Patch2:		0002-linux_sysfs.c-Include-limits.h-for-PATH_MAX.patch
Patch3:		0005-linux_sysfs-include-limits.h-for-PATH_MAX.patch
Patch4:		0006-libpciaccess-Fix-incorrect-format-specification.patch
Patch5:		0007-vgaarb-add-a-the-trailing-NULL-character-on-read-vga.patch
Patch6:		0008-device-name-handle-calloc-failure-in-insert.patch
Patch7:		0009-Ignore-32-bit-domains.patch
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

%makeinstall_std -C system

%files -n %{libname}
%{_libdir}/libpciaccess.so.%{major}*

%files -n %{devname}
%{_libdir}/libpciaccess.so
%{_includedir}/pciaccess.h
%{_libdir}/pkgconfig/pciaccess.pc
