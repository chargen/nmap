#
# Conditional build:
%bcond_without x		# don't build gtk-based nmap-X11
#
Summary:	Network exploration tool and security scanner
Summary(es):	Herramienta de exploraci�n de la rede y seguridad
Summary(pl):	Programem do badania i audytu sieci
Summary(pt_BR):	Ferramenta de explora��o da rede e seguran�a
Summary(ru):	������� ������������ ���� � ������ ������������
Summary(uk):	���̦�� ���������� ����֦ �� ������ �������
Summary(zh_CN):	[ϵͳ]ǿ���˿�ɨ����
Summary(zh_TW):	[.)B�t.$)B��].)B�j�O.$)B��.)B�f.$)B��.)B�y.$)B��
Name:		nmap
Version:	3.48
Release:	2
License:	GPL
Group:		Networking
Source0:	http://www.insecure.org/nmap/dist/%{name}-%{version}.tar.bz2
# Source0-md5:	8c38559a863efd476c5b042123f1ee3a
Source1:	%{name}.png
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-statistics.patch
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
Xmas Tree, SYN sweep, and Null scan.

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
Summary:	Gtk+ frontend for nmap
Summary(pl):	Frontend Gtk+ dla nmapa
Summary(pt_BR):	Frontend gtk+ para o nmap
Summary(ru):	Gtk+ ��������� ��� nmap
Summary(uk):	Gtk+ ��������� ��� nmap
Group:		X11/Applications/Networking
Requires:	%{name} = %{version}
Obsoletes:	nmap-frontend

%description X11
This package includes nmapfe, a Gtk+ frontend for nmap.

%description X11 -l pl
Ten pakiet zawiera nmapfe, czyli frontend dla nmapa pisany z u�yciem
Gtk+.

%description X11 -l pt_BR
Frontend gr�fico para o nmap (nmapfe) escrito em gtk+. N�o cont�m toda
a funcionalidade do nmap em si, mas � �til para usu�rios iniciantes.

%description X11 -l ru
���� ����� �������� nmapfe, Gtk+ ��������� ��� nmap.

%description X11 -l uk
��� ����� ͦ����� nmapfe, Gtk+ ��������� ��� nmap.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal}
%{__autoconf}
cd nbase
%{__aclocal}
%{__autoconf}
cd ../libpcap-possiblymodified
%{__aclocal}
%{__autoconf}
cd ../nmapfe
%{!?with_x:echo 'AC_DEFUN([AM_PATH_GTK],[AC_DEFINE(MISSING_GTK)])' >> acinclude.m4}
%{__aclocal}
%{__autoconf}
cd ..
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	%{!?with_x:--without-nmapfe}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	deskdir=%{_desktopdir}

%if %{?with_x}
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

%if %{?with_x}
%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nmapfe
%attr(755,root,root) %{_bindir}/xnmap
%{_mandir}/man1/nmapfe.*
%{_mandir}/man1/xnmap.*
%{_desktopdir}/nmapfe.desktop
%{_pixmapsdir}/nmap.png
%endif
