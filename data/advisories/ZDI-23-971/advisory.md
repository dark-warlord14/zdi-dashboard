# ZDI-23-971: (Pwn2Own) Tesla Model 3 bcmdhd Out-Of-Bounds Write Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-971
- **ZDI-CAN:** ZDI-CAN-20733
- **Date:** 2023-07-18
- **CVE:** CVE-2023-32155
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Tesla
- **Affected Products:** Model 3
- **Credit:** David BERARD (@_p0ly_) and Vincent DEHORS (@vdehors) from Synacktiv (@Synacktiv)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-971/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected Tesla Model 3 vehicles. An attacker must first obtain the ability to execute code on the wifi subsystem in order to exploit this vulnerability. The specific flaw exists within the bcmdhd driver. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of the kernel.

## Additional Details

Fixed in 2023.12 firmware release.

## Disclosure Timeline

- 2023-03-30 - Vulnerability reported to vendor
- 2023-07-18 - Coordinated public release of advisory
