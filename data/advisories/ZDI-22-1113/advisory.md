# ZDI-22-1113: Adobe FrameMaker SVG File Parsing Out-Of-Bounds Read Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1113
- **ZDI-CAN:** ZDI-CAN-17623
- **Date:** 2022-08-18
- **CVE:** CVE-2022-35674
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** FrameMaker
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1113/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe FrameMaker. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SVG files. Crafted data in an SVG file can trigger a read past the end of an allocated buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/framemaker/apsb22-42.html

## Disclosure Timeline

- 2022-06-03 - Vulnerability reported to vendor
- 2022-08-18 - Coordinated public release of advisory
