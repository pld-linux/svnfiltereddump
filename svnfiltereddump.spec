%define		subver	beta4
%define		rel		1
Summary:	Tool to extract portions from Subversion repositories
Name:		svnfiltereddump
Version:	1.0
Release:	0.%{subver}.%{rel}
License:	GPL
Group:		Development/Version Control
Source0:	https://github.com/TNG/svnfiltereddump/tarball/master/%{name}-%{version}%{subver}.tgz
# Source0-md5:	a0471604afd2edc8ff0df878cd7b5ee7
URL:		https://github.com/TNG/svnfiltereddump
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The svnfiltereddump tool is meant to extract portions of repositories
of the Subversion source control system. It's output can be loaded
with Subversion's "svnadmin load" command into a new Subversion
repository. The source repository must be given on the command line. A
list of paths to extract may given on command line or in one or more
input file(s). It is also possible to skip the revision history before
a given starting revision.

%prep
%setup -qc
mv *-%{name}-*/* .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}-%{version}%{subver}-py*.egg-info
