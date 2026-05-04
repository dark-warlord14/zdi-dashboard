# ZDI-17-470: (Pwn2Own) Microsoft Windows fnHKINLPRECT Untrusted Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-470
- **ZDI-CAN:** ZDI-CAN-4626
- **Date:** 2017-07-11
- **CVE:** CVE-2017-8467
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** GuoPengfei from 360 Codesafe Team
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-470/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the win32kfull.sys driver. The issue results from the lack of proper validation of a user-supplied value prior to dereferencing it as a pointer. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2017-8467

## Disclosure Timeline

- 2017-03-16 - Vulnerability reported to vendor
- 2017-07-11 - Coordinated public release of advisory
