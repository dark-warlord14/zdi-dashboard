# ZDI-24-566: Luxion KeyShot Viewer KSP File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-566
- **ZDI-CAN:** ZDI-CAN-22449
- **Date:** 2024-06-05
- **CVE:** CVE-2024-30374
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Luxion
- **Affected Products:** KeyShot Viewer
- **Credit:** Simon Janz (@esj4y)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-566/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Luxion KeyShot Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of KSP files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

02/22/24 – ZDI reported the vulnerabilities to the vendor 02/29/24 – the vendor acknowledged the receipt of the reports 03/11/24 –The vendor communicated that the fix will be ready on 07/11/24 05/22/24 – ZDI notified the vendor of the intention to publish the cases as 0-day advisories -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-12-08 - Vulnerability reported to vendor
- 2024-06-05 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
