# ZDI-25-1055: (0Day) Microsoft Windows MP4 File Parsing Null Pointer Dereference Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-1055
- **ZDI-CAN:** ZDI-CAN-27835
- **Date:** 2025-12-10
- **CVE:** N/A
- **CVSS:** 4.3
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:L
- **Affected Vendors:** Microsoft
- **Affected Products:** Windows
- **Credit:** sumin
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-1055/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Microsoft Windows. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of MP4 files. The issue results from dereferencing a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

10/08/25 - ZDI reported the vulnerability to the vendor 10/08/25 – the vendor acknowledged the receipt of the report 10/20/25 – the vendor communicated that the reported behavior did not meet the bar for immediate servicing 11/26/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory on 12/10/25 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-10-08 - Vulnerability reported to vendor
- 2025-12-10 - Coordinated public release of advisory
- 2025-12-10 - Advisory Updated
