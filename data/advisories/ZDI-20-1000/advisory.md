# ZDI-20-1000: Microsoft Office OfficeClickToRun Time-Of-Check Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1000
- **ZDI-CAN:** ZDI-CAN-10974
- **Date:** 2020-08-13
- **CVE:** CVE-2020-1581
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Office
- **Credit:** hackyzh and lm0963 of DBAppSecurity Zion Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1000/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Microsoft Office. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the OfficeClickToRun executable. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2020-1581

## Disclosure Timeline

- 2020-05-07 - Vulnerability reported to vendor
- 2020-08-13 - Coordinated public release of advisory
