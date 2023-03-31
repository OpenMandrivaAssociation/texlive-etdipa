Name:		texlive-etdipa
Version:	36354
Release:	2
Summary:	Simple, lightweight template for scientific documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/etdipa
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etdipa.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/etdipa.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a complete working directory for the
scientific documentation of arbitrary projects. It was
originally developed to provide a template for Austrian
"Diplomarbeiten" or "Vorwissenschaftliche Arbeiten", which are
scientfic projects of students at a secondary school.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/latex/etdipa

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
