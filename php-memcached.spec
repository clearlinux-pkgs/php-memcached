#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-memcached
Version  : 3.2.0
Release  : 21
URL      : https://pecl.php.net/get/memcached-3.2.0.tgz
Source0  : https://pecl.php.net/get/memcached-3.2.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT PHP-3.01
Requires: php-memcached-lib = %{version}-%{release}
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

%description lib
lib components for the php-memcached package.


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
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/memcached.so
