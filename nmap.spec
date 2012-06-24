#
# Conditional build:
%bcond_without	x	# don't build gtk-based nmap-X11
#
Summary:	Network exploration tool and security scanner
Summary(es):	Herramienta de exploraci�n de la rede y seguridad
Summary(pl):	Program do badania i audytu sieci
Summary(pt_BR):	Ferramenta de explora��o da rede e seguran�a
Summary(ru):	������� ������������ ���� � ������ ������������
Summary(uk):	���̦�� ���������� ����֦ �� ������ �������
Summary(zh_CN):	[ϵͳ]ǿ���˿�ɨ����
Summary(zh_TW):	[.)B�t.$)B��].)B�j�O.$)B��.)B�f.$)B��.)B�y.$)B��
Name:		nmap
Version:	3.75
Release:	1
License:	GPL
Group:		Networking
Source0:	http://www.insecure.org/nmap/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	1b54c0608b36f6b3ac92d7d1b910738f
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-statistics.patch
Patch2:		%{name}-am18.patch
URL:		http://www.insecure.org/nmap/index.html
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_x:BuildRequires:	gtk+-devel >= 1.0}
BuildRequires:	libstdc++-devel
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
connect(), TCP SYN (half open), ftp proxy (bounce attack),
Reverse-ident, ICMP (ping sweep), FIN, ACK sweep, Xmas Tree, SYN
sweep, and Null scan.

%description -l es
Nmap es un utilitario para la exploraci�n y auditor�a de redes.
Soporta "ping scanning", varias t�cnicas de b�squeda de puertos
abiertos, e identificaci�n remota de sistemas operacionales v�a
impresiones digitales TCP/IP.

%description -l pl
Nmap jest programem przeznaczonym do badania i audytu sieci. Wspiera
r�ne techniki skanowania (badanie jakie us�ugi s� uruchomione na
danym ho�cie), a tak�e TCP/IP fingerprinting (zdalne rozpoznawanie
typu systemu operacyjnego). Nmap oferuje r�ne techniki skanowania
wykorzystuj�ce: UDP, TCP connect(), TCP SYN (half open), ftp proxy
(bounce attack), Reverse-ident, ICMP (ping sweep), FIN, ACK sweep,
Xmas Tree, SYN sweep i Null scan.

%description -l pt_BR
Nmap � um utilit�rio para a explora��o e auditoria de redes. Ele
suporta "ping scanning", v�rias t�cnicas de procura por portas
abertas, e identifica��o remota de sistemas operacionais via
impress�es digitais TCP/IP.

%description -l ru
Nmap - ��� ������� ��� �������� ���� � ������ ������������. ���
������������ ping-������������ (�����������, ����� ����� ��������),
����� ������� ������������ ������ (�����������, ����� �������
������������� �����), � "��������� �������" TCP/IP (�������������
������������ ������� �����). Nmap ����� ������������ ������ �������
���� � �����, ������� ������������ (decoy scanning), �����������
������������� ��������������� TCP sequence, ������������ sunRPC,
reverse-identd ������������ � ������.

%description -l uk
Nmap - �� ���̦�� ��� ���̦������ ����֦ �� ������ �������. ����
Ц�����դ ping-���������� (����������, �˦ ����� ��������), ������
������� ���������� ���Ԧ� (����������, �˦ ���צ�� ������� �����), ��
"צ������ ����æ�" TCP/IP (������Ʀ��æ� �����æ��ϧ ������� �����).
Nmap ����� Ц�����դ ������ ������� æ̦ �� �����, ���������
���������� (decoy scanning), ���������� ������������� ��������������Ԧ
TCP sequence, ���������� sunRPC, reverse-identd ���������� �� ����.

%package X11
Summary:	GTK+ frontend for nmap
Summary(pl):	Frontend GTK+ dla nmapa
Summary(pt_BR):	Frontend GTK+ para o nmap
Summary(ru):	GTK+ ��������� ��� nmap
Summary(uk):	GTK+ ��������� ��� nmap
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}
Obsoletes:	nmap-frontend

%description X11
This package includes nmapfe, a GTK+ frontend for nmap.

%description X11 -l pl
Ten pakiet zawiera nmapfe, czyli frontend dla nmapa pisany z u�yciem
GTK+.

%description X11 -l pt_BR
Frontend gr�fico para o nmap (nmapfe) escrito em GTK+. N�o cont�m toda
a funcionalidade do nmap em si, mas � �til para usu�rios iniciantes.

%description X11 -l ru
���� ����� �������� nmapfe, GTK+ ��������� ��� nmap.

%description X11 -l uk
��� ����� ͦ����� nmapfe, GTK+ ��������� ��� nmap.

%prep
%setup -q
%patch0 -p1
#patch1 -p1
%patch2 -p1

%build
cp /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
cd nbase
cp /usr/share/automake/config.sub .
# AC_C___ATTRIBUTE__
tail -n +302 aclocal.m4 >> acinclude.m4
%{__aclocal}
%{__autoconf}
cd ../libpcap-possiblymodified
cp /usr/share/automake/config.sub .
# don't run aclocal - only local macros here!
%{__autoconf}
cd ../nmapfe
cp /usr/share/automake/config.sub .
%{!?with_x:echo 'AC_DEFUN([AM_PATH_GTK],[AC_DEFINE(MISSING_GTK)])' >> acinclude.m4}
%{__aclocal}
%{__autoconf}
cd ../nsock/src
cp /usr/share/automake/config.sub .
cd ../..
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--enable-ipv6 \
	%{!?with_x:--without-nmapfe}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	deskdir=%{_desktopdir}

%if %{with x}
cd $RPM_BUILD_ROOT%{_bindir}
rm -f xnmap
ln -s nmapfe xnmap
cd -

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.txt CHANGELOG
%attr(755,root,root) %{_bindir}/nmap
%{_datadir}/nmap
%{_mandir}/man1/nmap.*

%if %{with x}
%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmapfe
%attr(755,root,root) %{_bindir}/xnmap
%{_mandir}/man1/nmapfe.*
%{_mandir}/man1/xnmap.*
%{_desktopdir}/nmapfe.desktop
%{_pixmapsdir}/nmap.png
%endif
