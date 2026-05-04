# ZDI-20-259: Microsoft Windows NtUserResolveDesktopForWOW Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-259
- **ZDI-CAN:** ZDI-CAN-10076
- **Date:** 2020-02-20
- **CVE:** CVE-2020-0792
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** anch0vy@theori, kkokkokye@theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-259/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the function NtUserResolveDesktopForWOW. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0792

## Disclosure Timeline

- 2020-01-14 - Vulnerability reported to vendor
- 2020-02-20 - Coordinated public release of advisory
