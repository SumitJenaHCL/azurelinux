Summary:        Mock a DNS Resolver object for testing
Name:           perl-Net-DNS-Resolver-Mock
Version:        1.20200215
Release:        3%{?dist}
License:        GPL+ OR Artistic
Vendor:         Microsoft Corporation
Distribution:   Azure Linux
URL:            https://metacpan.org/release/Net-DNS-Resolver-Mock
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/Net-DNS-Resolver-Mock-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Net::DNS::Packet)
BuildRequires:  perl(Net::DNS::Question)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::DNS::ZoneFile)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
BuildArch:      noarch

%description
A subclass of Net::DNS::Resolver which parses a zonefile for it's data
source. Primarily for use in testing.

%prep
%autosetup -n Net-DNS-Resolver-Mock-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 07 2023 Muhammad Falak <mwani@microsoft.com> - 1.20200215-3
- License verified

* Fri Oct 15 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 1.20200215-2
- Initial CBL-Mariner import from Fedora 32 (license: MIT).

* Mon Feb 17 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.20200215-1
- 1.20200215 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.20171219-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20171219-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.20171219-6
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20171219-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20171219-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.20171219-3
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20171219-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.20171219-1
- 1.20171219 bump

* Wed Nov 01 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.20171031-1
- 1.20171031 bump

* Thu Oct 19 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.20170814-1
- Specfile autogenerated by cpanspec 1.78.
