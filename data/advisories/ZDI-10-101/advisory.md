# ZDI-10-101: Apple Webkit SVG RadialGradiant Run-in Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-101
- **ZDI-CAN:** ZDI-CAN-764
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1749
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-101/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's support of the run-in display property. On insertion of a specific element with the "run-in" display property, the application will create a duplicate reference of a child element used to support that attribute. Upon destruction of the parent container, the application will then call the destructor for this child element multiple times. Successful exploitation can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-05-03 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
