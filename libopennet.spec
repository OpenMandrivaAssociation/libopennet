%define	major 0
%define libname	%mklibname opennet %{major}

Summary:	Libopennet allows you to open_net() files the same way you open() them now
Name:		libopennet
Version:	0.9.9
Release:	%mkrel 1
Group:		System/Libraries
License:	LGPL
URL:		http://www.rkeene.org/oss/libopennet/
Source0:	http://www.rkeene.org/files/oss/libopennet/%{name}-%{version}.tar.bz2
Patch0:		libopennet-0.9.3-DESTDIR.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Libopennet allows you to open_net()  urls (or files, for that matter) the same
way you would normally open() just files.

%package -n	%{libname}
Summary:	Libopennet allows you to open_net() files the same way you open() them now
Group:          System/Libraries

%description -n	%{libname}
Libopennet allows you to open_net()  urls (or files, for that matter) the same
way you would normally open() just files.

%package -n	%{libname}-devel
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}

%description -n	%{libname}-devel
Libopennet allows you to open_net()  urls (or files, for that matter) the same
way you would normally open() just files.

This package contains the static %{name} library and its header
files.

%prep

%setup -q -n %{name}-%{version}
%patch0 -p0

%build

%configure2_5x

# fix soname
perl -pi -e "s|^SHOBJFLAGS.*|SHOBJFLAGS=-Wl,-soname=%{name}.so.%{major} -shared -rdynamic -fPIC -D_REENTRANT|g" Makefile

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_mandir}/man3/*
