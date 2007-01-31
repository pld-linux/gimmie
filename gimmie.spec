#
Summary:	Desktop Dock and helper for GNOME
Name:		gimmie
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.beatniksoftware.com/gimmie/releases/%{name}-%{version}.tar.gz
# Source0-md5:	102684f0aa1e45aa6cb3f5259a83f66a
URL:		http://www.beatniksoftware.com/gimmie/
Patch0:	gimmie-0.2.1-bookmarks.patch
Patch1:	gimmie-tooltip-crash.patch
BuildRequires:	gnome-menus-editor
BuildRequires:	gnome-vfs2-devel
BuildRequires:	libgnomeprintui-devel >= 1.0
BuildRequires:	python-gnome-desktop-devel
Requires: python-Numeric
Requires:	python-gnome-desktop-libwnck
Requires:	python-gnome-extras-egg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gimmie is an elegant way to think about how you use your desktop
computer.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{a,la,py}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/*.{a,la,py}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*/*/*.{a,la,py}

%find_lang %{name} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gimmie
%{_prefix}/lib/bonobo/servers/GNOME_GimmieApplet.server
%{_prefix}/lib/gimmie_applet
%dir %{py_sitedir}/gimmie/
%{py_sitedir}/gimmie/*.py[co]
%dir %{py_sitedir}/gimmie/gdmclient/
%{py_sitedir}/gimmie/gdmclient/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/gdmclient/*.so
%dir %{py_sitedir}/gimmie/gnomecups/
%{py_sitedir}/gimmie/gnomecups/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/gnomecups/*.so
%dir %{py_sitedir}/gimmie/iconentry/
%{py_sitedir}/gimmie/iconentry/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/iconentry/*.so
%dir %{py_sitedir}/gimmie/sexy/
%{py_sitedir}/gimmie/sexy/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/sexy/*.so
%dir %{py_sitedir}/gimmie/traymanager/
%{py_sitedir}/gimmie/traymanager/*.py[co]
%attr(755,root,root) %{py_sitedir}/gimmie/traymanager/*.so
