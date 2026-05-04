# ZDI-24-249: (0Day) Ashlar-Vellum Cobalt IGS File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-249
- **ZDI-CAN:** ZDI-CAN-21918
- **Date:** 2024-03-05
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Ashlar-Vellum
- **Affected Products:** Cobalt
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-249/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Ashlar-Vellum Cobalt. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of IGS files. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

09/05/23 – ZDI reported the vulnerability to the vendor 09/05/23 – The vendor acknowledged the receipt of the report 11/16/23 – ZDI asked for updates 11/16/23 –The vendor communicated that the case was not fixed 12/05/23 – ZDI asked for updates 12/06/23 –The vendor communicated that the case was not fixed 02/28/24 – ZDI notified the vendor of the intention to publish the case as 0-day advisory on 03/04/24 -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2023-09-05 - Vulnerability reported to vendor
- 2024-03-05 - Coordinated public release of advisory
- 2024-07-01 - Advisory Updated
