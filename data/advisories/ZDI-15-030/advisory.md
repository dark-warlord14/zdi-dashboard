# ZDI-15-030: Microsoft Windows win32k.sys Dangling Pointer Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-030
- **ZDI-CAN:** ZDI-CAN-2626
- **Date:** 2015-02-10
- **CVE:** CVE-2015-0058
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** n3phos
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-030/
## Vulnerability Details

This vulnerability allows for elevation of privilege on vulnerable installations of Microsoft Windows. An attacker must have valid logon credentials and be able to log on locally to exploit this vulnerability. The specific flaw exists within the usage of Cursor objects. The issue lies in the failure to properly handle error conditions leading to a pointer not being reset. An attacker can leverage this vulnerability to raise privileges and execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/library/security/MS15-010

## Disclosure Timeline

- 2014-11-06 - Vulnerability reported to vendor
- 2015-02-10 - Coordinated public release of advisory
