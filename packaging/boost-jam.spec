Name:           boost-jam
Version:        201104
Release:        0
Summary:        An Enhanced Make Replacement
License:        BSD-3-Clause
Group:          Development/Tools/Building
Source:         %{name}-%{version}.tar.xz
# From http://boost.cvs.sourceforge.net/boost/boost/tools/jam/test/:
Source2:        test.tar.gz 
Source1001: 	boost-jam.manifest
Url:            http://www.boost.org/
BuildRequires:  xz

%description
Boost Jam is a build tool based on FTJam, which in turn is based on
Perforce Jam. It contains significant improvements made to facilitate
its use in the Boost Build System, but should be backward compatible
with Perforce Jam.

%prep
%setup -q
cp %{SOURCE1001} .
find . -type f|xargs chmod -R u+w

%build
export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
export CFLAGS="$RPM_OPT_FLAGS"
LOCATE_TARGET=bin ./build.sh gcc --symbols
# Trivial test: -- Documented used of bjam -v: Print the version of jam and exit:
bin/bjam -v
ln  -s bin bin.linux
cd ..
tar xvf %{SOURCE2}
ln -s %{name}-%{version} src
cd test
sh test.sh || if [ $? -gt 5 ]; then sh test.sh;fi

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 755 bin/bjam %{buildroot}%{_bindir}/bjam-%{version}
ln -sf bjam-%{version} %{buildroot}%{_bindir}/bjam
ln -sf bjam-%{version} %{buildroot}%{_bindir}/jam

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/*

%changelog
