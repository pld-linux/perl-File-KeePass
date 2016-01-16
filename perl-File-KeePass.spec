#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	File
%define		pnam	KeePass
%include	/usr/lib/rpm/macros.perl
Summary:	File::KeePass - Interface to KeePass V1 and V2 database files
Name:		perl-File-KeePass
Version:	2.03
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	085da6ef1ada886ca3e9b8724fc213b3
URL:		http://search.cpan.org/dist/File-KeePass/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Crypt::Rijndael) >= 1.0
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File::KeePass gives access to KeePass version 1 (kdb) and version 2
(kdbx) databases.

The version 1 and version 2 databases are very different in
construction, but the majority of information overlaps and many
algorithms are similar. File::KeePass attempts to iron out as many of
the differences.

File::KeePass gives nearly raw data access. There are a few utility
methods for manipulating groups and entries. More advanced
manipulation can easily be layered on top by other modules.

File::KeePass is only used for reading and writing databases and for
keeping passwords scrambled while in memory. Programs dealing with UI
or using of auto-type features are the domain of other modules on
CPAN. File::KeePass::Agent is one example.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/File/*.pm
#{perl_vendorlib}/File/KeePass
%{_mandir}/man3/*
