%define gemname mail
Summary:	A really Ruby Mail handler
Name:		ruby-%{gemname}
Version:	2.4.4
Release:	1
Source0:	http://rubygems.org/downloads/%{gemname}-%{version}.gem
License:	MIT
Group:		System/Servers
Url:		http://www.rubyonrails.org/
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
