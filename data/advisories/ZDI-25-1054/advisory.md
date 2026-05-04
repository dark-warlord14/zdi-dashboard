# ZDI-25-1054: (0Day) Microsoft Windows dir Command Improper Character Neutralization Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1054
- **ZDI-CAN:** ZDI-CAN-26750
- **Date:** 2025-12-10
- **CVE:** N/A
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** St4nly0n
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1054/
## Vulnerability Details

This vulnerability allows remote attackers to display misleading terminal output on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of filenames in the built-in dir command. By including invalid characters in a filename, an attacker can cause the display of misleading text and terminal effects. An attacker can leverage this vulnerability to deceive the user into performing dangerous actions.

## Additional Details

04/04/25 - ZDI reported the vulnerability to the vendor 04/04/25 – the vendor acknowledged the receipt of the report 04/09/25 – the vendor asked for technical details 04/09/25 - ZDI provided more information 05/06/25 – the vendor communicated that the reported behavior was not a vulnerability 11/26/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/10/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-04-04 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
