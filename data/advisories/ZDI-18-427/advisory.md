# ZDI-18-427: Microsoft Windows win32k Menu Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-427
- **ZDI-CAN:** ZDI-CAN-5616
- **Date:** 2018-05-14
- **CVE:** CVE-2018-8124
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** nyaacate of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-427/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of menus in the win32k driver. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to escalate privileges to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8124

## Disclosure Timeline

- 2018-01-30 - Vulnerability reported to vendor
- 2018-05-14 - Coordinated public release of advisory
- 2018-05-14 - Advisory Updated
