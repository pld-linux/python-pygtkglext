Summary:	Python bindings for GtkGLExt library
Summary(pl):	Wi±zania Pythona do biblioteki GtkGLExt
Name:		python-pygtkglext
Version:	1.0.1
Release:	2
License:	LGPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/gtkglext/pygtkglext-%{version}.tar.bz2
# Source0-md5:	b34d61b427e5ade8791b6e4441e85793
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	automake
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-devel >= 2.0.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-pygtk-gtk >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
PyGtkGLExt is Python language bindings for GtkGLExt, OpenGL Extension
to GTK.

%description -l pl
PyGtkGLExt to wi±zania jêzyka Python do GtkGLExt - rozszerzenia OpenGL
dla GTK.

%package devel
Summary:	Development files for Python bindings for GtkGLExt
Summary(pl):	Pliki programistyczne wi±zañ Pythona do GtkGLExt
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
Requires:	python-pygtk-devel >= 2.0.0

%description devel
Development files for Python bindings for GtkGLExt.

%description devel -l pl
Pliki programistyczne wi±zañ Pythona do GtkGLExt.

%prep
%setup -q -n pygtkglext-%{version}

%build
cp -f /usr/share/automake/config.* .
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/gtk/g[dt]kgl/*.{la,py}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{py_sitedir}/gtk-2.0/gtk/g[dt]kgl
%{py_sitedir}/gtk-2.0/gtk/g[dt]kgl/*.py[co]
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/g[dt]kgl/*.so

%files devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/*.defs
%{_pkgconfigdir}/*.pc
