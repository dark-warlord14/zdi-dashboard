# ZDI-13-140: Microsoft Internet Explorer SmartDispClient Type Confusion Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-140
- **ZDI-CAN:** ZDI-CAN-1822
- **Date:** 2013-06-27
- **CVE:** CVE-2013-3124
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Microsoft
- **Affected Products:** Internet Explorer
- **Credit:** Omair and Amol Naik
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-140/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Microsoft Internet Explorer. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the document layout formatting. By manipulating a document's elements an attacker can force a type confusion error in the layout process. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Disclosure Timeline

- 2013-03-29 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
