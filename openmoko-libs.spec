#
Summary:	Platform libraries for OpenMoko
Name:		openmoko-libs
Version:	0.0.0.2352
Release:	0.1
License:	LGPL v2.1
Group:		Development/Libraries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	9a7e554d3d8e2a9ad33a991744b8285e
URL:		http://openmoko.org
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xosd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%package devel
Summary:	Header files for openmoko-libs library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki openmoko-libs
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for openmoko-libs library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki openmoko-libs.

%package static
Summary:	Static openmoko-libs library
Summary(pl.UTF-8):	Statyczna biblioteka openmoko-libs
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static openmoko-libs library.

%description static -l pl.UTF-8
Statyczna biblioteka openmoko-libs.

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
%attr(755,root,root)    %{_libdir}/libmokogsmd.so.0.0.0
%attr(755,root,root)    %{_libdir}/libmokojournal.so.0.0.0
%attr(755,root,root)    %{_libdir}/libmokoui.so.0.0.2

%files devel
%defattr(644,root,root,755)
%{_includedir}/openmoko-libs
%{_libdir}/*.la
%{_libdir}/*.so
%{_pkgconfigdir}/openmoko-libs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmokogsmd.a
%{_libdir}/libmokojournal.a
%{_libdir}/libmokoui.a
