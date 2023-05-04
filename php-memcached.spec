#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-memcached
Version  : 3.2.0
Release  : 32
URL      : https://pecl.php.net/get/memcached-3.2.0.tgz
Source0  : https://pecl.php.net/get/memcached-3.2.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT PHP-3.01
Requires: php-memcached-lib = %{version}-%{release}
Requires: php-memcached-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : pkgconfig(libmemcached)
BuildRequires : pkgconfig(zlib)

%description
Build Status
------------
[![Build Status](https://travis-ci.org/php-memcached-dev/php-memcached.png)](https://travis-ci.org/php-memcached-dev/php-memcached)

%package lib
Summary: lib components for the php-memcached package.
Group: Libraries
Requires: php-memcached-license = %{version}-%{release}

%description lib
lib components for the php-memcached package.


%package license
Summary: license components for the php-memcached package.
Group: Default

%description license
license components for the php-memcached package.


%prep
%setup -q -n memcached-3.2.0
cd %{_builddir}/memcached-3.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static --disable-memcached-sasl
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-memcached
cp %{_builddir}/memcached-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-memcached/e2815bf94c6ff64afbc20d3403dc45ea5c73c6f0
cp %{_builddir}/memcached-%{version}/fastlz/LICENSE %{buildroot}/usr/share/package-licenses/php-memcached/350f74b0e80aa38c5a75d8de5f367706920fdaa4
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/memcached.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-memcached/350f74b0e80aa38c5a75d8de5f367706920fdaa4
/usr/share/package-licenses/php-memcached/e2815bf94c6ff64afbc20d3403dc45ea5c73c6f0
