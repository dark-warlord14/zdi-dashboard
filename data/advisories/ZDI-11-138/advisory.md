# ZDI-11-138: Webkit Undefined DOM Prototype Attach Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-138
- **ZDI-CAN:** ZDI-CAN-1036
- **Date:** 2011-04-19
- **CVE:** CVE-2011-0234
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-138/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the application's implementation of a Frame element. When attaching this element to a document, the application will duplicate a reference of an anonymous block. When freeing the container holding the Frame element, the reference will still be available. If an attacker can perform an explicit type change of the contents the element this can then be leveraged to gain code execution under the context of the application.

## Disclosure Timeline

- 2011-03-31 - Vulnerability reported to vendor
- 2011-04-19 - Coordinated public release of advisory
- 2020-07-30 - Advisory Updated
