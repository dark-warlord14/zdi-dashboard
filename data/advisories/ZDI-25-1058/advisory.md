# ZDI-25-1058: (0Day) Microsoft Windows TAR File UI Misrepresentation Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1058
- **ZDI-CAN:** ZDI-CAN-27311
- **Date:** 2025-12-10
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Len Sadowski and Oguz Bektas
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1058/
## Vulnerability Details

This vulnerability allows remote attackers to disguise hard links on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the rendering of the contents of TAR files. Windows displays hard links within TAR files without providing any visual indication to differentiate them from normal files. An attacker can leverage this vulnerability to deceive a user regarding the trustworthiness of a file.

## Additional Details

07/25/25 - ZDI reported the vulnerability to the vendor 07/25/25 – the vendor acknowledged the receipt of the report 07/28/25 – the vendor asked for technical details 07/28/25 - ZDI provided more information 09/16/25 – the vendor communicated that the reported behavior did not meet the bar for immediate servicing 11/26/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/10/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-07-25 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
