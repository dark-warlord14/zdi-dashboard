# ZDI-25-956: (0Day) Ashlar-Vellum Cobalt CO File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-956
- **ZDI-CAN:** ZDI-CAN-26631
- **Date:** 2025-10-16
- **CVE:** CVE-2025-11465
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-956/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CO files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

04/14/25 – ZDI reported the vulnerability to the vendor 04/23/25 – the vendor acknowledged the receipt of the report 07/30/25 – ZDI asked for updates 08/06/25 - ZDI asked for updates 09/24/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product.

## Disclosure Timeline

- 2025-04-14 - Vulnerability reported to vendor
- 2025-10-16 - Coordinated public release of advisory
- 2025-10-16 - Advisory Updated
