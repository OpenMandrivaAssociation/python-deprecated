%define module deprecated
%define oname Deprecated

Name:		python-deprecated
Summary:	Python @deprecated decorator to deprecate old python classes, functions or methods.
Version:	1.3.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL:		https://pypi.org/project/deprecated/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Python @deprecated decorator to deprecate old python classes, functions or methods.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%doc README.md
%license LICENSE.rst
%{py_sitedir}/%{module}
%{py_sitedir}/%{module}-%{version}.dist-info
