Summary:	XMMS - applet for controlling xmms from the KDE panel
Summary(pl):	Aplet do kontrolowaniaa xmms z panelu KDE
Name:		xmms-kde 
Version:	0.6.5
Release:	2
Epoch:		1
License:	GPL
Vendor:		Flo Niebling <tranqlzer@users.sourceforge.net>
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://prdownloads.sourceforge.net/xmms-kde/%{name}-%{version}.tgz
URL:		http://xmms-kde.sourceforge.net
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
BuildRequires:	kdelibs-devel
BuildRequires:	xmms-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
Requires:	xmms
Requires:	kdelibs >= 2.0
Requires:	qt >= 2.1.1 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XMMS panel applet for the KDE2 panel (kicker). It is used to be able
to control XMMS without having to switch to the virtual desktop where
XMMS is running.

Email (author): tranqlzer@users.sourceforge.net

%description -l pl
Aplet XMMS dla panelu KDE2 (kickera). S³u¿y do kontrolowania XMMS bez
konieczno¶ci prze³±czania siê na wirtualny pulpit, na którym dzia³a
XMMS.

%prep 
%setup -q

%build 
%configure2_13 \
	--with-qt-includes=%{_includedir}/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog INSTALL README  TODO

%clean 
rm -rf $RPM_BUILD_ROOT 

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files 
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/libxmmskde.la
%{_libdir}/libxmmskde.so.*.*
%dir %{_datadir}/apps/xmms-kde
%{_datadir}/apps/kicker/applets/xmms-kde.desktop
%{_datadir}/apps/xmms-kde/*
