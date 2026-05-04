# ZDI-25-121: (0Day) Ashlar-Vellum Cobalt CO File Parsing Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-121
- **ZDI-CAN:** ZDI-CAN-25240
- **Date:** 2025-03-10
- **CVE:** CVE-2025-2017
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-121/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of CO files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

09/26/24 – ZDI reported the vulnerability to the vendor 09/26/24 – the vendor acknowledged the receipt of the report 01/13/25 - ZDI asked for updates 01/17/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory

## Disclosure Timeline

- 2024-09-26 - Vulnerability reported to vendor
- 2025-03-10 - Coordinated public release of advisory
- 2025-03-10 - Advisory Updated
