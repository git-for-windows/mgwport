%define debug_package %{nil}

Name:           mgwport
Version:        0.10.6
Release:        1%{?dist}
Summary:        MinGW package building tool

License:        GPLv3+
Group:          Development/Tools
URL:            http://www.mingw.org
Source0:        http://downloads.sourceforge.net/mingw/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

# for building documentation (TODO: add to EXTRA_DIST)
BuildRequires:  groff
BuildRequires:  help2man
BuildRequires:  robodoc

Requires:       autoconf automake libtool pkgconfig
Requires:       xz xz-lzma-compat bzip2 gzip unzip
Requires:       mingw-binutils
Requires:       mingw-gcc
Requires:       diffstat
Requires:       diffutils
Requires:       file
Requires:       grep
Requires:       imake
Requires:       make
Requires:       patch
Requires:       rsync
Requires:       util-linux
Requires:       wget


%description
MinGW package building tool.


%prep
%setup -q


%build
%configure --docdir=%{_docdir}/%{name}-%{version}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

# First install all the files belonging to the shared build
make DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/update-mime-database ${_datadir}/mime &> /dev/null || :


%postun
/usr/bin/update-mime-database ${_datadir}/mime &> /dev/null || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO doc/mgwport.1.html doc/manual.css doc/manual.html
%config %{_sysconfdir}/bash_completion.d/mgwport-bash-completion
%config(noreplace) %{_sysconfdir}/mgwport.conf
%{_bindir}/mgwport
%{_libdir}/mgwport
%{_datadir}/mgwport
%{_datadir}/mime/packages/mgwport.xml
%{_mandir}/man1/mgwport.1.gz


%changelog
* Fri Oct 28 2011 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 0.10.6-1
- Version bump.
- Call update-mime-database in post and postun for the new MIME package.

* Tue Aug 30 2011 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 0.10.5-1
- Version bump.

* Thu Mar 17 2011 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 0.10.4-1
- Version bump.

* Wed Mar 16 2011 Yaakov Selkowitz <cygwin-ports-general@lists.sourceforge.net> - 0.10.3-1
- Initial RPM release.
