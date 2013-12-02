#
# Conditional build:
%bcond_with	opencl_amd	# AMD OpenCL
%bcond_with	opencl_intel	# Intel OpenCL (64-bit)
%bcond_with	opencl_nvidia	# NVidia OpenCL
#
Summary:	Bullet - collision detection and rigid body dynamics library
Summary(pl.UTF-8):	Bullet - biblioteka wykrywania kolizji oraz dynamiki ciała sztywnego
Name:		bullet
Version:	2.82
Release:	1
License:	Zlib (BSD-like)
Group:		Libraries
#Source0Download: https://code.google.com/p/bullet/downloads/list
Source0:	http://bullet.googlecode.com/files/%{name}-%{version}-r2704.tgz
# Source0-md5:	70b3c8d202dee91a0854b4cbc88173e8
Patch0:		%{name}-link.patch
URL:		http://bulletphysics.org/wordpress/
BuildRequires:	OpenCL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-glut-devel
BuildRequires:	cmake >= 2.4.3
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bullet is a collision detection and rigid nody dynamics library.

%description -l pl.UTF-8
Bullet to biblioteka wykrywania kolizji oraz dynamiki ciała sztywnego.

%package devel
Summary:	Header files for bullet libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek bullet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenCL-devel
Requires:	OpenGL-GLU-devel
Requires:	OpenGL-glut-devel

%description devel
Header files for bullet libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek bullet.

%prep
%setup -q -n %{name}-%{version}-r2704
%patch0 -p1

%build
install -d pkgbuild
cd pkgbuild
%cmake .. \
	%{!?with_opencl_amd:-DAMD_OPENCL_BASE_DIR:BOOL=OFF} \
	%{!?with_opencl_intel:-DINTEL_OPENCL_BASE_DIR:BOOL=OFF} \
	%{!?with_opencl_nvidia:-DNVIDIA_OPENCL_BASE_DIR:BOOL=OFF} \
	-DBUILD_DEMOS=OFF \
	-DBUILD_EXTRAS=ON \
	-DBUILD_MULTITHREADING=ON \
	-DINCLUDE_INSTALL_DIR=%{_includedir}/%{name} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C pkgbuild install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libBulletCollision.so.*.*
%attr(755,root,root) %{_libdir}/libBulletDynamics.so.*.*
%attr(755,root,root) %{_libdir}/libBulletMultiThreaded.so.*.*
%attr(755,root,root) %{_libdir}/libBulletSoftBody.so.*.*
%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_Mini.so.*.*
%{?with_opencl_amd:%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_AMD.so.*.*}
%{?with_opencl_intel:%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_Intel.so.*.*}
%{?with_opencl_nvidia:%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_NVidia.so.*.*}
%attr(755,root,root) %{_libdir}/libLinearMath.so.*.*
%attr(755,root,root) %{_libdir}/libMiniCL.so.*.*

%files devel
%defattr(644,root,root,755)
%doc Bullet_User_Manual.pdf
%attr(755,root,root) %{_libdir}/libBulletCollision.so
%attr(755,root,root) %{_libdir}/libBulletDynamics.so
%attr(755,root,root) %{_libdir}/libBulletMultiThreaded.so
%attr(755,root,root) %{_libdir}/libBulletSoftBody.so
%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_Mini.so
%{?with_opencl_amd:%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_AMD.so}
%{?with_opencl_intel:%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_Intel.so}
%{?with_opencl_nvidia:%attr(755,root,root) %{_libdir}/libBulletSoftBodySolvers_OpenCL_NVidia.so}
%attr(755,root,root) %{_libdir}/libLinearMath.so
%attr(755,root,root) %{_libdir}/libMiniCL.so
%{_includedir}/bullet
%{_libdir}/cmake/bullet
%{_pkgconfigdir}/bullet.pc
