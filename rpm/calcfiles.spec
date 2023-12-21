Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to calculate files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/romanchuk-artem-developer/laba_os_romanchuk_artem
Source0:        main.zip

BuildArch:      noarch

%description
calc_files.sh is a simple script that calculates the number of files in a directory.

%prep
%setup -q -n laba_os_romanchuk_artem-main

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 calc_files.sh %{buildroot}/usr/bin/calc_files

%files
/usr/bin/calc_files

%changelog
* Thu Dec 21 2023 Artem Romanchuk <romanchukartem04@gmail.com> - 1.0-1
- Initial build
