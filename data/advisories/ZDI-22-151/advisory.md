# ZDI-22-151: Bentley MicroStation CONNECT JT File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-151
- **ZDI-CAN:** ZDI-CAN-15023
- **Date:** 2022-01-31
- **CVE:** CVE-2021-46564
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Bentley
- **Affected Products:** MicroStation CONNECT
- **Credit:** xina1i
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-151/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Bentley MicroStation CONNECT. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of JT files. Crafted data in a JT file can trigger a write past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Bentley has issued an update to correct this vulnerability. More details can be found at: https://www.bentley.com/en/common-vulnerability-exposure/BE-2021-0005

## Disclosure Timeline

- 2021-10-06 - Vulnerability reported to vendor
- 2022-01-31 - Coordinated public release of advisory
