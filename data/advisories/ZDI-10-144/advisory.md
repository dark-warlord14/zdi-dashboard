# ZDI-10-144: Apple Webkit Rendering Counter Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-144
- **ZDI-CAN:** ZDI-CAN-784
- **Date:** 2010-08-09
- **CVE:** CVE-2010-1784
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-144/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within Webkit's support for generated content. When utilizing generated content on a particular element, the library will insert more than one reference of the generated element element. During page destruction the application will navigate through the reference to discover more elements to destroy. This can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4276

## Disclosure Timeline

- 2010-06-01 - Vulnerability reported to vendor
- 2010-08-09 - Coordinated public release of advisory
