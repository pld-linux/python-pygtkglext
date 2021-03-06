Summary:	Python bindings for GtkGLExt library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki GtkGLExt
Name:		python-pygtkglext
Version:	1.1.0
Release:	7
License:	LGPL
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/gtkglext/pygtkglext-%{version}.tar.bz2
# Source0-md5:	720b421d3b8514a40189b285dd91de57
URL:		http://gtkglext.sourceforge.net/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.7
BuildRequires:	gtkglext-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-devel >= 2:2.6.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	python-pygtk-gtk >= 2:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
PyGtkGLExt is Python language bindings for GtkGLExt, OpenGL Extension
to GTK.

%description -l pl.UTF-8
PyGtkGLExt to wiązania języka Python do GtkGLExt - rozszerzenia OpenGL
dla GTK.

%package devel
Summary:	Development files for Python bindings for GtkGLExt
Summary(pl.UTF-8):	Pliki programistyczne wiązań Pythona do GtkGLExt
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python-pygtk-devel >= 2:2.6.0

%description devel
Development files for Python bindings for GtkGLExt.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań Pythona do GtkGLExt.

%package examples
Summary:	Example programs for PyGtkGLExt
Summary(pl.UTF-8):	Przykładowe programy do PyGtkGLExt
Group:		Development/Languages/Python

%description examples
Example programs for PyGtkGLExt.

%description examples -l pl.UTF-8
Przykładowe programy do PyGtkGLExt.

%prep
%setup -q -n pygtkglext-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pythondir=%{py_sitedir}

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/gtk/gdkgl/_gdkgl.la
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gtk-2.0/gtk/gtkgl/_gtkgl.la

cp -p examples/*.{png,py} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{py_sitedir}/gtk-2.0/gtk/gdkgl
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/gdkgl/_gdkgl.so
%{py_sitedir}/gtk-2.0/gtk/gdkgl/__init__.py[co]
%{py_sitedir}/gtk-2.0/gtk/gdkgl/ext.py[co]
%dir %{py_sitedir}/gtk-2.0/gtk/gtkgl
%attr(755,root,root) %{py_sitedir}/gtk-2.0/gtk/gtkgl/_gtkgl.so
%{py_sitedir}/gtk-2.0/gtk/gtkgl/__init__.py[co]
%{py_sitedir}/gtk-2.0/gtk/gtkgl/apputils.py[co]
%{py_sitedir}/gtk-2.0/gtk/gtkgl/widget.py[co]

%files devel
%defattr(644,root,root,755)
%{_datadir}/pygtk/2.0/defs/gdkglext*.defs
%{_datadir}/pygtk/2.0/defs/gtkglext*.defs
%{_pkgconfigdir}/pygtkglext-1.0.pc

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
