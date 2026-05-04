# ZDI-11-228: Apple ColorSync ICC Profile ncl2 Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-228
- **ZDI-CAN:** ZDI-CAN-1147
- **Date:** 2011-06-29
- **CVE:** CVE-2011-0200
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple, Apple, Apple
- **Affected Products:** OS X, Safari
- **Credit:** binaryproof
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-228/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Safari on Windows and multiple applications on OSX. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the ColorSync component which is used when handling image files containing embedded ICC data. When handling the ncl2 tag the process miscalculates an integer value used in a memory allocation. This buffer is later used as a destination when copying user controlled data. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user running the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4723

## Disclosure Timeline

- 2011-04-04 - Vulnerability reported to vendor
- 2011-06-29 - Coordinated public release of advisory
