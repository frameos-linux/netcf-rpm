%define dist frameos

Name:           netcf
Version:        0.1.6
Release:        1%{?dist}%{?extra_release}
Summary:        Cross-platform network configuration library

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            https://fedorahosted.org/netcf/
Source0:        https://fedorahosted.org/released/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  readline-devel augeas-devel >= 0.5.2
BuildRequires:  libxml2-devel libxslt-devel libnl-devel
Requires:       %{name}-libs = %{version}-%{release}

%description
A library for modifying the network configuration of a system. Network
configurations are expresed in a platform-independent XML format, which
netcf translates into changes to the system's 'native' network
configuration files.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        libs
Summary:        Libraries for %{name}
Group:          System Environment/Libraries

%description    libs
The libraries for %{name}.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/ncftool

%files libs
%defattr(-,root,root,-)
%{_datadir}/netcf
%{_libdir}/*.so.*
%doc AUTHORS COPYING NEWS

%files devel
%defattr(-,root,root,-)
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/netcf.pc

%changelog
* Thu Jul 01 2010 Sergio Rubio <sergio@rubio.name> - 0.1.6-1
- New Version

* Fri Sep 25 2009 David Lutterkort <lutter@redhat.com> - 0.1.2-1
- New Version

* Wed Sep 16 2009 David Lutterkort <lutter@redhat.com> - 0.1.1-1
- New Version

* Mon Jul 13 2009 David Lutterkort <lutter@redhat.com> - 0.1.0-1
- BR on augeas-0.5.2
- Drop explicit requires for augeas-libs

* Wed Apr 15 2009 David Lutterkort <lutter@redhat.com> - 0.0.2-1
- Updates acording to Fedora review

* Fri Feb 27 2009 David Lutterkort <lutter@redhat.com> - 0.0.1-1
- Initial specfile
