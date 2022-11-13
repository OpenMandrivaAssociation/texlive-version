Name:		texlive-version
Version:	21920
Release:	1
Summary:	Conditionally include text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/version
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/version.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/version.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines macros \includeversion{NAME} and \excludeversion{NAME},
each of which defines an environment NAME whose text is to be
included or excluded from compilation. Although the command
syntax is very similar to that of comment, comment.sty is to be
preferred to version.sty for documents where significant chunks
of text may be excluded.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/version/version.sty
%doc %{_texmfdistdir}/doc/latex/version/version-doc.pdf
%doc %{_texmfdistdir}/doc/latex/version/version-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
