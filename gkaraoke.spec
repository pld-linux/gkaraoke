Summary:	GNOME Karaoke simulator
Summary(pl):	Symulator Karaoke dla GNOME
Name:		gkaraoke
Version:	0.2
Release:	1
License:	GPL
Group:		Applications/Multimedia
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	f582394e133cb4bcccea291b6fcf73ae
URL:		http://gkaraoke.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libunicode-devel
Requires:	TiMidity++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Karaoke simulator for the GNOME environment.

%description -l pl
Symulator karaoke dla GNOME

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} \
        CC="%{__cc}" \
        CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

cp po/Makefile po/Makefile.orig
sed  's/^\(mkinstalldirs = .*\)$/mkinstalldirs = $\(MKINSTALLDIRS\)/' po/Makefile.orig >po/Makefile
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/share/gnome/apps/Applications/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/gkaraoke/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}/%{name}_icon.png
