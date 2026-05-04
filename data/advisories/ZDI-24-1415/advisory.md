# ZDI-24-1415: Schneider Electric Zelio Soft 2 ZM2 File Parsing Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1415
- **ZDI-CAN:** ZDI-CAN-22347
- **Date:** 2024-10-17
- **CVE:** CVE-2024-8422
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Schneider Electric
- **Affected Products:** Zelio Soft 2
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1415/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Schneider Electric Zelio Soft 2. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of ZM2 files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Schneider Electric has issued an update to correct this vulnerability. More details can be found at: https://www.cisa.gov/news-events/ics-advisories/icsa-24-284-14

## Disclosure Timeline

- 2024-03-27 - Vulnerability reported to vendor
- 2024-10-17 - Coordinated public release of advisory
- 2024-10-17 - Advisory Updated
