Name:		xedit
Version:	1.2.1
Release:	6
Summary:	Simple text editor for X
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libxaw-devel		>= 1.0.4
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

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xedit
%{_libdir}/X11/xedit
%{_datadir}/X11/app-defaults/Xedit
%{_datadir}/X11/app-defaults/Xedit-color
%{_mandir}/man1/xedit.1*


%changelog
* Tue May 22 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2012.0
+ Revision: 800163
- Update to latest upstream release.

* Thu Dec 29 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1.2-6
+ Revision: 746207
- Correct read of uninitialized memory when creating a new file.

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-5
+ Revision: 671303
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-4mdv2011.0
+ Revision: 608202
- rebuild

* Sat May 08 2010 Paulo Andrade <pcpa@mandriva.com.br> 1.1.2-3mdv2010.1
+ Revision: 543541
- Correct 64 bit issues in lisp bignum code

* Fri Nov 27 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.1.2-2mdv2010.1
+ Revision: 470687
- Don't quote strings inside macro expansion blocks protected by '[' and ']'.

* Wed May 20 2009 Funda Wang <fwang@mandriva.org> 1.1.2-1mdv2010.0
+ Revision: 377914
- fix str fmt

* Wed Nov 12 2008 Thierry Vignaud <tv@mandriva.org> 1.1.2-1mdv2009.1
+ Revision: 302455
- new version

* Tue Aug 05 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.1-1mdv2009.0
+ Revision: 264105
- Update to upstream release 1.1.1.

* Mon May 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-6mdv2009.0
+ Revision: 206408
- Warn if a newer version of a file exists before overwritting it.
  Fix an off by one error check that can lead to an infinite loop on
  regex search&replace.

* Wed Apr 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-5mdv2009.0
+ Revision: 194829
- Add python mode and some compile warning fixes.
  License reverted to only MIT as freedesktop asked for it to
  accept the patches.

* Thu Mar 13 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-4mdv2008.1
+ Revision: 187574
- Update to latest version of patches. Some patches were reordered to
  apply the version bump last.
  This version has the auto and perl edit mode files license changed
  from GPL to BSD, as requested by Xorg.
  Also added support for multiple make jobs.

* Fri Feb 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-3mdv2008.1
+ Revision: 173972
- Remake git-branch with xedit patches due to removing
  #ifdef INCLUDE_XPRINT_SUPPORT around call to XtSetLanguageProc when spliting
  patches in different commits. XtSetLanguageProc can take several seconds to
  finish when some fonts are not installed, and is the default on Mandriva.

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-2mdv2008.1
+ Revision: 166319
- Revert to use upstream tarball instead of using git-archive.
  Add one patch per change since upstream version.
  Only change since last package is proper check if tag file is in cwd.

* Mon Jan 21 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.3-1mdv2008.1
+ Revision: 155905
- Bump to version 1.0.3, and add changes to git.mandriva.com, but only as
  two batch of changes, one including GPL code and another not.
  Changes include:
 o Single/simple hash table implementation for almost all code.
 o Fix ispell interface.
 o Fix several bugs and crashes.
 o Add a tags interface.
 o Fix a bug in the regex library that could cause empty matches be
   Returned when testing alternative matches, but no match actually
   was found.
 o Update documentation.
 o Add perl and "autotools" edit modes. Perl mode has auto indentation.
- Rewrite code that parses replace string in regex search&replace as
  it was buggy and not properly handling the escape sequence \\.
- Add a simple syntax highlight mode for autoconf/automake/m4 files.
  Use same syntax as vi for +<number> in command line, i.e. "xedit file.c +32"
  will load file.c and go to line 32.
  Fix license in spec file.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Dec 12 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-17mdv2008.1
+ Revision: 117860
- Change license to GPL/MIT to cover perl mode code.
  Build, but not install the standalone lisp interpreter and the regex test
  program, and also remove the test program from libre.a.
  Some cleanup and bug fixes to perl mode, including adding some macros to
  make it easier to add new patterns, assing the hash value :cont-indent to
  *cont-indent*, and not :indentation, and some missing keywords are highlited
  now. Also added an initial support for "here docs".
  This patch also adds a fix for the regex library (lisp/re/re.c), as one of
  the patterns in the perl-mode showed a problem where it was returning a 0
  length match when it  really wasn't matching anything. Also added a regression
  test to lisp/test/regex.lsp and lisp/re/tests.txt. To run the "regression
  tests", either type (load "path/to/regression-test.lsp")C-J in the scratch
  buffer, or run the standalone lisp interpreter to test it.

* Mon Dec 10 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-16mdv2008.1
+ Revision: 116976
- Remove lsp.c from liblisp.a. It contains a main function, and is the
  main file of a standalone lisp interpreter that should be linked with
  liblisp.a, not required by the text editor.
  Added a perl syntax highlight and indentation rules progmode.
  Fixed a problem wen attempting to save a file in "line edit" mode,
  where it would attempt to save the file using the regex pattern as file
  name, but usually fail.
  Fixed a bug that was reinstantied in a previous fix, where it would
  not properly parse all escaped characters of a replace string, in line
  edit mode.
  Fixed a warning about an unusued lisp variable in the indentation
  macro. Currently only the C mode uses that variable.
  Changed the C mode to understand C++ comments in preprocessor lines,
  and also properly parse strings and character constants, otherwise it
  would not properly parse // inside strings.
  NOTE that the perl mode is the first GNU/GPL licensed file in xedit,
  but I may change the license of other files to GPL also (since I am the
  author of 95%% or more of the xedit code).
  Fixed a bug that would not allow "unreadable" atoms as keywords,
  mainly for consistency, bug found when trying to create a keyword
  containing the ')' character in it's name.
  Changed the default *auto-modes* to treat .cpp and .hpp as C/C++
  sources, to treat xorg.conf as a XF86Config mode, and Xorg.\d+.log as
  XFree86.\d+.log.

* Wed Nov 21 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-15mdv2008.1
+ Revision: 110991
- Avoid risk of deferencing a "reallocated" pointer in commands.c.
  Some review of the regex search code. Better detecting when needs to recompile
  the regex search. Better handling of escape sequences (that code is very hard
  to maintain due to too many gotos, and in a previous patch I added a wrong
  fix for character escaping, fixed now).
  The fix for proper checking if the file ends in a newline actually ended up
  showing another bug, where the code, due to the logic updating offsets, would
  always try to match the empty string just after a newline, what caused it to
  call the reexec function with an invalid argument (negative length string);
  problem fixed in this patch.
  Add proper check in tags.c; if a function can return null, the caller should
  check the returned value before deferencing it :-)

* Mon Nov 19 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-14mdv2008.1
+ Revision: 110436
- Some cleanup/padronization on messes printed to the message window.
  Fix an issue, that maybe should really be fixed in Xaw, where using XtSetValues
  to change the contents of a TextWidget will not properly horizontal scroll. The
  was to call the internal Xaw function "_XawTextShowPosition" always the problem
  could occur.
  Fix a bad reference to realloc'ed memory when expanding home directories. The
  code was also wrong, i.e. code like:  "ptr1 = ptr + num; ... ptr = realloc(ptr);
  ... memcpy(ptr1, value);"  When realloc'ing ptr, it could change address.
  Fix tags search patterns to properly handle escaped backslashes.
  Fix problem matching patterns in the last line of a file due to buggy checking
  if file ends in a newline.
  When repeated text is sent to the messagewindow, it will show the number of
  times it repeated, instead of printing again.

* Wed Nov 14 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-13mdv2008.1
+ Revision: 108671
- Update to my latest xorg git diff.
  Properly list directory contents on empty directories (i.e. pressing Tab
  on the filenamewindow will show ./ and ../, instead of doing nothing).
  Fix a bug in the generic regex search and that extended to the tags search
  where it would not find patterns in the last line of a file due to a bug
  involving checking if file ends or not in a newline.
  Better patch to initialize/associate a tags file with the *scratch* buffer,
  so it can be used to type symbols and search a tags (selected text and
  press "Alt-.")
- Minor patch to allow typing a symbol in the *scratch* buffer to search for
  a symbol definition, i.e. add tags pointer to the scratch buffer. It probably
  would be better to have a fully featured dialog box to manage tags searches...
  Fix what appears to be an old bug the became clear now, and could cause some
  corruption in the "File Menu" as it was passing the wrong string to the menu
  entry creation routine.

* Tue Nov 13 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-12mdv2008.1
+ Revision: 108439
- Update the XeditPrintf to work correctly. This was dumb but was the "original
  version". Now all calls properly handle parameters.
  Rewrite the tags interface. Now instead of loading a single tags file, when
  loading a new file, unless the resource tagsName starts with '/', it will
  descend up to the root directory searching for a tags file, and associate it
  with the loaded file. Loaded tags are in a global tags hash table.
  When searching for a symbol tag, if it is not found, check if there exists
  other available tags files, searching down to the root directory again.
  If still failing, check if there are loaded tags associated with other
  directory trees until finding the symbol tag or traversing all loaded tags, in
  no specific order.

* Mon Nov 12 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-11mdv2008.1
+ Revision: 108250
- Use correct INSTALL file. Messed on rebuilding and it generated the "default"
  symbolic link to automake version.
  Correct Requires, aspell-en instead of aspell-us and grep instead of grep
  Make sure the correct Xedit.ad is generated so that the correct actions will
  be available after package is installed.

* Mon Nov 12 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-10mdv2008.1
+ Revision: 108229
- Add diff patch from a local git branch.
  Add more Requires.
  See the updated README, INSTALL, AUTHORS, etc for more details.
- Add conditional around BuildRequires.
- Update the 'resolve name' patch to make a copy of the string, so that, if there
  are no allocations during calls, free(str); str=malloc(size) should never return
  the same pointer, i.e. what the patch tries to fix.
  Add readdir patch, that removes the assumption that '.' and '..' are always the
  2 first entries in a directory, i.e. the 2 first values returned by readdir().

* Fri Oct 19 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-8mdv2008.1
+ Revision: 100508
- Remake ResolveName patch. It depends on compiling with -O2 or not, as it was
  using a static buffer to store the result of calls to realpath and some
  optimization was messing things.
  Now it calls free() and malloc() at every invocation of the code using the
  static variable, so that the glibc realpath will not try to be smart using
  the static pointer.
  Also add minor fix changing a code like:
  if (buffer[i] && i < sizeof(buffer))
  to
  if (i < sizeof(buffer) && buffer[i])

* Thu Sep 20 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-7mdv2008.0
+ Revision: 91580
- Update correct patch.
- Add patch file to spec, not just command to use it...
- Revert the original 'hackish' XeditPrintf that just prints an string.
  At least for the moment, otherwise, code could send printf formats in a string
  that wasn't expected to be used by vsnprintf.
  Problem observed when loading a file with the %% character in it's name.

* Tue Sep 11 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-6mdv2008.0
+ Revision: 84432
- Fix fonts required by xedit for different edit modes, to install the minimum
  ammount of required packages.

* Wed Sep 05 2007 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-5mdv2008.0
+ Revision: 80345
- Compile without xprint support by default and fix a few problems.

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-4mdv2008.0
+ Revision: 76439
- rebuild for 2008
- simplify file list
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!


* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:23:32 (59548)
- rebuild to fix libXaw.so.8 dependency

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:24:58 (31400)
- fill in a couple of missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

