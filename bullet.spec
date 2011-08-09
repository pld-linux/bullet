#
# TODO: fix linking
#
Summary:	Bullet - vollision detection and rigid body dynamics library
Summary(pl.UTF-8):	Bullet - biblioteka wykrywania kolizji oraz dynamiki ciała sztywnego
Name:		bullet
Version:	2.78
Release:	1
License:	Zlib
Group:		Applications
Source0:	http://bullet.googlecode.com/files/%{name}-%{version}.zip
# Source0-md5:	99d4070864c9f73521481ba9cda25038
Patch0:		%{name}-link.patch
URL:		http://bulletphysics.org/wordpress/
BuildRequires:	OpenGL-glut-devel
BuildRequires:	cmake
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bullet is a collision detection and rigid nody dynamics library.

%description -l pl.UTF-8
Bullet to biblioteka wykrywania kolizji oraz dynamiki ciała sztywnego

%package devel
Summary:	Header files for bullet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki bullet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for bullet library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki bullet.

%prep
%setup -q
%undos src/BulletMultiThreaded/GpuSoftBodySolvers/OpenCL/NVidia/CMakeLists.txt
%undos src/BulletMultiThreaded/GpuSoftBodySolvers/OpenCL/MiniCL/CMakeLists.txt
%patch0 -p1

%build
mkdir build
cd build
%cmake \
	-DBUILD_DEMOS=OFF \
	-DBUILD_EXTRAS=ON \
	-DINCLUDE_INSTALL_DIR=%{_includedir}/%{name} \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libBulletCollision.so.*.*
%attr(755,root,root) %{_libdir}/libBulletDynamics.so.*.*
%attr(755,root,root) %{_libdir}/libBulletMultiThreaded.so.*.*
%attr(755,root,root) %{_libdir}/libBulletSoftBody.so.*.*
%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_CPU.so.*.*
%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_Mini.so.*.*
%attr(755,root,root) %{_libdir}/libLinearMath.so.*.*
%attr(755,root,root) %{_libdir}/libMiniCL.so.*.*

%files devel
%defattr(644,root,root,755)
%doc Bullet_User_Manual.pdf
%attr(755,root,root) %{_libdir}/libBulletCollision.so
%attr(755,root,root) %{_libdir}/libBulletDynamics.so
%attr(755,root,root) %{_libdir}/libBulletMultiThreaded.so
%attr(755,root,root) %{_libdir}/libBulletSoftBody.so
%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_CPU.so
%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_Mini.so
%attr(755,root,root) %{_libdir}/libLinearMath.so
%attr(755,root,root) %{_libdir}/libMiniCL.so
%{_includedir}/%{name}
%{_pkgconfigdir}/%{name}.pc
