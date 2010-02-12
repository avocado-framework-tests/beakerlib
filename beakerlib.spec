Name:       beakerlib
Summary:    A shell-level integration testing library
Version:    1.0
Release:    2%{?dist}
License:    GPLv2
Group:      Development/Libraries
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
Source0:    %{name}-%{version}.tar.gz
BuildArch:  noarch
URL:        https://fedorahosted.org/beakerlib/attachment/wiki/tarballs/beakerlib-1.0.tar.gz

%description
The BeakerLib project means to provide a library of various helpers, which
could be used when writing operating system level integration tests.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%dir %{_docdir}/%{name}
%{_datadir}/%{name}/dictionary.vim
%{_datadir}/%{name}/*.sh
%{_bindir}/%{name}-*
%{_mandir}/man1/beakerlib*1*
%doc %{_docdir}/beakerlib/*

%changelog

* Fri Feb 12 2010 Petr Muller <pmuller@redhat.com> - 1.0-2
- zillion of specfile tweaks for Fedora inclusion
- staf-rhts files were removed
- added a LICENSE file
- added a better package summary
- directory structure revamped
- improved rLDejaSum

* Wed Jan 27 2010 Petr Muller <pmuller@redhat.com> - 1.0-1
- genesis of the standalone BeakerLib
