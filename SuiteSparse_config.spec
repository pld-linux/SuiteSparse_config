Summary:	UFconfig development files
Summary(pl.UTF-8):	Pliki programistyczne UFconfig
Name:		UFconfig
Version:	2.4.0
Release:	0.2
License:	LGPL
Group:		Development
Source0:	http://www.cise.ufl.edu/research/sparse/UFconfig/%{name}-%{version}.tar.gz
# Source0-md5:	3cfdd2c223b9b31444782310a8cb2c65
URL:		http://www.cise.ufl.edu/research/sparse/UFconfig/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UFconfig is required by nearly all sparse matrix packages that are
authored by Timothy A. Davis.

%description -l pl.UTF-8
UFconfig jest wymagany przez prawie wszystkie pakiety do obliczeń na
macierzach rzadkich autorstwa Timothy'ego A. Davisa.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_datadir}/misc}
cp -a UFconfig.h $RPM_BUILD_ROOT%{_includedir}
cp -a UFconfig.mk $RPM_BUILD_ROOT%{_datadir}/misc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%{_includedir}/UFconfig.h
%{_datadir}/misc/UFconfig.mk
