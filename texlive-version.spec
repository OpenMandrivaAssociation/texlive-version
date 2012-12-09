# revision 21920
# category Package
# catalog-ctan /macros/latex/contrib/version
# catalog-date 2011-04-02 15:43:25 +0200
# catalog-license other-free
# catalog-version 2.0
Name:		texlive-version
Version:	2.0
Release:	2
Summary:	Conditionally include text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/version
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/version.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/version.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 757419
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 719886
- texlive-version
- texlive-version
- texlive-version

