# ZDI-06-015: Apple QuickTime H.264 Parsing Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-015
- **ZDI-CAN:** ZDI-CAN-033
- **Date:** 2006-05-11
- **CVE:** CVE-2006-1463
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** ATmaCA
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-015/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple's QuickTime media player. The specific flaw exists within the parsing of H.264 content. The implicit trust of a user-supplied size value during a memory copy loop allows an attacker to create an exploitable memory corruption condition. Exploitation requires that an attacker either coerce the target to open a malformed media file or visit a website embedding the malicious file.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://www.apple.com/support/downloads/

## Disclosure Timeline

- 2006-03-20 - Vulnerability reported to vendor
- 2006-05-11 - Coordinated public release of advisory
