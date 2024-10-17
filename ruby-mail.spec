%define gemname mail
Summary:	A really Ruby Mail handler
Name:		ruby-%{gemname}
Version:	2.4.4
Release:	2
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		https://www.rubyonrails.org/
BuildArch:	noarch
BuildRequires:	ruby-RubyGems
%rename		rubygem-%{gemname}

%description
A really Ruby Mail handler.

%prep
%setup -c

%build

%install
rm -rf %{buildroot}

gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%defattr(-,root,root)
%{ruby_gemdir}/gems/%{gemname}-%{version}
%{ruby_gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{gemname}-%{version}


%changelog
* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.4.4-1
+ Revision: 796024
- update to 2.4.4
- rename
- rename to comply ruby packaging policy

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.4.1-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 2.4.1-1
+ Revision: 769755
- Initial mdv package
- Created package structure for 'rubygem-mail'.

