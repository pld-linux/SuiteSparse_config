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
%patch0 -p1

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
