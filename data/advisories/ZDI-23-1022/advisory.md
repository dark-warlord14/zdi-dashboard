# ZDI-23-1022: Siemens Solid Edge Viewer IFC File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1022
- **ZDI-CAN:** ZDI-CAN-19429
- **Date:** 2023-08-04
- **CVE:** CVE-2023-0973
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Siemens
- **Affected Products:** Solid Edge Viewer
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Siemens Solid Edge Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of IFC files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Siemens has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-23-068-04

## Disclosure Timeline

- 2022-11-21 - Vulnerability reported to vendor
- 2023-08-04 - Coordinated public release of advisory
