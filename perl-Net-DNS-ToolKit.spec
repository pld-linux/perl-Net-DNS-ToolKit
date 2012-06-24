#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	DNS-ToolKit
Summary:	Net::DNS::ToolKit - tools for working with DNS packets
Summary(pl):	Net::DNS::ToolKit - narz�dzia do pracy z pakietami DNS
Name:		perl-Net-DNS-ToolKit
Version:	0.24
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	25287b8b06db487f2635e93b7d8baf64
%if %{with tests}
BuildRequires:	perl-Net-DNS-Codes >= 0.06
BuildRequires:	perl-NetAddr-IP
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Routines to pick apart, examine and put together DNS packets. They can
be used for diagnostic purposes or as building blocks for DNS
applications such as DNS servers and clients or to allow user
applications to interact directly with remote DNS servers.

%description -l pl
Procedury do wybierania, badania oraz sk�adania pakiet�w DNS. Mog� by�
u�yte do cel�w diagnostycznych lub do tworzenia blok�w dla aplikacji
NDS takich jak serwery oraz klienci DNS lub do umo�liwienia
u�ytkownikowi do bezpo�redniej interakcji ze zdalnymi serwerami DNS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} -j1 \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Net/DNS/ToolKit/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README
%{perl_vendorarch}/Net/DNS/*.pm
%{perl_vendorarch}/Net/DNS/ToolKit
%dir %{perl_vendorarch}/auto/Net/DNS
%dir %{perl_vendorarch}/auto/Net/DNS/ToolKit
%attr(755,root,root) %{perl_vendorarch}/auto/Net/DNS/ToolKit/*.so
%{perl_vendorarch}/auto/Net/DNS/ToolKit/*.ix
%{perl_vendorarch}/auto/Net/DNS/ToolKit/*.al
%{perl_vendorarch}/auto/Net/DNS/ToolKit/*.bs
%{perl_vendorarch}/auto/Net/DNS/ToolKit/Debug
%{perl_vendorarch}/auto/Net/DNS/ToolKit/Utilities
%{_mandir}/man3/*
