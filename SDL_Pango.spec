Summary:	Pango engine to SDL
Summary(pl.UTF-8):	Silnik Pango dla SDL
Name:		SDL_Pango
Version:	0.1.2
Release:	6
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/sdlpango/%{name}-%{version}.tar.gz
# Source0-md5:	85bbf9bb7b1cee0538154dadd045418c
Patch0:		%{name}-am.patch
Patch1:		%{name}-0.1.2-API-adds.patch
URL:		http://sdlpango.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pango engine to SDL.

%description -l pl.UTF-8
Silnik Pango dla SDL.

%package devel
Summary:	Header files and more to develop SDL_Pango applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL_Pango
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_Pango applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL_Pango.

%package static
Summary:	Static SDL_Pango libraries
Summary(pl.UTF-8):	Statyczne biblioteki SDL_Pango
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_Pango libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SDL_Pango.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p0

%build
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDL/*
%{_pkgconfigdir}/SDL_Pango.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
