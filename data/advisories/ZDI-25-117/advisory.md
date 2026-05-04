# ZDI-25-117: (0Day) Ashlar-Vellum Cobalt VC6 File Parsing Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-117
- **ZDI-CAN:** ZDI-CAN-25238
- **Date:** 2025-03-10
- **CVE:** CVE-2025-2016
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-117/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VC6 files. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

09/13/24 – ZDI reported the vulnerability to the vendor 09/13/24 – the vendor acknowledged the receipt of the report 01/13/25 - ZDI asked for updates 01/17/25 – ZDI notified the vendor of the intention to publish the case as 0-day advisory

## Disclosure Timeline

- 2024-09-13 - Vulnerability reported to vendor
- 2025-03-10 - Coordinated public release of advisory
- 2025-03-10 - Advisory Updated
