Summary:	Platform libraries for OpenMoko
Summary(pl.UTF-8):	Biblioteki platformy OpenMoko
Name:		openmoko-libs
Version:	0.0.0.2352
Release:	0.1
License:	LGPL v2.1
Group:		Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	9a7e554d3d8e2a9ad33a991744b8285e
URL:		http://openmoko.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	evolution-data-server-devel >= 1.4.2
BuildRequires:	gtk+2-devel >= 2:2.6
BuildRequires:	libgsmd-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Platform libraries for OpenMoko.

%description -l pl.UTF-8
Biblioteki platformy OpenMoko.

%package devel
Summary:	Header files for OpenMoko libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek OpenMoko
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	evolution-data-server-devel >= 1.4.2
Requires:	gtk+2-devel >= 2:2.6
Requires:	libgsmd-devel
Requires:	xosd-devel

%description devel
Header files for OpenMoko libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek OpenMoko.

%package static
Summary:	Static OpenMoko libraries
Summary(pl.UTF-8):	Statyczne biblioteki OpenMoko
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenMoko libraries.

%description static -l pl.UTF-8
Statyczne biblioteki OpenMoko.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
cp /usr/share/automake/mkinstalldirs .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libmokogsmd.so.*.*.*
%attr(755,root,root) %{_libdir}/libmokojournal.so.*.*.*
%attr(755,root,root) %{_libdir}/libmokoui.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmokogsmd.so
%attr(755,root,root) %{_libdir}/libmokojournal.so
%attr(755,root,root) %{_libdir}/libmokoui.so
%{_libdir}/libmokogsmd.la
%{_libdir}/libmokojournal.la
%{_libdir}/libmokoui.la
%{_includedir}/openmoko-libs
%{_pkgconfigdir}/openmoko-libs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmokogsmd.a
%{_libdir}/libmokojournal.a
%{_libdir}/libmokoui.a
