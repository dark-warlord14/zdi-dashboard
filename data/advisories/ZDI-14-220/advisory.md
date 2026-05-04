# ZDI-14-220: (Pwn2Own) Microsoft Windows AFD.SYS Dangling Pointer Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-220
- **ZDI-CAN:** ZDI-CAN-2228
- **Date:** 2014-07-09
- **CVE:** CVE-2014-1767
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Sebastian Apelt (sebastian.apelt@siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-220/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of sockets. The issue lies in the failure to properly handle error conditions leading to a pointer not being reset. An attacker can leverage this vulnerability to raise privileges and execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/library/security/MS14-040.aspx

## Disclosure Timeline

- 2014-03-11 - Vulnerability reported to vendor
- 2014-07-09 - Coordinated public release of advisory
