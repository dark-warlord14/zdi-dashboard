# ZDI-25-629: (0Day) Ashlar-Vellum Cobalt LI File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-629
- **ZDI-CAN:** ZDI-CAN-25354
- **Date:** 2025-07-22
- **CVE:** CVE-2025-7977
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-629/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of LI files. The issue results from the lack of proper validation of user-supplied data, which can result in a read before the start of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

10/11/24 – ZDI reported the vulnerability to the vendor 03/12/25 - ZDI asked for updates 03/20/25 – the vendor confirmed that resolving the issue was in progress 05/02/25 - ZDI asked for updates 07/15/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2024-10-11 - Vulnerability reported to vendor
- 2025-07-22 - Coordinated public release of advisory
- 2025-07-22 - Advisory Updated
