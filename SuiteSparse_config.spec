Summary:	SuiteSparse_config development files
Summary(pl.UTF-8):	Pliki programistyczne SuiteSparse_config
Name:		SuiteSparse_config
Version:	4.1.0
Release:	1
License:	no restrictions
Group:		Development
Source0:	http://www.cise.ufl.edu/research/sparse/UFconfig/%{name}-%{version}.tar.gz
# Source0-md5:	af1060a2bdd312571e065dab29cbbb70
Patch0:		%{name}-config.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/UFconfig/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SuiteSparse_config is required by nearly all sparse matrix packages
that are authored by Timothy A. Davis.

Before version 4, SuiteSparse_config used to be named UFconfig.

%description -l pl.UTF-8
SuiteSparse_config jest wymagany przez prawie wszystkie pakiety do
obliczeń na macierzach rzadkich autorstwa Timothy'ego A. Davisa.

SuiteSparse_concig przed wersją 4 nazywał się UFconfig.

%package libs
Summary:	SuiteSparse_config shared library
Summary(pl.UTF-8):	Biblioteka współdzielona SuiteSparse_config
Group:		Libraries

%description libs
SuiteSparse_config shared library, containing malloc/free wrappers.

%description libs -l pl.UTF-8
Biblioteka współdzielona SuiteSparse_config, zawierająca funkcje
obudowujące malloc/free.

%package devel
Summary:	Development files for SuiteSparse_config library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki SuiteSparse_config
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Development files for SuiteSparse_config library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki SuiteSparse_config.

%package static
Summary:	SuiteSparse_config static library
Summary(pl.UTF-8):	Biblioteka statyczna SuiteSparse_config
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
SuiteSparse_config static library.

%description static -l pl.UTF-8
Biblioteka statyczna SuiteSparse_config.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	INSTALL_LIB=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_datadir}/misc}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL_LIB=%{_libdir}

cp -a SuiteSparse_config.mk $RPM_BUILD_ROOT%{_datadir}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%{_includedir}/SuiteSparse_config.h
%{_datadir}/misc/SuiteSparse_config.mk

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsuitesparseconfig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsuitesparseconfig.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsuitesparseconfig.so
%{_libdir}/libsuitesparseconfig.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libsuitesparseconfig.a
