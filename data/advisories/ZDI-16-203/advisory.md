# ZDI-16-203: Apple OS X XML Double Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-203
- **ZDI-CAN:** ZDI-CAN-3420
- **Date:** 2016-03-22
- **CVE:** CVE-2016-1761
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** wol0xff
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-203/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of XML files. The issue lies in the handling of ENTITY declarations that reference unsupported protocols. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206167

## Disclosure Timeline

- 2015-12-03 - Vulnerability reported to vendor
- 2016-03-22 - Coordinated public release of advisory
