#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (useful for <3.7 only)

Summary:	Backport of new features in Python's tempfile module
Summary(pl.UTF-8):	Backport nowej funkcjonalności modułu Pythona tempfile
Name:		python-backports.tempfile
Version:	1.0
Release:	1
License:	PSF
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/backports.tempfile/
Source0:	https://files.pythonhosted.org/packages/source/b/backports.tempfile/backports.tempfile-%{version}.tar.gz
# Source0-md5:	f9576dcd07de140f0ad2327c8801ef3d
URL:		https://pypi.org/project/backports.tempfile/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-backports.test.support
BuildRequires:	python-backports.weakref
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-backports.test.support
BuildRequires:	python3-backports.weakref
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides backports of new features in Python's tempfile
module under the "backports" namespace.

%description -l pl.UTF-8
Ten pakiet zawiera backport nowej funkcjonalności modułu Pythona
tempfile, umieszczony w przestrzeni nazw "backports".

%package -n python3-backports.tempfile
Summary:	Backport of new features in Python's tempfile module
Summary(pl.UTF-8):	Backport nowej funkcjonalności modułu Pythona tempfile
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-backports.tempfile
This package provides backports of new features in Python's tempfile
module under the "backports" namespace.

%description -n python3-backports.tempfile -l pl.UTF-8
Ten pakiet zawiera backport nowej funkcjonalności modułu Pythona
tempfile, umieszczony w przestrzeni nazw "backports".

%prep
%setup -q -n backports.tempfile-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python} -m unittest discover tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m unittest discover tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

# packaged in python-backports
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/backports/__init__.py*
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/backports/tempfile.py[co]
%{py_sitescriptdir}/backports.tempfile-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-backports.tempfile
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/backports/tempfile.py
%{py3_sitescriptdir}/backports/__pycache__/tempfile.cpython-*.py[co]
%{py3_sitescriptdir}/backports.tempfile-%{version}-py*.egg-info
%endif
