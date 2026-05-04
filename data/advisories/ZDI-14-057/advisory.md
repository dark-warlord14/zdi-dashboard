# ZDI-14-057: Apple Mobile Safari isindex Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-057
- **ZDI-CAN:** ZDI-CAN-2109
- **Date:** 2014-04-03
- **CVE:** CVE-2014-1290
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** ant4g0nist (SegFault)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-057/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of isindex elements. The issue lies in setting attributes to invalid values. By manipulating a document's elements an attacker can force a dangling pointer to be reused after it has been freed. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT6162

## Disclosure Timeline

- 2014-01-30 - Vulnerability reported to vendor
- 2014-04-03 - Coordinated public release of advisory
