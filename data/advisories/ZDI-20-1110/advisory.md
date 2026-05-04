# ZDI-20-1110: (0Day) Fuji Electric Tellus Lite V-Simulator 6 V9 File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1110
- **ZDI-CAN:** ZDI-CAN-10696
- **Date:** 2020-09-08
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Fuji Electric
- **Affected Products:** Tellus Lite
- **Credit:** kimiya
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1110/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Fuji Electric Tellus Lite. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of V9 files by the V-Simulator 6 program. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 04/02/20 – ZDI reported the vulnerability to ICS-CERT 04/17/20 – ICS-CERT acknowledged the report 07/10/20 – ZDI requested an update 07/31/20 – ZDI requested an update 08/13/20 – ZDI notified ICS-CERT of the intention to publish the case as a 0-day advisory on 08/20/20 -- Mitigation: Given the nature of the vulnerability the only salient mitigation strategy is to restrict interaction with the application.

## Disclosure Timeline

- 2020-04-02 - Vulnerability reported to vendor
- 2020-09-08 - Coordinated public release of advisory
