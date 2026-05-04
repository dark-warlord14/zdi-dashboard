# ZDI-25-854: (0Day) Oxford Instruments Imaris Viewer IMS File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-854
- **ZDI-CAN:** ZDI-CAN-21655
- **Date:** 2025-08-20
- **CVE:** CVE-2025-9275
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oxford Instruments
- **Affected Products:** Imaris Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-854/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oxford Instruments Imaris Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of IMS files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

07/14/25 - ZDI reported the vulnerability to the vendor’s security team 07/30/25 - ZDI asked for updates 08/12/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-07-14 - Vulnerability reported to vendor
- 2025-08-20 - Coordinated public release of advisory
- 2025-08-20 - Advisory Updated
