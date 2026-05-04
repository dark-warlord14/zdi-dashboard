# ZDI-23-1452: (0Day) Ashlar-Vellum Cobalt AR File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1452
- **ZDI-CAN:** ZDI-CAN-20660
- **Date:** 2023-09-21
- **CVE:** CVE-2023-42103
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1452/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of AR files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

03/22/23 – ZDI reported the vulnerability to the vendor. 03/22/23 – The vendor acknowledged the report. 08/25/23 – The ZDI asked for an update. 08/28/23 – The vendor states that the open cases have not been resolved. 09/20/23 – The ZDI informed the vendor that the case will be published as a zero-day advisory on 09/21/23. -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-03-22 - Vulnerability reported to vendor
- 2023-09-21 - Coordinated public release of advisory
- 2023-09-21 - Advisory Updated
