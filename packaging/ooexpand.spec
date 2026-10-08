Name:           ooexpand
Version:        0.2.0
Release:        1%{?dist}
Summary:        Sovereign POSIX tab expander, whitespace visualizer, and indentation auditor
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/ooexpand
Source0:        ooexpand-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooexpand is a sovereign POSIX tab-to-spaces expander written in 100% pure
native openOODA (.oo). Features include standard and explicit tab-stop lists,
initial indentation conversion (-i), tab visualization, whitespace hygiene
auditing, and streaming Model Context Protocol (MCP).

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooexpand
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooexpand-uninstall

%files
/usr/bin/ooexpand
/usr/bin/ooexpand-uninstall

%changelog
* Thu Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevation to v0.2.0 in pure native openOODA with whitespace auditing and streaming MCP
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
