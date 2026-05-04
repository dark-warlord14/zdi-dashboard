# ZDI-19-913: Foxit PhantomPDF Dwg2Pdf DWG File Parsing Use-After-Free Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-913
- **ZDI-CAN:** ZDI-CAN-9273
- **Date:** 2019-10-22
- **CVE:** CVE-2019-17143
- **CVSS:** 3.3
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:N/A:N
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-913/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of DWG files. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the current process.

## Additional Details

The plugin Dwg2Pdf is End of Life and will not be included in Foxit Reader version 9.7 and higher.

## Disclosure Timeline

- 2019-08-09 - Vulnerability reported to vendor
- 2019-10-22 - Coordinated public release of advisory
