# ZDI-11-217: Adobe Shockwave Font Structure Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-217
- **ZDI-CAN:** ZDI-CAN-1055
- **Date:** 2011-06-14
- **CVE:** CVE-2011-2109
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Adobe
- **Affected Products:** Shockwave Player
- **Credit:** Sebastian Apelt (www.siberas.de)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-217/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Adobe Shockwave Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Font Asset.x32 module responsible for parsing font-related structures within Director movies (.dir). The code within this module extracts and copies strings without any bounds checking. Several calls to strcpy can be abused to overwrite stack buffers and subsequently execute remote code under the context of the user running the browser.

## Additional Details

Adobe has issued an update to correct this vulnerability. More details can be found at: http://www.adobe.com/support/security/bulletins/apsb11-17.html

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
