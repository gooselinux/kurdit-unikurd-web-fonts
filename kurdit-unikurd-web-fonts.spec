%global fontname kurdit-unikurd-web
%global archivename unikurdweb

%global fontconf 65-%{fontname}.conf

Name:    %{fontname}-fonts
Version: 20020502
Release: 6%{?dist}
Summary: A widely used Kurdish font for Arabic-like scripts and Latin

Group:     User Interface/X
License:   GPLv3
URL:       http://www.kurditgroup.org/node/1337
Source0:   http://www.kurditgroup.org/download/1337/%{archivename}.zip
Source1:   65-kurdit-unikurd-web.conf
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires:      fontpackages-filesystem
Obsoletes:     unikurd-web-font < 20020502-2

%description
A widely used Kurdish font which supports various Arabic-like scripts
(Arabic, Kurdish, Persian) and also Latin.

%prep
%setup -q -c %{archivename}

%build

%install
rm -rf %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

%clean
rm -rf %{buildroot}

%_font_pkg -f 65-kurdit-unikurd-web.conf *.ttf
%doc gpl.txt


%changelog
* Thu May 20 2010 Parag <pnemade AT redhat.com> - 20020502-6
- Resolves: rh#586885  - No fontconfig config files provided

* Tue Feb 16 2010 Parag <pnemade AT redhat.com> - 20020502-5
- Resolves:-rh#565783 - please correct rpmlint problems for kurdit-unikurd-web-fonts

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20020502-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20020502-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Michal Nowak <mnowak@redhat.com> - 20020502-2
- repackage to save myself a grief

* Sun Jan 25 2009 Michal Nowak <mnowak@redhat.com> - 20020502-1
- renamed from unikurd-web-font -> kurdit-unikurd-web-fonts
- enhanced %%description field
- changes for F11 fonts rules
- add Obsoletes: unikurd-web-font <= 20020502-1

* Tue Oct 14 2008 Michal Nowak <mnowak@redhat.com> - 20020502
- version is now based on date of last issue of the font
- %%defattr(-,root,root,-) -> %%defattr(644,root,root,755)

* Mon Oct 13 2008 Michal Nowak <mnowak@redhat.com> - 1.00-2
- got rid of -web sub-package
- changed name from unikurd-fonts-web to unikurd-web-font
- minor structural changes in SPEC file

* Tue Jul 30 2008 Michal Nowak <mnowak@redhat.com> - 1.00-1
- initial packaging
- this package should be prepared for another unikurd fonts
  in sub-packages because on the KurdIT group/unikurd web there
  are plenthora of them, but probably not under suitable licenses

