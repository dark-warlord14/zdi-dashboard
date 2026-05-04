# ZDI-20-1365: Microsoft Windows bindflt Driver Missing Authentication Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1365
- **ZDI-CAN:** ZDI-CAN-11361
- **Date:** 2020-11-11
- **CVE:** CVE-2020-17012
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** whoami
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1365/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the bindflt.sys driver. A crafted request with an IOCTL of 0x220000 can perform remapping of directories. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-us/security-guidance/advisory/CVE-2020-17012

## Disclosure Timeline

- 2020-08-05 - Vulnerability reported to vendor
- 2020-11-11 - Coordinated public release of advisory
