#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	DNS-ToolKit
Summary:	Net::DNS::ToolKit - tools for working with DNS packets
Summary(pl.UTF-8):	Net::DNS::ToolKit - narzędzia do pracy z pakietami DNS
Name:		perl-Net-DNS-ToolKit
Version:	0.48
Release:	7
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	242fab98e7a4e195d63e554b42f6c12b
URL:		http://search.cpan.org/dist/Net-DNS-ToolKit/
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

%description -l pl.UTF-8
Procedury do wybierania, badania oraz składania pakietów DNS. Mogą być
użyte do celów diagnostycznych lub do tworzenia bloków dla aplikacji
NDS takich jak serwery oraz klienci DNS lub do umożliwienia
użytkownikowi do bezpośredniej interakcji ze zdalnymi serwerami DNS.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} -j1 \
	CC="%{__cc}" \
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
%{perl_vendorarch}/auto/Net/DNS/ToolKit/Debug
%{perl_vendorarch}/auto/Net/DNS/ToolKit/Utilities
%{_mandir}/man3/*
