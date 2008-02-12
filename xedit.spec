%define		enable_xprint	0
%define		upstream	1.0.2
Name:		xedit
Version:	1.0.3
Release:	%mkrel 2
Summary:	Simple text editor for X
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{upstream}.tar.bz2
License:	GPLv2+ and MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libxaw-devel		>= 1.0.4
%if %{enable_xprint}
BuildRequires:	libxprintutil-devel	>= 1.0.1
%endif
Requires:	x11-data-bitmaps
Requires:	aspell aspell-en grep words
Requires:	ctags
Requires:	x11-font-alias
# sgml mode
Requires:	x11-font-dec-misc
Requires:	x11-font-misc-misc
# courier (most modes) helvetica (sgml/html edit modes)
Requires:	x11-font-adobe-75dpi x11-font-adobe-100dpi
# lucidatypewriter (most modes)
Requires:	x11-font-bh-lucidatypewriter-75dpi x11-font-bh-lucidatypewriter-100dpi
# lucida (hmtl mode)
Requires:	x11-font-bh-75dpi x11-font-bh-100dpi

Patch1:  0001-Add-updated-meaningful-README-COPYING-and-AUTHORS-f.patch
Patch2:  0002-Update-build-for-sane-defaults.patch
Patch3:  0003-Add-a-generic-hash-table-interface-to-replace-the-ot.patch
Patch4:  0004-Readd-support-for-international-resource-and-defaul.patch
Patch5:  0005-Make-ispell-interface-work-correctly-again.patch
Patch6:  0006-Fix-several-generic-bugs-including.patch
Patch7:  0007-Fix-several-problems-in-the-line-edit-mode.-Also-all.patch
Patch8:  0008-Generic-lisp-interface-bug-fixes-including.patch
Patch9:  0009-Add-support-to-enter-line-number-in-command-line.patch
Patch10: 0010-Fix-a-bug-in-the-regex-library-involving-alternate-p.patch
Patch11: 0011-Update-syntax-highlight-table-and-some-minor-tweaks.patch
Patch12: 0012-Add-a-tags-interface-to-xedit.patch
Patch13: 0013-Add-support-for-scrolling-textwindow-with-mouse-whee.patch
Patch14: 0014-GPL-licensed-perl-and-auto-tools-modes.patch
Patch15: 0015-Bump-reversion-to-1.0.3.patch

%description
Xedit provides a simple text editor for X.

%prep
%setup -q -n %{name}-%{upstream}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1

%build
autoreconf -ifs
%configure\
%if %{enable_xprint}
	--enable-xprint\
%else
	--disable-xprint\
%endif
	--x-includes=%{_includedir}\
	--x-libraries=%{_libdir}

# make sure the proper resources file will be installed
rm -f Xedit Xedit.ad

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xedit
%{_libdir}/X11/xedit
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_mandir}/man1/xedit.1*
