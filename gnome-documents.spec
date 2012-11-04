Summary:	Document manager for GNOME
Name:		gnome-documents
Version:	3.6.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-documents/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	46006058a93952e8e6f2ccab2b55a318
URL:		https://live.gnome.org/Design/Apps/Documents
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-gtk-devel
BuildRequires:	evince-devel
BuildRequires:	gettext-devel
BuildRequires:	gjs-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	gnome-online-accounts-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	libgdata-devel
BuildRequires:	liboauth-devel
BuildRequires:	libtool
BuildRequires:	libzapojit-devel
BuildRequires:	pkg-config
BuildRequires:	tracker-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	glib-gio-gsettings
Requires:	evince
Requires:	hicolor-icon-theme
Requires:	tracker
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/gnome-documents

%description
GNOME Documents is a document manager application for GNOME.


%package shell-search-provider
Summary:	GNOME Shell search provider
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gnome-shell

%description shell-search-provider
Search result provider for GNOME Shell.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4 -I libgd
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-documents/*.la

%find_lang gnome-documents

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_gsettings_cache

%postun
%update_icon_cache hicolor
%update_gsettings_cache

%files -f gnome-documents.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-documents
%attr(755,root,root) %{_libdir}/gnome-documents/gd-tracker-zpj-miner
%attr(755,root,root) %{_libdir}/gnome-documents/libgd.so
%attr(755,root,root) %{_libdir}/gnome-documents/libgdminer-1.0.so
%attr(755,root,root) %{_libdir}/gnome-documents/libgdprivate-1.0.so

%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gd-tracker-gdata-miner

%dir %{_libdir}/gnome-documents/girepository-1.0
%{_libdir}/gnome-documents/girepository-1.0/Gd-1.0.typelib
%{_libdir}/gnome-documents/girepository-1.0/GdPrivate-1.0.typelib

%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-documents

%{_desktopdir}/gnome-documents.desktop
%{_iconsdir}/hicolor/*/*/*.png

%files shell-search-provider
%defattr(644,root,root,755)
%{_datadir}/gnome-shell/search-providers/gnome-documents-search-provider.ini
%attr(755,root,root) %{_libexecdir}/gnome-documents-search-provider

