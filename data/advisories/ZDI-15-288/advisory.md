# ZDI-15-288: Apple OS X NTFS Compression Block Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-288
- **ZDI-CAN:** ZDI-CAN-2815
- **Date:** 2015-07-01
- **CVE:** CVE-2015-3711
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Peter Rutenbar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-288/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must open a malicious file. The specific flaw exists within the handling of NTFS file systems. The issue lies in the handling of compressed blocks. An attacker can leverage this vulnerability to leak the sensitive contents of physical memory.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2015-03-27 - Vulnerability reported to vendor
- 2015-07-01 - Coordinated public release of advisory
