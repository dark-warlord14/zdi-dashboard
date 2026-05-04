# ZDI-25-824: (0Day) Microsoft Windows Theme File Parsing Improper Input Validation NTLM Relay Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-824
- **ZDI-CAN:** ZDI-CAN-26364
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Alex Williams of Trend Micro Security Research
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-824/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of theme files. The issue results from the lack of proper input validation. An attacker can leverage this vulnerability to relay NTLM credentials in the context of the current user.

## Additional Details

01/30/25 – ZDI reported the vulnerability to the vendor 01/30/25 – the vendor acknowledged the receipt of the report 02/24/25 – the vendor communicated that the issues did not meet the bar for immediate servicing 07/31/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-01-30 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
