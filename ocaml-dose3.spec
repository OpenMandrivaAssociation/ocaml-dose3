%define	oname	dose3
%define ocaml_libdir %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)


Summary:	Framework for managing distribution packages and their dependencies
Name:		ocaml-%{oname}
Version:	2.9.2
%define	svnrev	2457
Release:	0.%{svnrev}.1
URL:		http://gforge.inria.fr/projects/sodiac/
License:	GPLv3+
Group:		Development/Other
Source0:	%{oname}-%{version}.tar.xz
# TODO: room for improval.. :|
Patch0:		dose3-2.9.2-rpm5.patch
%rename		edos-dose
%rename		edos-dose2

Requires:	ocaml-pcre
Requires:	ocaml-calendar
Requires:	ocaml-camlzip
Requires:	ocaml-camlbz2

BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-pcre-devel
BuildRequires:	ocaml-calendar-devel
BuildRequires:	ocaml-camlzip-devel
BuildRequires:	ocaml-camlbz2-devel
BuildRequires:	ocaml-ocamlgraph-devel
BuildRequires:	cudf-ocaml-devel
BuildRequires:	librpm-devel
BuildRequires:	libpopt-devel

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
Requires:	ocaml-dose2

%description	devel
Contains all libraries neededs to compile application using the dose3 framework

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1 -b .rpm5~
rm -f configure
autoreconf -f -Im4

%build
%configure	--with-rpm
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{ocaml_libdir}
%makeinstall DESTDIR=%{buildroot}%{ocaml_libdir}

%files
%doc README
%dir %{ocaml_libdir}/%{oname}
%{ocaml_libdir}/%{oname}/META
%{ocaml_libdir}/%{oname}/ascii_io.cmi
%{ocaml_libdir}/%{oname}/binary_io.cmi
%{ocaml_libdir}/%{oname}/conduit.cma
%{ocaml_libdir}/%{oname}/conduit.cmi
%{ocaml_libdir}/%{oname}/diagnosis.cmi
%{ocaml_libdir}/%{oname}/dosebase.cma
%{ocaml_libdir}/%{oname}/dosebase.cmi
%{ocaml_libdir}/%{oname}/fragments.cmi
%{ocaml_libdir}/%{oname}/generic_io.cmi
%{ocaml_libdir}/%{oname}/human_io.cmi
%{ocaml_libdir}/%{oname}/installability.cmi
%{ocaml_libdir}/%{oname}/io.cma
%{ocaml_libdir}/%{oname}/io.cmi
%{ocaml_libdir}/%{oname}/lexer.cmi
%{ocaml_libdir}/%{oname}/lifetime.cma
%{ocaml_libdir}/%{oname}/lifetime.cmi
%{ocaml_libdir}/%{oname}/napkin.cma
%{ocaml_libdir}/%{oname}/napkin.cmi
%{ocaml_libdir}/%{oname}/ocamldeb.cma
%{ocaml_libdir}/%{oname}/ocamldeb.cmi
%{ocaml_libdir}/%{oname}/ocamldebwriter.cmi
%{ocaml_libdir}/%{oname}/ocamlpkgsrc.cma
%{ocaml_libdir}/%{oname}/ocamlpkgsrc.cmi
%{ocaml_libdir}/%{oname}/ocamlrpm.cma
%{ocaml_libdir}/%{oname}/ocamlrpm.cmi
%{ocaml_libdir}/%{oname}/packetology.cma
%{ocaml_libdir}/%{oname}/pirate.cmi
%{ocaml_libdir}/%{oname}/progress.cma
%{ocaml_libdir}/%{oname}/progress.cmi
%{ocaml_libdir}/%{oname}/rapids.cma
%{ocaml_libdir}/%{oname}/rapids.cmi
%{ocaml_libdir}/%{oname}/satsolver.cma
%{ocaml_libdir}/%{oname}/solver.cmi
%{ocaml_libdir}/%{oname}/util.cma
%{ocaml_libdir}/%{oname}/util.cmi
%{ocaml_libdir}/%{oname}/waterway.cmi
%{ocaml_libdir}/stublibs/dllocamlpkgsrc.so
%{ocaml_libdir}/stublibs/dllocamlrpm.so*

%files  devel
%defattr(-,root,root)
%doc README
%{ocaml_libdir}/%{oname}/conduit.a
%{ocaml_libdir}/%{oname}/conduit.cmxa
%{ocaml_libdir}/%{oname}/dosebase.a
%{ocaml_libdir}/%{oname}/dosebase.cmxa
%{ocaml_libdir}/%{oname}/io.a
%{ocaml_libdir}/%{oname}/io.cmxa
%{ocaml_libdir}/%{oname}/lifetime.a
%{ocaml_libdir}/%{oname}/lifetime.cmxa
%{ocaml_libdir}/%{oname}/napkin.a
%{ocaml_libdir}/%{oname}/napkin.cmxa
%{ocaml_libdir}/%{oname}/ocamldeb.a
%{ocaml_libdir}/%{oname}/ocamldeb.cmxa
%{ocaml_libdir}/%{oname}/ocamlpkgsrc.a
%{ocaml_libdir}/%{oname}/ocamlpkgsrc.cmxa
%{ocaml_libdir}/%{oname}/ocamlrpm.a
%{ocaml_libdir}/%{oname}/ocamlrpm.cmxa
%{ocaml_libdir}/%{oname}/packetology.a
%{ocaml_libdir}/%{oname}/packetology.cmxa
%{ocaml_libdir}/%{oname}/progress.a
%{ocaml_libdir}/%{oname}/progress.cmxa
%{ocaml_libdir}/%{oname}/rapids.a
%{ocaml_libdir}/%{oname}/rapids.cmxa
%{ocaml_libdir}/%{oname}/satsolver.a
%{ocaml_libdir}/%{oname}/satsolver.cmxa
%{ocaml_libdir}/%{oname}/util.a
%{ocaml_libdir}/%{oname}/util.cmxa
#copied with spurious permissions, need a setting to standard permissions
%defattr(644,root,root)
%{ocaml_libdir}/%{oname}/libocamlpkgsrc.a
%{ocaml_libdir}/%{oname}/libocamlrpm.a
