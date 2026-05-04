# ZDI-24-1091: (0Day) Microsoft Windows DirectComposition Out-Of-Bounds Read Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1091
- **ZDI-CAN:** ZDI-CAN-20572
- **Date:** 2024-08-06
- **CVE:** N/A
- **CVSS:** 5.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Sergey Kornienko (@b1thvn_)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1091/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of Microsoft Windows. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the implementation of DirectComposition in the win32kbase driver. The issue results from the lack of proper validation of user-supplied data, which can result in a read before the start of an array. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

04/28/23 – ZDI reported the vulnerability to the vendor. 05/02/23 – The vendor acknowledged the report. 05/23/23 – The vendor states this case doesn’t meet the bar for immediate servicing. 05/23/23 – ZDI informed the vendor of our intention to publish this as a zero-day advisory. 02/05/24 – The vendor states this case might be fixed but would verify. 08/05/24 – The ZDI informed the vendor that we are publishing this case as a zero-day advisory on 08/06/24. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2023-05-01 - Vulnerability reported to vendor
- 2024-08-06 - Coordinated public release of advisory
- 2024-08-15 - Advisory Updated
