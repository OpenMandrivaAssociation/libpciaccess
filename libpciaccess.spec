%define major		0
%define libname		%mklibname pciaccess %major
%define develname	%mklibname pciaccess -d

Name:		libpciaccess
Version:	0.13
Release:	1
Summary:	Generic PCI access library (from X.org)
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
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
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
A generic PCI access library from X.org. Development headers and
libraries.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--with-pciids-path=/usr/share

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/*.pc

