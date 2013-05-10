# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       nemo-qml-plugin-policy-qt5

# >> macros
# << macros

Summary:    Resource policy plugin for Nemo Mobile
Version:    0.0.0
Release:    1
Group:      System/Libraries
License:    BSD
URL:        https://github.com/nemomobile/nemo-qml-plugin-policy
Source0:    %{name}-%{version}.tar.bz2
Source100:  nemo-qml-plugin-policy-qt5.yaml
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(libresourceqt1-qt5)
Provides:   nemo-qml-plugins-policy-qt5

%description
%{summary}.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qmake 

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post


%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/org/nemomobile/policy/libnemopolicy.so
%{_libdir}/qt5/qml/org/nemomobile/policy/qmldir
# >> files
# << files
