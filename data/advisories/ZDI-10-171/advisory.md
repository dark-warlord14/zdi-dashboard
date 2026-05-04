# ZDI-10-171: Mozilla Firefox nsTreeContentView Dangling Pointer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-171
- **ZDI-CAN:** ZDI-CAN-804
- **Date:** 2010-09-13
- **CVE:** CVE-2010-3167
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Mozilla Firefox
- **Affected Products:** 3.6.x
- **Credit:** regenrecht
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-171/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Mozilla Firefox. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the implementation of a particular element within the XUL namespace. Due to a method for the element having the side effect of executing javascript, an attacker can provide their own javascript code which can be used to remove an object out from underneath the element's child hierarchy. This can force the application to make an invalid reference when traversing it's internal objects, thus using an illegitimate pointer. This can be leveraged by an attacker to execute arbitrary code under the context of the application.

## Additional Details

Mozilla Firefox has issued an update to correct this vulnerability. More details can be found at: http://www.mozilla.org/security/announce/2010/mfsa2010-56.html

## Disclosure Timeline

- 2010-06-30 - Vulnerability reported to vendor
- 2010-09-13 - Coordinated public release of advisory
