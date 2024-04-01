# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-typeguard
Epoch: 100
Version: 4.2.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Run-time type checker for Python
License: MIT
URL: https://github.com/agronholm/typeguard/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This library provides run-time type checking for functions defined with
PEP 484 argument (and return) type annotations, and any arbitrary
objects. It can be used together with static type checkers as an
additional layer of type safety, to catch type violations that could
only be detected at run time.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-typeguard
Summary: Run-time type checker for Python
Requires: python3
Provides: python3-typeguard = %{epoch}:%{version}-%{release}
Provides: python3dist(typeguard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typeguard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typeguard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typeguard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typeguard) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-typeguard
This library provides run-time type checking for functions defined with
PEP 484 argument (and return) type annotations, and any arbitrary
objects. It can be used together with static type checkers as an
additional layer of type safety, to catch type violations that could

%files -n python%{python3_version_nodots}-typeguard
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-typeguard
Summary: Run-time type checker for Python
Requires: python3
Provides: python3-typeguard = %{epoch}:%{version}-%{release}
Provides: python3dist(typeguard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typeguard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typeguard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typeguard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typeguard) = %{epoch}:%{version}-%{release}

%description -n python3-typeguard
This library provides run-time type checking for functions defined with
PEP 484 argument (and return) type annotations, and any arbitrary
objects. It can be used together with static type checkers as an
additional layer of type safety, to catch type violations that could
only be detected at run time.

%files -n python3-typeguard
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-typeguard
Summary: Run-time type checker for Python
Requires: python3
Provides: python3-typeguard = %{epoch}:%{version}-%{release}
Provides: python3dist(typeguard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typeguard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typeguard) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typeguard = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typeguard) = %{epoch}:%{version}-%{release}

%description -n python3-typeguard
This library provides run-time type checking for functions defined with
PEP 484 argument (and return) type annotations, and any arbitrary
objects. It can be used together with static type checkers as an
additional layer of type safety, to catch type violations that could
only be detected at run time.

%files -n python3-typeguard
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
