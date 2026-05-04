# ZDI-11-139: Webkit Anonymous Frame Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-139
- **ZDI-CAN:** ZDI-CAN-1035
- **Date:** 2011-04-19
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** WebKit
- **Affected Products:** WebKit
- **Credit:** wushi of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-139/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the library's implementation of a frame element. When parsing a malformed document embedded inside an SVG document, the library will create an anonymous block around a frame element in the block's contents. When freeing this anonymous block via an assignment to the read-only .textContent attribute, a reference to one of the child elements will still exist. Accessing this child element can then lead to code execution under the context of the application.

## Additional Details

Webkit fix: http://trac.webkit.org/changeset/81611

## Disclosure Timeline

- 2011-03-31 - Vulnerability reported to vendor
- 2011-04-19 - Coordinated public release of advisory
