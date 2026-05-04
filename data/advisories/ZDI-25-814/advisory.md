# ZDI-25-814: (0Day) Microsoft Windows MonikerLink Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-814
- **ZDI-CAN:** ZDI-CAN-23548
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Girnus (@gothburz) and Ian Kenefick (@ian_kenefick) of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-814/
## Vulnerability Details

This vulnerability allows remote attackers to relay NTLM credentials on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of redirections. An attacker can leverage this vulnerability to relay NTLM credentials in the context of the current user.

## Additional Details

02/27/24 – ZDI reported the vulnerability to the vendor 02/27/24 – the vendor acknowledged the receipt of the report 03/04/24 – the vendor confirmed the reported behaviour 03/04/24 – the vendor communicated that the issue was duplicate and was affecting a third-party vendor 07/31/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-02-27 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
