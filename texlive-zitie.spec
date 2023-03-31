Name:		texlive-zitie
Version:	60676
Release:	2
Summary:	Create CJK character calligraphy practicing sheets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zitie
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zitie.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zitie.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package for creating CJK character calligraphy
practicing sheets (copybooks). Currently, only XeTeX is
supported.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/zitie
%doc %{_texmfdistdir}/doc/xelatex/zitie

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
