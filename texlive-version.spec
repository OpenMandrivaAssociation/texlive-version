%global tl_name version
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Conditionally include text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/version
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/version.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/version.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Defines macros \includeversion{NAME} and \excludeversion{NAME}, each of
which defines an environment NAME whose text is to be included or
excluded from compilation. Although the command syntax is very similar
to that of comment, comment.sty is to be preferred to version.sty for
documents where significant chunks of text may be excluded.

