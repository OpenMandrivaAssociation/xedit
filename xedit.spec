%define		enable_xprint	0
Name:		xedit
Version:	1.0.2
Release:	%mkrel 18
Summary:	Simple text editor for X
Group:		Development/X11
#		git clone git://anongit.freedesktop.org/git/xorg/app/xedit xedit
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		xedit-git.patch
License:	GPLv2+ and MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
%if %{enable_xprint}
BuildRequires:	libxprintutil-devel >= 1.0.1
%endif
BuildRequires:	x11-util-macros >= 1.0.1

Requires:	x11-data-bitmaps
Requires:	aspell aspell-en grep
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
%patch0 -p1 -b .git

%build
autoreconf -ifs
%configure2_5x\
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

