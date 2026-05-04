# ZDI-25-810: (0Day) Microsoft Windows ZIP File Insufficient UI Warning Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-810
- **ZDI-CAN:** ZDI-CAN-23945
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 8.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Peter Girnus (@gothburz) and Simon Zuckerbraun - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-810/
## Vulnerability Details

This vulnerability allows remote attackers to bypass the SmartScreen security feature on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ZIP files. The user interface fails to warn the user of unsafe actions. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

04/17/24 – ZDI reported the vulnerability to the vendor 04/17/24 – the vendor acknowledged the receipt of the report 05/02/24 – the vendor communicated that the reported behaviour was by design 07/31/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-04-17 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
