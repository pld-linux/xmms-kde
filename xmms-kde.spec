# TODO:
# -separate packages with themes
Summary:	XMMS - applet for controlling xmms from the KDE panel
Summary(pl):	Aplet do kontrolowaniaa xmms z panelu KDE
Name:		xmms-kde
Version:	3.0.0
Release:	3
Epoch:		1
License:	GPL v2
Vendor:		Flo Niebling <tranqlzer@users.sourceforge.net>
Group:		X11/Applications/Sound
Source0:	http://prdownloads.sourceforge.net/xmms-kde/xmmskde-%{version}.tar.gz
Patch0:		%{name}-no-version.patch
URL:		http://xmms-kde.sourceforge.net/
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	libjpeg-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	smpeg-devel >= 0.4.2
BuildRequires:	xmms-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%description
XMMS panel applet for the KDE panel (kicker). It is used to be able
to control XMMS without having to switch to the virtual desktop where
XMMS is running.

Email (author): tranqlzer@users.sourceforge.net

%description -l pl
Aplet XMMS dla panelu KDE (kickera). S�u�y do kontrolowania XMMS bez
konieczno�ci prze��czania si� na wirtualny pulpit, na kt�rym dzia�a
XMMS.

%prep
%setup -q -n xmmskde-3.0
%patch0 -p1

%build
kde_htmldir=%{_htmldir}; export kde_htmldir
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti -fno-implicit-templates"
%configure \
	--with-qt-includes=%{_includedir}/qt

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang xmmskde --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f xmmskde.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/themes.txt
%{_libdir}/kde3/libxmmskde.la
%{_libdir}/kde3/libxmmskde.so
%{_datadir}/apps/xmms-kde
%{_datadir}/apps/kicker/applets/xmms-kde.desktop