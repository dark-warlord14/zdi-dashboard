# ZDI-25-174: (0Day) Luxion KeyShot DAE File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-174
- **ZDI-CAN:** ZDI-CAN-23704
- **Date:** 2025-03-20
- **CVE:** CVE-2025-2531
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Luxion
- **Affected Products:** KeyShot
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-174/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Luxion KeyShot. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of dae files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

09/11/24 – ZDI reported the vulnerability to the vendor 09/25/24 – the vendor acknowledged the receipt of the report 09/30/24 – the vendor communicated that the fix would be released by November 2024 12/19/24 - ZDI asked for updates 01/06/25 – the vendor requested an extension until March 2025 02/11/25 - ZDI asked for updates 02/19/25 – the vendor requested an extension until June 2025 02/19/25 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory

## Disclosure Timeline

- 2024-09-11 - Vulnerability reported to vendor
- 2025-03-20 - Coordinated public release of advisory
- 2025-03-20 - Advisory Updated
