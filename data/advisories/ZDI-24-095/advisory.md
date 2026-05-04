# ZDI-24-095: Canon imageCLASS MF753Cdw Fax Job Heap-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-095
- **ZDI-CAN:** ZDI-CAN-22658
- **Date:** 2024-02-06
- **CVE:** CVE-2024-0244
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Canon
- **Affected Products:** imageCLASS MF753Cdw
- **Credit:** Connor Ford (@ByteInsight) of Nettitude
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-095/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Canon imageCLASS MF753Cdw printers. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of fax jobs. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the device.

## Additional Details

Canon has issued an update to correct this vulnerability. More details can be found at: https://www.canon-europe.com/support/product-security-latest-news/

## Disclosure Timeline

- 2023-12-11 - Vulnerability reported to vendor
- 2024-02-06 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
