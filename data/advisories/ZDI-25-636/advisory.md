# ZDI-25-636: (0Day) Ashlar-Vellum Cobalt AR File Parsing Uninitialized Variable Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-636
- **ZDI-CAN:** ZDI-CAN-25700
- **Date:** 2025-07-22
- **CVE:** CVE-2025-7984
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Rocco Calvi (@TecR0c) with TecSecurity
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-636/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of AR files. The issue results from the lack of proper initialization of memory prior to accessing it. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

11/21/24 – ZDI reported the vulnerability to the vendor 11/22/24 – the vendor acknowledged the receipt of the report 03/12/25 - ZDI asked for updates 03/20/25 – the vendor confirmed that resolving the issue was in progress 05/02/25 - ZDI asked for updates 07/15/25 – ZDI notified the vendor of the intention to publish the case as a 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the product

## Disclosure Timeline

- 2024-11-21 - Vulnerability reported to vendor
- 2025-07-22 - Coordinated public release of advisory
- 2025-07-22 - Advisory Updated
