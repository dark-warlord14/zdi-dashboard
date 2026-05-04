# ZDI-15-286: Apple OS X LZVN DMG Information Disclosure Vulnerabillity

## Metadata

- **ZDI ID:** ZDI-15-286
- **ZDI-CAN:** ZDI-CAN-2719
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3677
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-286/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DMG files. The issue lies in the handling of LZVN compressed streams. An attacker can leverage this vulnerability to leak the sensitive contents of physical memory.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2015-02-26 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
