#TODO - add support for applnk, now is only gnome-menus
Summary:	Desktop Dock and helper for GNOME
Summary(pl.UTF-8):	Dok i pomoc dla pulpitu GNOME
Name:		gimmie
Version:	0.2.8
Release:	10
License:	GPL
Group:		X11/Applications
Source0:	http://www.beatniksoftware.com/gimmie/releases/%{name}-%{version}.tar.gz
# Source0-md5:	721b8ec80f0247e1281aeb4aa5614c2f
URL:		http://www.beatniksoftware.com/gimmie/
BuildRequires:	gettext-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gnome-menus-editor
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libgnomecups-devel
BuildRequires:	libgnomeprintui-devel >= 1.0
BuildRequires:	perl-XML-Parser
BuildRequires:	pkgconfig
BuildRequires:	python-gnome-desktop-devel
BuildRequires:	rpm-pythonprov
Requires:	python-Numeric
Requires:	python-gnome-desktop-libwnck
Requires:	python-gnome-extras-egg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gimmie is an elegant way to think about how you use your desktop
computer.

%description -l pl.UTF-8
Gimmie to elegancki sposób myślenia jak używać komputera biurkowego.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,py}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/*.{la,py}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/*/*.{la,py}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install %{name}.schemas

%preun
%gconf_schema_uninstall %{name}.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_sysconfdir}/gconf/schemas/gimmie.schemas
%attr(755,root,root) %{_bindir}/gimmie
%{_libdir}/bonobo/servers/GNOME_GimmieApplet.server
%{_libdir}/gimmie_applet
%dir %{py_sitedir}/gimmie
%{py_sitedir}/gimmie/*.py[co]
%dir %{py_sitedir}/gimmie/gdmclient
%{py_sitedir}/gimmie/gdmclient/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/gdmclient/*.so
%dir %{py_sitedir}/gimmie/gmenu
%{py_sitedir}/gimmie/gmenu/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/gmenu/*.so
%dir %{py_sitedir}/gimmie/gnomecups
%{py_sitedir}/gimmie/gnomecups/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/gnomecups/*.so
%dir %{py_sitedir}/gimmie/iconentry
%{py_sitedir}/gimmie/iconentry/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/iconentry/*.so
%dir %{py_sitedir}/gimmie/sexy
%{py_sitedir}/gimmie/sexy/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/sexy/*.so
%dir %{py_sitedir}/gimmie/traymanager
%{py_sitedir}/gimmie/traymanager/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/traymanager/*.so
%{_datadir}/gnome-2.0/ui/*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_pixmapsdir}/*.png
