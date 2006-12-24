# TODO:
# -separate packages with themes

Summary:	XMMS - applet for controlling XMMS from the KDE panel
Summary(pl):	Aplet do kontrolowania XMMS-a z panelu KDE
Name:		xmms-kde
Version:	3.2
Release:	2
Epoch:		1
License:	GPL v2
Vendor:		Flo Niebling <tranqlzer@users.sourceforge.net>
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/xmms-kde/%{name}-%{version}.tar.gz
# Source0-md5:	7d5b69ce64650178d259faaf130fd88e
URL:		http://xmms-kde.sourceforge.net/
BuildRequires:	amarok
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	libart_lgpl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	smpeg-devel >= 0.4.2
BuildRequires:	xmms-devel >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS panel applet for the KDE panel (kicker). It is used to be able
to control XMMS without having to switch to the virtual desktop where
XMMS is running.

%description -l pl
Aplet XMMS dla panelu KDE (kickera). S³u¿y do kontrolowania XMMS-a bez
konieczno¶ci prze³±czania siê na wirtualny pulpit, na którym dzia³a
XMMS.

%prep
%setup -q

%build
kde_htmldir=%{_kdedocdir}; export kde_htmldir
CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti -fno-implicit-templates"
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO doc/themes.txt
%attr(755,root,root) %{_libdir}/kde3/libxmmskde.so
%{_libdir}/kde3/libxmmskde.la
%{_datadir}/apps/xmms-kde
%{_datadir}/apps/kicker/applets/xmms-kde.desktop
