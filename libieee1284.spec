Summary:	A library for interfacing IEEE 1284-compatible devices
Summary(pl):	Biblioteka do komunikacji z urz±dzeniami kompatybilnymi z IEEE 1284
Name:		libieee1284
Version:	0.2.1
Release:	2
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/%{name}/%{name}-%{version}.tar.bz2
Patch0:		%{name}-no_sys_io.h.patch
URL:		http://cyberelk.net/tim/libieee1284/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libieee1284 library is for communicating with parallel port
devices.

%description -l pl
Biblioteka libieee1284 s³u¿y do komunikacji z urz±dzeniami
pod³±czanymi do portu równoleg³ego.

%package devel
Summary:	Files for developing applications that use libieee1284
Summary(pl):	Pliki do tworzenia programów u¿ywaj±cych libieee1284
Requires:	%{name} = %{version}
Group:		Development/Libraries

%description devel
The header files, libtool library and man pages for developing
applications that use libieee1284.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do tworzenia programów u¿ywaj±cych
libieee1284.

%package static
Summary:	Static version of libieee1284
Summary(pl):	Statyczna wersja libieee1284
Requires:	%{name} = %{version}
Group:		Development/Libraries

%description static
Static version of libieee1284 library.

%description static -l pl
Statyczna wersja biblioteki libieee1284.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cd $RPM_BUILD_ROOT%{_mandir}/man3

echo ".so ieee1284_control.3" > ieee1284_read_control.3
echo ".so ieee1284_control.3" > ieee1284_write_control.3
echo ".so ieee1284_control.3" > ieee1284_frob_control.3
echo ".so ieee1284_control.3" > ieee1284_do_nack_handshake.3
echo ".so ieee1284_data.3" > ieee1284_read_data.3
echo ".so ieee1284_data.3" > ieee1284_write_data.3
echo ".so ieee1284_data.3" > ieee1284_data_dir.3
echo ".so ieee1284_ecp_fwd_to_rev.3" > ieee1284_ecp_rev_to_fwd.3
echo ".so ieee1284_negotiation.3" > ieee1284_negotiate.3
echo ".so ieee1284_negotiation.3" > ieee1284_terminate.3
echo ".so ieee1284_status.3" > ieee1284_read_status.3
echo ".so ieee1284_status.3" > ieee1284_wait_status.3
for fn in nibble_read compat_write byte_read epp_read_data \
	epp_write_data epp_read_addr epp_write_addr ecp_read_data \
	ecp_write_data ecp_read_addr ecp_write_addr; do
	echo ".so ieee1284_transfer.3" > ieee1284_${fn}.3
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/ieee1284.h
%attr(755,root,root) %{_libdir}/*.so
%attr(755,root,root) %{_libdir}/*.la
%{_mandir}/man?/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
