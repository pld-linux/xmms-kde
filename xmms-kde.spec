Summary:	XMMS - applet for controlling xmms from the KDE panel.
Name:		xmms-kde 
Version:	0.6.5
Release:	2
Epoch:		1
Source0:	http://prdownloads.sourceforge.net/xmms-kde/%{name}-%{version}.tgz
URL:		http://xmms-kde.sourceforge.net
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Vendor:		Flo Niebling <tranqlzer@users.sourceforge.net>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
License:	GPL
Requires:	xmms
Requires:	kdelibs >= 2.0
Requires:	qt >= 2.1.1 
BuildRequires:	libstdc++-devel
BuildRequires:	XFree86-devel
BuildRequires:	qt-devel
BuildRequires:	zlib-devel
BuildRequires:	kdelibs-devel
BuildRequires:	xmms-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
XMMS panel applet for the KDE2 panel (kicker). It is used to be able
to control XMMS without having to switch to the virtual desktop where
XMMS is running.

Email (author): tranqlzer@users.sourceforge.net

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

%files 
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/libxmmskde.la
%{_libdir}/libxmmskde.so
%{_libdir}/libxmmskde.so.1
%{_libdir}/libxmmskde.so.1.0.0
%dir %{_datadir}/apps/xmms-kde
%{_datadir}/apps/kicker/applets/xmms-kde.desktop
%{_datadir}/apps/xmms-kde/aluminum25.rc
%{_datadir}/apps/xmms-kde/aluminum25.tgz
%{_datadir}/apps/xmms-kde/aluminum42.rc
%{_datadir}/apps/xmms-kde/aluminum42.tgz
%{_datadir}/apps/xmms-kde/blueish.rc
%{_datadir}/apps/xmms-kde/blueish.tgz
%{_datadir}/apps/xmms-kde/horizontal25.rc
%{_datadir}/apps/xmms-kde/horizontal25.tgz
%{_datadir}/apps/xmms-kde/horizontalblue.rc
%{_datadir}/apps/xmms-kde/horizontalblue.tgz
%{_datadir}/apps/xmms-kde/noscreen.tgz
%{_datadir}/apps/xmms-kde/icons.tgz
%{_datadir}/apps/xmms-kde/small.rc
%{_datadir}/apps/xmms-kde/small.tgz
%{_datadir}/apps/xmms-kde/tiny.rc
%{_datadir}/apps/xmms-kde/tiny.tgz
%{_datadir}/apps/xmms-kde/vertical26.rc
%{_datadir}/apps/xmms-kde/vertical26.tgz
%{_datadir}/apps/xmms-kde/verticalblue.rc
%{_datadir}/apps/xmms-kde/verticalblue.tgz
%{_datadir}/apps/xmms-kde/wm60x26.rc
%{_datadir}/apps/xmms-kde/wm60x26.tgz
%{_datadir}/apps/xmms-kde/wm63x42.rc
%{_datadir}/apps/xmms-kde/wm63x42.tgz
%{_datadir}/apps/xmms-kde/xmms-kderc
