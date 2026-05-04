# ZDI-18-1357: Microsoft Windows NtGdiExtTextOutW Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1357
- **ZDI-CAN:** ZDI-CAN-6991
- **Date:** 2018-11-21
- **CVE:** CVE-2018-8553
- **CVSS:** 8.4
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** GDPR
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1357/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the kernel-mode routines that output text to a device context. The issue results from the lack of proper validation of user-supplied data, which can result in a memory access past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privilege to the level of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8553

## Disclosure Timeline

- 2018-09-19 - Vulnerability reported to vendor
- 2018-11-21 - Coordinated public release of advisory
- 2023-06-22 - Advisory Updated
