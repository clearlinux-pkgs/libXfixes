#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x687393EE37D128F8 (matthieu@herrb.eu)
#
Name     : libXfixes
Version  : 5.0.3
Release  : 16
URL      : http://xorg.freedesktop.org/releases/individual/lib/libXfixes-5.0.3.tar.bz2
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libXfixes-5.0.3.tar.bz2
Source99 : http://xorg.freedesktop.org/releases/individual/lib/libXfixes-5.0.3.tar.bz2.sig
Summary  : X Fixes  Library
Group    : Development/Tools
License  : HPND
Requires: libXfixes-lib
Requires: libXfixes-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xextproto)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(fixesproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
Xfixes
XFIXES Extension
Version 2.0.1
2002-10-4
This package contains header files and documentation for the XFIXES
extension.  Library and server implementations are separate.

%package dev
Summary: dev components for the libXfixes package.
Group: Development
Requires: libXfixes-lib
Provides: libXfixes-devel

%description dev
dev components for the libXfixes package.


%package dev32
Summary: dev32 components for the libXfixes package.
Group: Default
Requires: libXfixes-lib32
Requires: libXfixes-dev

%description dev32
dev32 components for the libXfixes package.


%package doc
Summary: doc components for the libXfixes package.
Group: Documentation

%description doc
doc components for the libXfixes package.


%package lib
Summary: lib components for the libXfixes package.
Group: Libraries

%description lib
lib components for the libXfixes package.


%package lib32
Summary: lib32 components for the libXfixes package.
Group: Default

%description lib32
lib32 components for the libXfixes package.


%prep
%setup -q -n libXfixes-5.0.3
pushd ..
cp -a libXfixes-5.0.3 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492279313
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492279313
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/Xfixes.h
/usr/lib64/libXfixes.so
/usr/lib64/pkgconfig/xfixes.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libXfixes.so
/usr/lib32/pkgconfig/32xfixes.pc
/usr/lib32/pkgconfig/xfixes.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libXfixes.so.3
/usr/lib64/libXfixes.so.3.1.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libXfixes.so.3
/usr/lib32/libXfixes.so.3.1.0
