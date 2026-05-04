# ZDI-22-614: Bentley MicroStation CONNECT IFC File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-614
- **ZDI-CAN:** ZDI-CAN-16446
- **Date:** 2022-04-12
- **CVE:** CVE-2022-28302
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** MicroStation CONNECT
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-614/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley MicroStation CONNECT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of IFC files. Crafted data in an IFC file can trigger a read past the end of an allocated buffer. An attacker can leverage this to execute code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/en/common-vulnerability-exposure/be-2022-0006

## Disclosure Timeline

- 2022-02-09 - Vulnerability reported to vendor
- 2022-04-12 - Coordinated public release of advisory
