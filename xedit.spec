%define		enable_xprint	0
Name:		xedit
Version:	1.0.3
Release:	%mkrel 1
Summary:	Simple text editor for X
Group:		Development/X11
URL: http://xorg.freedesktop.org
# Note tag xedit-1.0.3@mandriva suggested upstream
# Tag at commit 946b5b745d9d326799a23f7210b799e1b690643d
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/xedit xorg/app/xedit
# cd xorg/app/xedit
# git-archive --format=tar --prefix=xedit-1.0.3/ xedit-1_0_2 | bzip2 -9 > xedit-1.0.3.tar.bz2
########################################################################
Source:		%{name}-%{version}.tar.bz2
License:	GPLv2+ and MIT
########################################################################
# git-format-patch xedit-1.0.3@mandriva..origin/mandriva+gpl
Patch1: 0001-Make-mandriva-1.0.3-release.-This-includes-a-signi.patch
Patch2: 0002-Add-perl-and-autotools-edit-modes.-Perl-mode-has.patch
########################################################################
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

%description
Xedit provides a simple text editor for X.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1
%patch2 -p1

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
