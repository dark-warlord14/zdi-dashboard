# ZDI-11-251: Apple QuickTime STSS atom Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-251
- **ZDI-CAN:** ZDI-CAN-1161
- **Date:** 2011-08-09
- **CVE:** CVE-2011-0250
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Matt "j00ru" Jurczyk
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-251/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Quicktime handles invalid values in the Sync Sample Atom. Due to a signed compare instead of an unsigned compare it is possible to corrupt the Sample Atom Table. Values from this table are later used to populate a heap buffer and the corrupted value causes a heap overflow. This can result in remote code execution under the context of the current user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4826

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2011-08-09 - Coordinated public release of advisory
