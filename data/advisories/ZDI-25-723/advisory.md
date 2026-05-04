# ZDI-25-723: (0Day) Ashlar-Vellum Cobalt XE File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-723
- **ZDI-CAN:** ZDI-CAN-26236
- **Date:** 2025-07-30
- **CVE:** CVE-2025-8004
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-723/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XE files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated data structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

02/11/25 – ZDI reported the vulnerability to the vendor 03/13/25 – the vendor acknowledged the receipt of the report 05/02/25 - ZDI asked for updates 06/19/25 - ZDI asked for updates 07/15/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2025-02-11 - Vulnerability reported to vendor
- 2025-07-30 - Coordinated public release of advisory
- 2025-07-30 - Advisory Updated
