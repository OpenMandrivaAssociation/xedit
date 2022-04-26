Name:		xedit
Version:	1.2.3
Release:	1
Summary:	Simple text editor for X
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xorg-macros) >= 1.1.5
BuildRequires:	xaw-devel >= 1.0.4
Requires:	x11-data-bitmaps
Requires:	aspell
Requires:	aspell-en
Requires:	grep
Requires:	words
Requires:	ctags
Requires:	x11-font-alias
# sgml mode
Requires:	x11-font-dec-misc
Requires:	x11-font-misc-misc
# courier (most modes) helvetica (sgml/html edit modes)
Requires:	x11-font-adobe-75dpi
Requires:	x11-font-adobe-100dpi
# lucidatypewriter (most modes)
Requires:	x11-font-bh-lucidatypewriter-75dpi
Requires:	x11-font-bh-lucidatypewriter-100dpi
# lucida (hmtl mode)
Requires:	x11-font-bh-75dpi
Requires:	x11-font-bh-100dpi

%description
Xedit provides a simple text editor for X.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xedit
%{_libdir}/X11/xedit
%{_datadir}/X11/app-defaults/Xedit*
%doc %{_mandir}/man1/xedit.1*
