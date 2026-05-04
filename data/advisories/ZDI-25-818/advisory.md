# ZDI-25-818: (0Day) Microsoft Windows OneDrive SmartScreen Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-818
- **ZDI-CAN:** ZDI-CAN-24078
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Girnus (@gothburz) - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-818/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the Mark-of-the-Web protection mechanism on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of OneDrive file syncing. When syncing files from the cloud to the local filesystem, OneDrive neither applies nor preserves the Mark-of-the-Web on files originating from untrusted locations. An attacker can leverage this vulnerability to bypass SmartScreen protection and execute arbitrary code in the context of the current user.

## Additional Details

06/06/24 – ZDI reported the vulnerability to the vendor 06/06/24 – the vendor acknowledged the receipt of the report 07/10/24 – the vendor rated the severity of the vulnerability to be Low and communicated that the issues did not meet the bar for immediate servicing 07/31/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-06-06 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
