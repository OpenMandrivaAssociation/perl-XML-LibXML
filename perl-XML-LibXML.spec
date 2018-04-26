%define	module XML-LibXML
%define modver 2.0132

Summary:	Perl Binding for libxml2
Name:		perl-%{module}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source0:	http://www.cpan.org/modules/by-module/XML/XML-LibXML-%{modver}.tar.gz
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	perl(XML::NamespaceSupport)
BuildRequires:	perl(XML::SAX)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(liblzma)
BuildRequires:	perl-devel
Obsoletes:	perl-XML-LibXML-XPathContext
Obsoletes:	perl-XML-LibXML-Common
Requires(post):	perl-XML-SAX >= 0.11
Requires(preun):	perl-XML-SAX >= 0.11

%description
This module implements much of the DOM Level 2 API as an 
interface to the Gnome libxml2 library. This makes it a fast
and highly capable validating XML parser library, as well as
a high performance DOM.

%prep
%setup -q -n %{module}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" SKIP_SAX_INSTALL=1 DEBUG=1
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
