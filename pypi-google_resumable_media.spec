#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-google_resumable_media
Version  : 2.4.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/88/11/ea0db6fe28017487dd1e2c6bc3623ea2dc4655947d6f571c6207b6d9693c/google-resumable-media-2.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/88/11/ea0db6fe28017487dd1e2c6bc3623ea2dc4655947d6f571c6207b6d9693c/google-resumable-media-2.4.1.tar.gz
Summary  : Utilities for Google Media Downloads and Resumable Uploads
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-google_resumable_media-license = %{version}-%{release}
Requires: pypi-google_resumable_media-python = %{version}-%{release}
Requires: pypi-google_resumable_media-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(google_crc32c)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
``google-resumable-media``
==========================
Utilities for Google Media Downloads and Resumable Uploads

%package license
Summary: license components for the pypi-google_resumable_media package.
Group: Default

%description license
license components for the pypi-google_resumable_media package.


%package python
Summary: python components for the pypi-google_resumable_media package.
Group: Default
Requires: pypi-google_resumable_media-python3 = %{version}-%{release}

%description python
python components for the pypi-google_resumable_media package.


%package python3
Summary: python3 components for the pypi-google_resumable_media package.
Group: Default
Requires: python3-core
Provides: pypi(google_resumable_media)
Requires: pypi(google_crc32c)

%description python3
python3 components for the pypi-google_resumable_media package.


%prep
%setup -q -n google-resumable-media-2.4.1
cd %{_builddir}/google-resumable-media-2.4.1
pushd ..
cp -a google-resumable-media-2.4.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1675274544
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-google_resumable_media
cp %{_builddir}/google-resumable-media-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-google_resumable_media/2b8b815229aa8a61e483fb4ba0588b8b6c491890 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-google_resumable_media/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*