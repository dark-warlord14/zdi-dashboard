# ZDI-19-924: (0Day) Microsoft Windows cdrom Driver Memory Corruption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-924
- **ZDI-CAN:** ZDI-CAN-9381
- **Date:** 2019-10-30
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Meysam Firouzi of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-924/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the cdrom.sys driver. A crafted request with an IOCTL of 0x56C008 or 0x56C064 can trigger a memory corruption condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with ZDI policies. 10/03/19 - ZDI reported the vulnerability to the vendor 10/03/19 - The vendor acknowledged reception of the case 10/14/19 - The vendor communicated that the case does not meet the bar for servicing 10/21/19 - ZDI communicated to the vendor the intention to 0-day the case on 10/30/19 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application to trusted files.

## Disclosure Timeline

- 2019-10-03 - Vulnerability reported to vendor
- 2019-10-30 - Coordinated public release of advisory
