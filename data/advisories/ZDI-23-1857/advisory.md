# ZDI-23-1857: (0Day) Hancom Office Show PPT File Parsing Stack-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1857
- **ZDI-CAN:** ZDI-CAN-20387
- **Date:** 2023-12-20
- **CVE:** CVE-2023-50235
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Hancom
- **Affected Products:** Office
- **Credit:** logos
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1857/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Hancom Office Show. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of PPT files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a stack-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

05/26/23 – ZDI made multiple attempts to contact the vendor across sales and support channels, which yielded no response from the vendor. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2023-11-17 - Vulnerability reported to vendor
- 2023-12-20 - Coordinated public release of advisory
