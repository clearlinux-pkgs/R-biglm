#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-biglm
Version  : 0.9.2
Release  : 27
URL      : https://cran.r-project.org/src/contrib/biglm_0.9-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/biglm_0.9-2.tar.gz
Summary  : bounded memory linear and generalized linear models
Group    : Development/Tools
License  : GPL-2.0
Requires: R-biglm-lib = %{version}-%{release}
Requires: R-DBI
Requires: R-leaps
BuildRequires : R-DBI
BuildRequires : R-leaps
BuildRequires : buildreq-R

%description
This is basically Alan Miller's modification (AS274) of the other
Gentleman's (AS 75) regression by incremental QR decomposition. It has
been lifted out of the "leaps" package and wrapped with an lm-like
interface to make experimentation easier.

%package lib
Summary: lib components for the R-biglm package.
Group: Libraries

%description lib
lib components for the R-biglm package.


%prep
%setup -q -c -n biglm
cd %{_builddir}/biglm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1590518045

%install
export SOURCE_DATE_EPOCH=1590518045
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library biglm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library biglm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library biglm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc biglm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/biglm/DESCRIPTION
/usr/lib64/R/library/biglm/INDEX
/usr/lib64/R/library/biglm/Meta/Rd.rds
/usr/lib64/R/library/biglm/Meta/features.rds
/usr/lib64/R/library/biglm/Meta/hsearch.rds
/usr/lib64/R/library/biglm/Meta/links.rds
/usr/lib64/R/library/biglm/Meta/nsInfo.rds
/usr/lib64/R/library/biglm/Meta/package.rds
/usr/lib64/R/library/biglm/NAMESPACE
/usr/lib64/R/library/biglm/NEWS
/usr/lib64/R/library/biglm/R/biglm
/usr/lib64/R/library/biglm/R/biglm.rdb
/usr/lib64/R/library/biglm/R/biglm.rdx
/usr/lib64/R/library/biglm/help/AnIndex
/usr/lib64/R/library/biglm/help/aliases.rds
/usr/lib64/R/library/biglm/help/biglm.rdb
/usr/lib64/R/library/biglm/help/biglm.rdx
/usr/lib64/R/library/biglm/help/paths.rds
/usr/lib64/R/library/biglm/html/00Index.html
/usr/lib64/R/library/biglm/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/biglm/libs/biglm.so
/usr/lib64/R/library/biglm/libs/biglm.so.avx2
/usr/lib64/R/library/biglm/libs/biglm.so.avx512
