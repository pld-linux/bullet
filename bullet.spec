#
%define		patch	%{nil}

Summary:	Bullet - Collision Detection and Rigid Body Dynamics Library.
Summary(pl.UTF-8):	Bullet
Name:		bullet
Version:	2.74
Release:	0.99
License:	Zlib
Group:		Applications
Source0:	http://bullet.googlecode.com/files/%{name}-%{version}%{patch}.tgz
# Source0-md5:	a444e0a5cd528c91356490ed7f25e262
URL:		http://www.bulletphysics.com/Bullet/wordpress/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bullet is a Collision Detection and Rigid Body Dynamics Library.

%description -l pl.UTF-8

%package devel
Summary:	Header files for ... library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ...
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for ... library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ....

%package static
Summary:	Static ... library
Summary(pl.UTF-8):	Statyczna biblioteka ...
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ... library.

%description static -l pl.UTF-8
Statyczna biblioteka ....

%prep
%setup -q

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cat install-sh | tr -d '\r' > install-sh2
mv install-sh2 install-sh

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr (755,root,root) %{_libdir}/lib%{name}*.so.*.*

%files devel
%defattr(644,root,root)
%attr(755,root,root) %{_libdir}/lib%{name}*.so
%attr(755,root,root) %{_libdir}/lib%{name}*.so.*
%attr(644,root,root) %{_libdir}/lib%{name}*.la
%{_includedir}/%{name}/
%{_pkgconfigdir}/%{name}.pc

%files static
%{_libdir}/lib%{name}*.a
