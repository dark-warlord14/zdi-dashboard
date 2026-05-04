# ZDI-09-032: Apple WebKit attr() Invalid Attribute Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-032
- **ZDI-CAN:** ZDI-CAN-441
- **Date:** 2009-06-08
- **CVE:** CVE-2009-1698
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Safari
- **Credit:** Thierry Zoller
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-032/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple WebKit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the handling of attr() functions in a CSS content object. When a large numerical value is passed as the argument to the attr() function, a memory corruption will occur which can be leveraged to execute arbitrary coder under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT3613

## Disclosure Timeline

- 2009-03-26 - Vulnerability reported to vendor
- 2009-06-08 - Coordinated public release of advisory
