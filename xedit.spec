Name:		xedit
Version:	1.0.2
Release:	%mkrel 4
Summary:	Simple text editor for X
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
BuildRequires:	libxprintutil-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

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
%{_libdir}/X11/xedit
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_mandir}/man1/xedit.1x*

