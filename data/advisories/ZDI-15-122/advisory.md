# ZDI-15-122: Apple OS X XNU HFS_GETPATH Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-122
- **ZDI-CAN:** ZDI-CAN-2682
- **Date:** 2015-04-08
- **CVE:** CVE-2015-1101
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-122/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within XNU HFS_GETPATH. This does not check the length of an attacker-supplied string before copying it into a fixed length buffer. This allows an attacker to execute arbitrary code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT204659

## Disclosure Timeline

- 2015-01-27 - Vulnerability reported to vendor
- 2015-04-08 - Coordinated public release of advisory
