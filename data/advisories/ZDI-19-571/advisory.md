# ZDI-19-571: Microsoft Windows DirectComposition PropertySet Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-571
- **ZDI-CAN:** ZDI-CAN-8371
- **Date:** 2019-06-14
- **CVE:** CVE-2019-1065
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** fluoroacetate (@fluoroacetate)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-571/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of DirectComposition PropertySet objects in the kernel. The issue results from a failure to guard critical data from being modified while the kernel is performing an operation, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the kernel.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2019-1065

## Disclosure Timeline

- 2019-06-13 - Vulnerability reported to vendor
- 2019-06-14 - Coordinated public release of advisory
