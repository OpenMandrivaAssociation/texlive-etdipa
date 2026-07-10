%global tl_name etdipa
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6
Release:	%{tl_revision}.1
Summary:	Simple, lightweight template for scientific documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/etdipa
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etdipa.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/etdipa.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a complete working directory for the scientific
documentation of arbitrary projects. It was originally developed to
provide a template for Austrian "Diplomarbeiten" or
"Vorwissenschaftliche Arbeiten", which are scientific projects of
students at a secondary school.

