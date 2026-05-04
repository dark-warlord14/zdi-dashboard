# ZDI-13-171: Microsoft Windows win32k.sys Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-171
- **ZDI-CAN:** ZDI-CAN-1873
- **Date:** 2013-07-26
- **CVE:** CVE-2013-1345
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows 7
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-171/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must run a malicious executable. The specific flaw exists within the handling of Dynamic Data Exchange objects. The issue lies in the destruction of DDE objects within a thread. An attacker can leverage this to escalate their privileges and execute code under the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://technet.microsoft.com/en-us/security/bulletin/ms13-053

## Disclosure Timeline

- 2013-05-13 - Vulnerability reported to vendor
- 2013-07-26 - Coordinated public release of advisory
