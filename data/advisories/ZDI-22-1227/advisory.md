# ZDI-22-1227: Adobe InDesign SVG File Parsing Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1227
- **ZDI-CAN:** ZDI-CAN-17615
- **Date:** 2022-09-14
- **CVE:** CVE-2022-38413
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Adobe
- **Affected Products:** InDesign
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1227/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Adobe InDesign. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of SVG files. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: https://helpx.adobe.com/security/products/indesign/apsb22-50.html

## Disclosure Timeline

- 2022-06-02 - Vulnerability reported to vendor
- 2022-09-14 - Coordinated public release of advisory
