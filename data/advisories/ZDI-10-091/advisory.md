# ZDI-10-091: Apple Webkit Attribute Child Removal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-091
- **ZDI-CAN:** ZDI-CAN-762
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1119
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** Ralf Philipp Weinmann Vincenzo Iozzo
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-091/
## Vulnerability Details

This vulnerability allows remote attackers to execute remote code on vulnerable installations of Apple Webkit. User interaction is required in that a target must be coerced into visiting a malicious page. The specific flaw exists within Webkit's process for destructing attribute objects via the removeChild method. If an attribute's child object is accessed after the attribute was removed from the document, an invalid pointer is referenced. This can be exploited by an attacker to execute remote code under the context of the user running the browser.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2010-03-26 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
