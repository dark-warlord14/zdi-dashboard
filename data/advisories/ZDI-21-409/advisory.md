# ZDI-21-409: Microsoft Windows Installer Service Untrusted File Path Arbitrary File Write Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-409
- **ZDI-CAN:** ZDI-CAN-12403
- **Date:** 2021-04-15
- **CVE:** CVE-2021-26415
- **CVSS:** 7.3
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Adrian Denkiewicz of CLOAKED.pl
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-409/
## Vulnerability Details

This vulnerability allows local attackers to write data to arbitrary files on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Windows Installer service. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of an administrator.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://msrc.microsoft.com/update-guide/vulnerability/CVE-2021-26415

## Disclosure Timeline

- 2020-12-16 - Vulnerability reported to vendor
- 2021-04-15 - Coordinated public release of advisory
