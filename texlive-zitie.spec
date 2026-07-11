%global tl_name zitie
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.4.0
Release:	%{tl_revision}.1
Summary:	Create CJK character calligraphy practicing sheets
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/zitie
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zitie.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zitie.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX package for creating CJK character calligraphy
practicing sheets (copybooks). Currently, only XeTeX is supported.

