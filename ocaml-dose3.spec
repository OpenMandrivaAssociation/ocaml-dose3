%define	oname	dose3
%define ocaml_libdir %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)


Summary:	Framework for managing distribution packages and their dependencies
Name:		ocaml-%{oname}
Version:	2.9.9
%define	svnrev	2753
Release:	0.%{svnrev}.3
URL:		https://gforge.inria.fr/projects/sodiac/
License:	GPLv3+
Group:		Development/Other
Source0:	%{oname}-%{svnrev}.tar.xz
# TODO: room for improval.. :|
Patch0:		dose3-2.9.2-rpm5.patch
Patch1:		dose3-2.9.2-backend.ml.patch
Patch2:		dose3-2.9.9-gold.patch
%rename		edos-dose
%rename		edos-dose3

Requires:	ocaml-pcre
Requires:	ocaml-calendar
Requires:	ocaml-camlzip
Requires:	ocaml-camlbz2

BuildRequires:	camlp4
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-extlib-devel
BuildRequires:	ocaml-calendar-devel
BuildRequires:	ocaml-camlzip-devel
BuildRequires:	ocaml-camlbz2-devel
BuildRequires:	ocaml-ocamlgraph-devel
BuildRequires:	ocaml-curl
BuildRequires:	ocaml-ounit
BuildRequires:	ocaml-expat-devel
BuildRequires:	ocaml-camlzip-devel
BuildRequires:	ocaml-camlbz2-devel
BuildRequires:	ocaml-sqlite-devel
#BuildRequires:	ocaml-postgresql-devel
BuildRequires:	ocaml-benchmark
BuildRequires:	ocaml-graphviz
BuildRequires:	ocaml-json-static ocaml-json-wheel-devel
BuildRequires:	ocaml-ocamlnet-devel
BuildRequires:	ocaml-xml-light-devel
BuildRequires:	cudf-ocaml-devel
BuildRequires:	rpm-devel
BuildRequires:	popt-devel
BuildRequires:	bc

%description
Dose 3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

Though not tied to any particular distribution, Dose 3 forms a background of
libraries which enable injecting packages coming for various distribution.
Companion libraries (e.g. ceve) and tools (e.g.  pkglab) rely on Dose 3 to
manage packages coming from various distributions, e.g. Debian and Red Hat.

Besides basic functionalities for querying and setting package properties, Dose
3 also implements algorithms for solving more complex problems (monitoring
package evolutions, correct and complete dependency resolution, repository-wide
uninstallability checks).

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	ocaml-dose3

%description	devel
Contains all libraries neededs to compile application using the dose3 framework

%prep
%setup -q -n %{oname}
#%if %mdkversion > 201010
#%patch0 -p1 -b .rpm5~
#%endif

#%patch1 -p0
%patch2 -p0
rm -f configure
autoreconf -f -Im4

%build
%configure	--with-rpm5 \
	#	--with-xml \
	#	--with-curl \
	#	--with-zip \
	#	--with-oUnit \
	#	--with-bz2 \
		#--with-sqlite \
	#	--with-benchmark \
		#--with-ocamlgraph \
		#--with-experimental \
		#--with-postgresql \

make

%install
%makeinstall_std LIBDIR=%{buildroot}%{_libdir}/ocaml BINDIR=%{buildroot}%{_bindir}
cd doc/manpages
for man in *.?; do
	install -m644 $man -D %{buildroot}%{_mandir}/man1/$man
done
rm %{buildroot}%{ocaml_libdir}/%{oname}/boilerplate*

%files
%defattr(-,root,root,-)
%{_bindir}/apt-cudf
%{_bindir}/ceve
%{_bindir}/deb-buildcheck
%{_bindir}/distcheck
%{_mandir}/man1/ceve.1*
%{_mandir}/man1/buildcheck.1*
%{_mandir}/man1/distcheck.1*
%dir %{ocaml_libdir}/%{oname}
%{ocaml_libdir}/%{oname}/META
%{ocaml_libdir}/%{oname}/*.cmi
%{ocaml_libdir}/%{oname}/*.cma

%files  devel
%doc README.architecture TODO
%dir %{ocaml_libdir}/%{oname}/algo
%{ocaml_libdir}/%{oname}/algo/*mli
%dir %{ocaml_libdir}/%{oname}/common
%{ocaml_libdir}/%{oname}/common/*.mli
%dir %{ocaml_libdir}/%{oname}/deb/
%{ocaml_libdir}/%{oname}/deb/*mli

%{ocaml_libdir}/%{oname}/*.cmo
%{ocaml_libdir}/%{oname}/*.a
%{ocaml_libdir}/%{oname}/*.cmxs
%{ocaml_libdir}/%{oname}/*.cmxa
#%{ocaml_libdir}/%{oname}/*.mli
%{ocaml_libdir}/%{oname}/*.o
%{_mandir}/man1/apt-cudf.1*
