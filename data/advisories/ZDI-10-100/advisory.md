# ZDI-10-100: Apple Webkit ConditionEventListener Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-100
- **ZDI-CAN:** ZDI-CAN-704
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1402
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-100/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application duplicates event listeners in .svg documents. Upon creating an AnimateTransform object, the library will create a timer to handle the transformation and duplicate the object's event listener into Webkit's "shadow tree" of the image. Upon destruction of the shadow tree and the original tree, the application will destroy the Element containing the event listener twice. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-02-18 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
