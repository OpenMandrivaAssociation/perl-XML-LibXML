%define	module	XML-LibXML
%define	modver	1.98

Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	3

Summary:	Perl Binding for libxml2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/XML/%{module}-%{modver}.tar.gz

BuildRequires:	libxml2-devel >= 2.4.20
BuildRequires:	perl(XML::NamespaceSupport)
BuildRequires:	perl(XML::SAX)
BuildRequires:	perl-devel
Obsoletes:	perl-XML-LibXML-XPathContext
Obsoletes:	perl-XML-LibXML-Common
Requires(post):	perl-XML-SAX >= 0.11
Requires(preun):perl-XML-SAX >= 0.11

%description
This module implements much of the DOM Level 2 API as an 
interface to the Gnome libxml2 library. This makes it a fast
and highly capable validating XML parser library, as well as
a high performance DOM.

%prep
%setup -q -n %{module}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" SKIP_SAX_INSTALL=1
%make

%check
make test

%install
%makeinstall_std

%preun -p %{__perl}
use XML::SAX;
XML::SAX->remove_parser(q(XML::LibXML::SAX::Parser))->save_parsers();

%post -p %{__perl}
use XML::SAX;
XML::SAX->add_parser(q(XML::LibXML::SAX::Parser))->save_parsers();

%files
%doc Changes README example/*
%{perl_vendorarch}/auto/XML/LibXML
%{perl_vendorarch}/XML/LibXML*
%{_mandir}/*/*

%changelog
* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.980.0-3
- rebuild for new perl

* Fri May 25 2012 Crispin Boylan <crisb@mandriva.org> 1.980.0-1
+ Revision: 800699
- New release

