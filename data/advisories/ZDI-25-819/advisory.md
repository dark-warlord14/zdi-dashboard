# ZDI-25-819: (0Day) Microsoft Windows NetBIOS Hostname SmartScreen Bypass Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-819
- **ZDI-CAN:** ZDI-CAN-24425
- **Date:** 2025-08-06
- **CVE:** N/A
- **CVSS:** 7.1
- **CVSS Vector:** AV:A/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** Simon Zuckerbraun and Peter Girnus (@gothburz) - Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-819/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to bypass the SmartScreen security feature on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of NetBIOS hostnames. By advertising a NetBIOS name on a host, an attacker can bypass SmartScreen on files originating from that host when accessed via the NetBIOS name. An attacker can leverage this vulnerability to execute arbitrary code in the context of the current user.

## Additional Details

06/12/24 – ZDI reported the vulnerability to the vendor 06/12/24 – the vendor acknowledged the receipt of the report 07/11/24 – the vendor rated the severity of the vulnerability to be Low and communicated that the issues did not meet the bar for immediate servicing 07/31/25 – ZDI notified the vendor of the intention to publish the cases as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2024-06-12 - Vulnerability reported to vendor
- 2025-08-06 - Coordinated public release of advisory
- 2025-08-06 - Advisory Updated
