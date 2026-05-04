# ZDI-10-142: Apple Webkit SVG First-Letter Style Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-142
- **ZDI-CAN:** ZDI-CAN-782
- **Date:** 2010-08-05
- **CVE:** CVE-2010-1785
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-142/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the library's implementation of the first-letter style in the context of an SVG text element. Upon applying the style to this element, the library will calculate the height for determining the overflow for an inline box. While traversing the elements for the height, the library will utilize data from a non-existent linebox. Successful exploitation will lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4276

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-08-05 - Coordinated public release of advisory
