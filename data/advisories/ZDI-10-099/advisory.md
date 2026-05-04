# ZDI-10-099: Apple Webkit ProcessInstruction Target Error Message Insertion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-099
- **ZDI-CAN:** ZDI-CAN-702
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1403
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-099/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists with how WebKit inserts error messages into documents utilizing the SVG namespace. Upon a parsing error the library will attempt to access an element before repairing the XML. This will cause the library to access uninitialized memory which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-02-23 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
