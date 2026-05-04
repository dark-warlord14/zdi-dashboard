# ZDI-20-125: Microsoft Windows CLFS Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-125
- **ZDI-CAN:** ZDI-CAN-9382
- **Date:** 2020-01-15
- **CVE:** CVE-2020-0634
- **CVSS:** 8.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Meysam Firouzi of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-125/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the CLFS.SYS driver. Crafted data in a binary log file can cause a pointer to be reused after it has been freed. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-0634

## Disclosure Timeline

- 2019-10-08 - Vulnerability reported to vendor
- 2020-01-15 - Coordinated public release of advisory
