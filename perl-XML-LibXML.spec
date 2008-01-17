%define module  XML-LibXML
%define name    perl-%{module}
%define version 1.65
%define release %mkrel 3

Name:               %{name}
Version:            %{version}
Release:            %{release}
Summary:            Perl Binding for libxml2
License:            GPL or Artistic
Group:              Development/Perl
Url:                http://search.cpan.org/dist/%{module}/
Source:             http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.bz2
Patch0:		    XML-LibXML-1.65-shut-up-warnings-in-XML-LibXML-Reader.patch
Requires(post):     libxml2
Requires(post):     perl-XML-SAX >= 0.11
Requires(post):     perl-XML-LibXML-Common
Requires(preun):    libxml2
Requires(preun):    perl-XML-SAX >= 0.11
Requires(preun):    perl-XML-LibXML-Common
BuildRequires:      libxml2-devel >= 2.4.20
BuildRequires:      perl-devel
BuildRequires:      perl(XML::NamespaceSupport)
BuildRequires:      perl(XML::SAX)
BuildRequires:      perl(XML::LibXML::Common)
Obsoletes:          perl-XML-LibXML-XPathContext
BuildRoot:          %{_tmppath}/%{name}-%{version}

%description
This module implements much of the DOM Level 2 API as an 
interface to the Gnome libxml2 library. This makes it a fast
and highly capable validating XML parser library, as well as
a high performance DOM.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
# only when building from CVS (version 1.51-3mdk)
#CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
#make docs -i
# only when building from CVS (version 1.51-3mdk)
SKIP_SAX_INSTALL=1 CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std

%preun -p %{__perl}
use XML::SAX;
XML::SAX->remove_parser(q(XML::LibXML::SAX::Parser))->save_parsers();

%post -p %{__perl}
use XML::SAX;
XML::SAX->add_parser(q(XML::LibXML::SAX::Parser))->save_parsers();

%files
%defattr(-,root,root)
%doc Changes README example/*
%{perl_vendorarch}/auto/XML/LibXML
%{perl_vendorarch}/XML/LibXML*
%{_mandir}/*/*

