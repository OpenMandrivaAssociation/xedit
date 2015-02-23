Name:		xedit
Version:	1.2.2
Release:	1
Summary:	Simple text editor for X
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRequires:	pkgconfig(xorg-macros) >= 1.1.5
BuildRequires:	xaw-devel >= 1.0.4
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
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/xedit
%{_libdir}/X11/xedit
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_mandir}/man1/xedit.1*
