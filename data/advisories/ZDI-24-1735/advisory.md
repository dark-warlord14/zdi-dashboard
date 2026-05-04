# ZDI-24-1735: (0Day) Ashlar-Vellum Graphite VC6 File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1735
- **ZDI-CAN:** ZDI-CAN-24977
- **Date:** 2024-12-30
- **CVE:** CVE-2024-13051
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Graphite
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1735/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Graphite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of VC6 files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

08/16/24 – ZDI reported the vulnerability to the vendor 08/16/24 – the vendor acknowledged the receipt of the report 09/11/24 - ZDI asked for updates 12/16/24 - ZDI notified the vendor of the intention to publish the case as a 0-day advisory Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-08-16 - Vulnerability reported to vendor
- 2024-12-30 - Coordinated public release of advisory
- 2024-12-30 - Advisory Updated
