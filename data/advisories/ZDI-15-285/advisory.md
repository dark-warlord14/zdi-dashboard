# ZDI-15-285: Apple iOS ICC Profile curv Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-285
- **ZDI-CAN:** ZDI-CAN-2761
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3723
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** iOS
- **Credit:** chaithanya (SegFault)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-285/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple iOS. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of ICC profiles. The issue lies in the parsing of 'curv' types. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2015-02-26 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
