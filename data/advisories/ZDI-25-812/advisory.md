# ZDI-25-812: (0Day) Microsoft Windows SmartScreen Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-812
- **ZDI-CAN:** ZDI-CAN-23938
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Girnus (@gothburz) and Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-812/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the SmartScreen security feature on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the verification of signatures on executables. The issue results from the lack of a proper security warning message. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

04/12/24 – ZDI reported the vulnerability to the vendor 04/12/24 – the vendor acknowledged the receipt of the report 05/01/24 – the vendor rated the severity of the vulnerability to be Moderate and communicated that the issues did not meet the bar for immediate servicing 07/31/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-04-12 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
