%define name	plasma-applet-message-indicator
%define	srcname	plasma-widget-message-indicator
%define version	0.5.2
%define release	%mkrel 1
%define Summary	 Plasmoid for displaying messages from message-indicator enabled applications


Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://launchpad.net/%{srcname}/trunk/%{version}/+download/%{srcname}-%{version}.tar.bz2
License:	GPLv3
Group:		Graphical desktop/KDE
URL:		https://launchpad.net/plasma-widget-message-indicator
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	libindicate-qt-devel
BuildRequires:	libdbusmenu-qt-devel
Provides:	plasma-applet
Provides:	%srcname = %version

%description

A Plasma widget which displays messages from message-indicator enabled
applications.


%files 
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_message_indicator.so
%_kde_services/plasma-applet-message-indicator.desktop




#---------------------------------------------------------------------

%prep
%setup -q -n %srcname-%{version}

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build



%clean
%__rm -rf %buildroot
