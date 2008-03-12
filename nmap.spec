#
# TODO:
#	- use system lua51
#	- use system libdnet
#	- R: for zenmap
#	- desktop file for zenmap
#
Summary:	Network exploration tool and security scanner
Summary(es.UTF-8):	Herramienta de exploración de la rede y seguridad
Summary(pl.UTF-8):	Program do badania i audytu sieci
Summary(pt_BR.UTF-8):	Ferramenta de exploração da rede e segurança
Summary(ru.UTF-8):	Утилита сканирования сети и аудита безопасности
Summary(uk.UTF-8):	Утиліта сканування мережі та аудиту безпеки
Summary(zh_CN.UTF-8):	[系统]强力端口扫描器
Summary(zh_TW.UTF-8):	[.)B系.$)B統].)B強力.$)B端.)B口.$)B掃.)B描.$)B器
Name:		nmap
Version:	4.53
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.insecure.org/nmap/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	bb203c47f3c234b61d3c4916da7eaa27
Patch0:		%{name}-am18.patch
URL:		http://www.insecure.org/nmap/index.html
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_x:BuildRequires:	gtk+2-devel >= 2.0}
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
%{?with_x:BuildRequires:	pkgconfig}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nmap is a utility for network exploration or security auditing. It
supports ping scanning (determine which hosts are up), many port
scanning techniques (determine what services the hosts are offering),
and TCP/IP fingerprinting (remote host operating system
identification). Nmap also offers flexible target and port
specification, decoy scanning, determination of TCP sequence
predictability characteristics, sunRPC scanning, reverse-identd
scanning, and more.

nmap supports a large number of scanning techniques such as: UDP, TCP
connect(), TCP SYN (half open), FTP proxy (bounce attack),
Reverse-ident, ICMP (ping sweep), FIN, ACK sweep, Xmas Tree, SYN
sweep, and Null scan.

%description -l es.UTF-8
Nmap es un utilitario para la exploración y auditoría de redes.
Soporta "ping scanning", varias técnicas de búsqueda de puertos
abiertos, e identificación remota de sistemas operacionales vía
impresiones digitales TCP/IP.

%description -l pl.UTF-8
Nmap jest programem przeznaczonym do badania i audytu sieci. Wspiera
różne techniki skanowania (badanie jakie usługi są uruchomione na
danym hoście), a także TCP/IP fingerprinting (zdalne rozpoznawanie
typu systemu operacyjnego). Nmap oferuje różne techniki skanowania
wykorzystujące: UDP, TCP connect(), TCP SYN (half open), FTP proxy
(bounce attack), Reverse-ident, ICMP (ping sweep), FIN, ACK sweep,
Xmas Tree, SYN sweep i Null scan.

%description -l pt_BR.UTF-8
Nmap é um utilitário para a exploração e auditoria de redes. Ele
suporta "ping scanning", várias técnicas de procura por portas
abertas, e identificação remota de sistemas operacionais via
impressões digitais TCP/IP.

%description -l ru.UTF-8
Nmap - это утилита для изучения сети и аудита безопасности. Она
поддерживает ping-сканирование (определение, какие хосты работают),
много методик сканирования портов (определение, какие сервисы
предоставляют хосты), и "отпечатки пальцев" TCP/IP (идентификация
операционной системы хоста). Nmap также поддерживает гибкое задание
цели и порта, скрытое сканирование (decoy scanning), определение
характеристик предсказуемости TCP sequence, сканирование sunRPC,
reverse-identd сканирование и другое.

%description -l uk.UTF-8
Nmap - це утиліта для дослідження мережі та аудиту безпеки. Вона
підтримує ping-сканування (визначення, які хости працюють), багато
методик сканування портів (визначення, які сервіси надають хости), та
"відбитки пальців" TCP/IP (ідентифікація операційної системи хоста).
Nmap також підтримує гнучке задання цілі та порта, приховане
сканування (decoy scanning), визначення характеристик передбачуваності
TCP sequence, сканування sunRPC, reverse-identd сканування та інше.

%package zenmap
Summary:	Graphical frontend for nmap
Summary(pl.UTF-8):	Graficzny frontend dla nmapa
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}-%{release}
Obsoletes:	nmap-X11
Obsoletes:	nmap-frontend

%description zenmap
This package includes zenmap, a graphical frontend for nmap.

%description zenmap -l pl.UTF-8
Ten pakiet zawiera zenmap, czyli graficzny frontend dla nmapa.

%prep
%setup -q
%patch0 -p1

%build
find -type f -name 'configure.ac' | while read CFG; do
	cd $(dirname "$CFG")
	cp -f /usr/share/automake/config.sub .
	%{__aclocal}
	%{__autoconf}
	cd -
done

CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions" \
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install docs/zenmap.1 $RPM_BUILD_ROOT%{_mandir}/man1

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/README docs/*.txt CHANGELOG
%attr(755,root,root) %{_bindir}/nmap
%{_libdir}/nmap
%{_datadir}/nmap
%{_mandir}/man1/nmap.1*

%files zenmap
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmapfe
%attr(755,root,root) %{_bindir}/xnmap
%attr(755,root,root) %{_bindir}/zenmap
%dir %{py_sitescriptdir}/higwidgets
%dir %{py_sitescriptdir}/zenmapCore
%dir %{py_sitescriptdir}/zenmapGUI
%{py_sitescriptdir}/higwidgets/*.py[co]
%{py_sitescriptdir}/zenmapCore/*.py[co]
%{py_sitescriptdir}/zenmapGUI/*.py[co]
%{py_sitescriptdir}/zenmap-*-info
%dir %{_datadir}/zenmap
%dir %{_datadir}/zenmap/locale
%lang(pt_BR) %{_datadir}/zenmap/locale/pt_BR
%{_datadir}/zenmap/config
%{_datadir}/zenmap/docs
%{_datadir}/zenmap/misc
%{_mandir}/man1/zenmap.1*
%{_iconsdir}/*.ico
%{_pixmapsdir}/*.png
%{_pixmapsdir}/*.svg
