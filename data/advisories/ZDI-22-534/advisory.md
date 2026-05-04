# ZDI-22-534: (Pwn2Own) HP LaserJet Pro MFP M283fdw ScanJobs Memory Corruption Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-534
- **ZDI-CAN:** ZDI-CAN-15897
- **Date:** 2022-03-23
- **CVE:** CVE-2022-24291
- **CVSS:** 6.5
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** HP
- **Affected Products:** LaserJet Pro MFP M283fdw
- **Credit:** Alexander Bolshev (@dark_k3y), Timo Hirvonen (@TimoHirvonen), and Dmitry Janushkevich (@InfoSecDJ)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-534/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of HP LaserJet Pro MFP M283fdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ScanJobs API. Crafted data in a request can cause a memory corruption condition. An attacker can leverage this vulnerability to create a denial-of-service condition on the system. An attacker can also leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of root.

## Additional Details

https://support.hp.com/us-en/document/ish_5950417-5950443-16/hpsbpi03781

## Disclosure Timeline

- 2022-01-21 - Vulnerability reported to vendor
- 2022-03-23 - Coordinated public release of advisory
