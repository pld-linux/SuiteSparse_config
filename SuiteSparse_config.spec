Summary:	UFconfig development files
Summary(pl.UTF-8):	Pliki programistyczne UFconfig
Name:		UFconfig
Version:	3.7.0
Release:	1
License:	no restrictions
Group:		Development
Source0:	http://www.cise.ufl.edu/research/sparse/UFconfig/%{name}-%{version}.tar.gz
# Source0-md5:	ab8c355d683e8c5597a0824b32704c70
Patch0:		%{name}-config.patch
Patch1:		%{name}-shared.patch
URL:		http://www.cise.ufl.edu/research/sparse/UFconfig/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UFconfig is required by nearly all sparse matrix packages that are
authored by Timothy A. Davis.

%description -l pl.UTF-8
UFconfig jest wymagany przez prawie wszystkie pakiety do obliczeń na
macierzach rzadkich autorstwa Timothy'ego A. Davisa.

%package libs
Summary:	UFconfig shared library
Summary(pl.UTF-8):	Biblioteka współdzielona UFconfig
Group:		Libraries

%description libs
UFconfig shared library, containing malloc/free wrappers.

%description libs -l pl.UTF-8
Biblioteka współdzielona UFconfig, zawierająca funkcje obudowujące
malloc/free.

%package devel
Summary:	Development files for UFconfig library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki UFconfig
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Development files for UFconfig library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki UFconfig.

%package static
Summary:	UFconfig static library
Summary(pl.UTF-8):	Biblioteka statyczna UFconfig
Group:		Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
UFconfig static library.

%description static -l pl.UTF-8
Biblioteka statyczna UFconfig.

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

cp -a UFconfig.mk $RPM_BUILD_ROOT%{_datadir}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.txt
%{_includedir}/UFconfig.h
%{_datadir}/misc/UFconfig.mk

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libufconfig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libufconfig.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libufconfig.so
%{_libdir}/libufconfig.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libufconfig.a
