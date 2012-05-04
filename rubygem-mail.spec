%define gemname mail
Summary:	A really Ruby Mail handler
Name:		rubygem-%{gemname}
Version:	2.4.1
Release:	2
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
BuildRoot:	%{_tmppath}/%{gemname}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	ruby-RubyGems

%description
A really Ruby Mail handler.

%prep
%setup -c

%build

%install
rm -rf $RPM_BUILD_ROOT

gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{ruby_gemdir}/gems/%{gemname}-%{version}
%{ruby_gemdir}/specifications/%{gemname}-%{version}.gemspec
%doc %{ruby_gemdir}/doc/%{gemname}-%{version}
