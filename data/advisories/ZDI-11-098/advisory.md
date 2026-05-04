# ZDI-11-098: Apple Safari Webkit Runin Box Promotion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-098
- **ZDI-CAN:** ZDI-CAN-987
- **Date:** 2011-03-02
- **CVE:** CVE-2011-0132
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509 Jose A. Vazquez of {http://spa-s3c.blogspot.com/}
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-098/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way the WebKit library implements the requirements required for a Runin box as outlined in the Visual Formatting Model listed in the CSS 2.1 Specification. When promoting a run-in element the application will incorrectly free one of the child elements of the run-in. Later, when attempting to do layout for this element, the application will access the freed element due to the dangling reference. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4554

## Disclosure Timeline

- 2010-11-29 - Vulnerability reported to vendor
- 2011-03-02 - Coordinated public release of advisory
