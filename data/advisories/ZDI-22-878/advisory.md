# ZDI-22-878: Apple macOS PackageKit PKInstallService Directory Traversal System Integrity Protection Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-878
- **ZDI-CAN:** ZDI-CAN-16111
- **Date:** 2022-06-29
- **CVE:** CVE-2022-22676
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:N
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Mickey Jin (@patch1t) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-878/
## Vulnerability Details

This vulnerability allows local attackers to bypass System Integrity Protection on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within PackageKit. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and delete files normally protected from the user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213054

## Disclosure Timeline

- 2021-12-03 - Vulnerability reported to vendor
- 2022-06-29 - Coordinated public release of advisory
