#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-ToolKit
Summary:	Net::DNS::ToolKit - tools for working with DNS packets
Summary(pl):	Net::DNS::ToolKit - narzêdzia do pracy z pakietami DNS
Name:		perl-Net-DNS-ToolKit
Version:	0.17
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ed41a6787f5e89666ab7ed6048e4b56e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Routines to pick apart, examine and put together DNS packets. They can be
used for diagnostic purposes or as building blocks for DNS applications such
as DNS servers and clients or to allow user applications to interact
directly with remote DNS servers.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorarch}/Net/DNS/ToolKit.pm
%{perl_vendorarch}/Net/DNS/ToolKit
%{_mandir}/man3/*
