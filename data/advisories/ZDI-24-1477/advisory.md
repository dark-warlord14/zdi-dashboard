# ZDI-24-1477: (0Day) Trimble SketchUp Viewer SKP File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1477
- **ZDI-CAN:** ZDI-CAN-24104
- **Date:** 2024-11-12
- **CVE:** CVE-2024-9720
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Trimble
- **Affected Products:** SketchUp Viewer
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1477/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Trimble SketchUp Viewer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SKP files. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

05/01/24 – ZDI reported the vulnerability to the vendor 05/01/24 – the vendor acknowledged the receipt of the report 09/06/24 - ZDI asked for updates 09/23/24 - ZDI asked for updates 10/08/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application

## Disclosure Timeline

- 2024-05-01 - Vulnerability reported to vendor
- 2024-11-12 - Coordinated public release of advisory
- 2024-11-12 - Advisory Updated
