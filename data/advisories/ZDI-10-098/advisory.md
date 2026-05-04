# ZDI-10-098: Apple Webkit First-Letter Pseudo-Element Style Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-098
- **ZDI-CAN:** ZDI-CAN-689
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1401
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-098/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Webkit. User interaction is required in that a user must visit a website or open a malicious document. The specific flaw exists within the way Webkit implements the 'first-letter' css style. If a container with the first-color style has it's contents replaced with a particular element, the library will create a dual reference of the style in order to apply to its contents. Later when the element is freed, the dangling reference will still be applied to the style. Upon navigating the document's styles for either repainting or style recalculation, the application will access the freed memory which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-02-23 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
