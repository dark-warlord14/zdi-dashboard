# ZDI-22-592: Bentley MicroStation CONNECT JP2 File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-592
- **ZDI-CAN:** ZDI-CAN-16202
- **Date:** 2022-04-12
- **CVE:** CVE-2022-28300
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** MicroStation
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-592/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley MicroStation CONNECT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JP2 images. Crafted data in a JP2 file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/en/common-vulnerability-exposure/be-2022-0007

## Disclosure Timeline

- 2022-01-14 - Vulnerability reported to vendor
- 2022-04-12 - Coordinated public release of advisory
