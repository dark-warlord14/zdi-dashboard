# ZDI-10-110: Adobe Flash Player Multiple Tag JPEG Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-110
- **ZDI-CAN:** ZDI-CAN-636
- **Date:** 2010-06-16
- **CVE:** CVE-2010-2171
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Adobe
- **Affected Products:** Flash Player
- **Credit:** Anonymous Tielei Wang, from ICST-ERCIS, Peking University
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-110/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Adobe Flash Player. User interaction is required in that a target must visit a malicious website. The specific flaw exists within the code for parsing embedded image data within SWF files. The DefineBits tag and several of its variations are prone to a parsing issue while handling JPEG data. Specifically, the vulnerability is due to decompression routines that do not validate image dimensions sufficiently before performing operations on heap memory. An attacker can exploit this vulnerability to execute arbitrary code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb10-14.html

## Disclosure Timeline

- 2010-06-08 - Vulnerability reported to vendor
- 2010-06-16 - Coordinated public release of advisory
