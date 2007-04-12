Name: xedit
Version: 1.0.2
Release: %mkrel 3
Summary: Simple text editor for X
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: libxprintutil-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
Xedit provides a simple text editor for X.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xedit
%{_libdir}/X11/xedit/lisp/lisp.lsp
%{_libdir}/X11/xedit/lisp/syntax.lsp
%{_libdir}/X11/xedit/lisp/indent.lsp
%{_libdir}/X11/xedit/lisp/progmodes/lisp.lsp
%{_libdir}/X11/xedit/lisp/progmodes/c.lsp
%{_libdir}/X11/xedit/lisp/progmodes/patch.lsp
%{_libdir}/X11/xedit/lisp/progmodes/html.lsp
%{_libdir}/X11/xedit/lisp/progmodes/rpm.lsp
%{_libdir}/X11/xedit/lisp/progmodes/man.lsp
%{_libdir}/X11/xedit/lisp/progmodes/xconf.lsp
%{_libdir}/X11/xedit/lisp/progmodes/make.lsp
%{_libdir}/X11/xedit/lisp/progmodes/xrdb.lsp
%{_libdir}/X11/xedit/lisp/progmodes/imake.lsp
%{_libdir}/X11/xedit/lisp/progmodes/sh.lsp
%{_libdir}/X11/xedit/lisp/progmodes/xlog.lsp
%{_libdir}/X11/xedit/lisp/progmodes/sgml.lsp
%{_libdir}/X11/xedit/lisp/xedit.lsp
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_mandir}/man1/xedit.1x.bz2


