%{!?python3_pkgversion:%global python3_pkgversion 3}

# EL7 does not have a new enough python-setuptools
%if 0%{?rhel} && 0%{?rhel} <= 7
%global with_python2 0
%else
%global with_python2 1
%endif

%global srcname setuptools_scm

Name:           python-%{srcname}
Version:        1.17.0
Release:        3.CROC1TEST%{?dist}
Summary:        The blessed package to manage your versions by scm tags

License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://github.com/pypa/setuptools_scm/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

# For tests
BuildRequires:  git-core
BuildRequires:  mercurial

%description
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%package -n python2-%{srcname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-pytest

%description -n python2-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

Provides: python36-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%prep
%setup -q -n %{srcname}-%{version}

%build
%if 0%{?with_python2}
%py2_build
%endif
%py3_build

%install
%if 0%{?with_python2}
%py2_install
%endif
%py3_install

%if 0%{?with_python2}
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -vv
%endif
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -vv
# Cleanup stray .pyc files from running python in python3 tests
rm -f %{buildroot}%{python3_sitelib}/%{srcname}/*.pyc

%if 0%{?with_python2}
%files -n python2-%{srcname}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python2_sitelib}/*
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/*

%changelog
* Mon Jan 25 2021 Andrey Kulaev <adkulaev@gmail.com> - 1.17.0-3 CROC1
- Add to c2 project

* Thu Mar 07 2019 Troy Dawson <tdawson@redhat.com> - 1.17.0-3
- Rebuilt to change main python from 3.4 to 3.6

* Tue Feb 12 2019 Scott K Logan <logans@cottsay.net> - 1.17.0-2
- Add Python 3.6 subpackage for EPEL 7

* Wed Feb 06 2019 Miro Hrončok <mhroncok@redhat.com> - 1.17.0-1
- Update to 1.17.0 to fix tests (#1672741)

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-2
- No python2 package on EPEL (setuptools too old)

* Thu Dec 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-1
- Update to 1.10.1

* Wed Dec 2 2015 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-1
- Update to 1.9.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-2
- Cleanup stray .pyc files from tests

* Sat Sep 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-1
- Update to 1.8.0
- Fix license tag

* Mon Sep 14 2015 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-1
- Initial package
