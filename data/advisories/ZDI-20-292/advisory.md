# ZDI-20-292: Parallels Desktop VGA Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-292
- **ZDI-CAN:** ZDI-CAN-9403
- **Date:** 2020-03-13
- **CVE:** CVE-2020-8871
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Parallels
- **Affected Products:** Desktop
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-292/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Parallels Desktop . An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the VGA virtual device. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Fixed in version 15.1.3 (47255)

## Disclosure Timeline

- 2019-11-14 - Vulnerability reported to vendor
- 2020-03-13 - Coordinated public release of advisory
- 2021-03-02 - Advisory Updated
