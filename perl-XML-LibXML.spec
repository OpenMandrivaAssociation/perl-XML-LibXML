%define upstream_name    XML-LibXML
%define upstream_version 1.69

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl Binding for libxml2
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:     XML-LibXML-1.69-fix-format-errors.patch

BuildRequires:      libxml2-devel >= 2.4.20
BuildRequires:      perl(XML::NamespaceSupport)
BuildRequires:      perl(XML::SAX)
BuildRequires:      perl(XML::LibXML::Common)
BuildRequires:      perl-devel
BuildRoot:          %{_tmppath}/%{name}-%{version}-%{release}
Obsoletes:          perl-XML-LibXML-XPathContext
Requires(post):     libxml2
Requires(post):     perl-XML-SAX >= 0.11
Requires(post):     perl-XML-LibXML-Common
Requires(preun):    libxml2
Requires(preun):    perl-XML-SAX >= 0.11
Requires(preun):    perl-XML-LibXML-Common

%description
This module implements much of the DOM Level 2 API as an 
interface to the Gnome libxml2 library. This makes it a fast
and highly capable validating XML parser library, as well as
a high performance DOM.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p 1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%optflags" SKIP_SAX_INSTALL=1
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

