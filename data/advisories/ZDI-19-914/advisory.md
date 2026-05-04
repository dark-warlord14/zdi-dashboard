# ZDI-19-914: Foxit PhantomPDF Dwg2Pdf DWG File Parsing Out-Of-Bounds Write Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-914
- **ZDI-CAN:** ZDI-CAN-9274
- **Date:** 2019-10-22
- **CVE:** CVE-2019-17144
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** PhantomPDF
- **Credit:** Mat Powell of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-914/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Foxit PhantomPDF. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the conversion of DWG files to PDF. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated structure. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

The plugin Dwg2Pdf is End of Life and will not be included in Foxit Reader version 9.7 and higher.

## Disclosure Timeline

- 2019-08-09 - Vulnerability reported to vendor
- 2019-10-22 - Coordinated public release of advisory
