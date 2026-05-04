# ZDI-11-140: Webkit Detached Body Element Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-140
- **ZDI-CAN:** ZDI-CAN-1026
- **Date:** 2011-04-19
- **CVE:** CVE-2011-0234
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Rob King
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-140/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application manages a reference to an anonymous block located near a particular element within the document. When cloning this element, the application will duplicate a reference to the block and then later re-attach this element to the rendering tree. During this process the library will free the original rendering element. Subsequent access to the same element will then cause the library to use the freed object. This can be utilized to achieve code execution under the context of the application.

## Additional Details

Webkit fix: https://trac.webkit.org/changeset/67182 Apple fix: https://support.apple.com/kb/HT4808

## Disclosure Timeline

- 2011-03-31 - Vulnerability reported to vendor
- 2011-04-19 - Coordinated public release of advisory
- 2020-07-30 - Advisory Updated
