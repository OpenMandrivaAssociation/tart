#OCcaml compiler generate both bytecode (normal name) and native executable (suffixed with .opt) ; this macro tests if the native compiler is installed, and if, uses it)
%define opt %(test -x %{_bindir}/ocamlopt && echo 1 || echo 0)

Summary:	Tart is a fast, greedy repository partitioner
Name:		tart
Version:	1.0.3
Release:	%mkrel 1
Source0:	%{name}-%{version}.tar.gz
License:	GPLv2
Group:		Development/Other
Url:		http://gforge.inria.fr/projects/sodiac
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Buildrequires:	ocaml-dose2-devel
Requires:	ocaml-dose2

%description
Tart is the program that takes care of thinning, i.e. spreading a
distribution over different (numbered) media (CDs, DVDs, etc) so
that every package on the distribution can be installed using only
the medium it is on and preceeding media. For example, all packages
on CD 1 can be installed using only the packages from CD 1, all
packages on CD 2 can be installed using only the packages from CDs
1 and 2, and so forth.

%prep
%setup -q

%build
%if %opt
make opt
%else
make byte
%endif

%install
rm -rf %{buildroot}
%if %opt
install -m755 tart.opt -D %{buildroot}%{_bindir}/tart
%else
install -m755 tart -D %{buildroot}%{_bindir}/tart
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/tart

