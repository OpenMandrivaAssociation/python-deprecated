Summary:	Python @deprecated decorator to deprecate old python classes, functions or methods.
Name:		python-deprecated
Version:	1.2.14
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/D/Deprecated/Deprecated-%{version}.tar.gz
URL:		https://pypi.org/project/deprecated/
License:	MIT
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python @deprecated decorator to deprecate old python classes, functions or methods.

%prep
%autosetup -p1 -n Deprecated-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/deprecated
%{py_sitedir}/Deprecated-*.*-info
