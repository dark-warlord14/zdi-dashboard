# ZDI-16-637: Apple OS X AppleIntelHD5000Graphics Null Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-637
- **ZDI-CAN:** ZDI-CAN-3677
- **Date:** 2016-12-15
- **CVE:** CVE-2016-1818
- **CVSS:** 7.2
- **CVSS Vector:** AV:L/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** sweetchip@GRAYHASH
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-637/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AppleIntelHD5000Graphics kernel extension. The issue lies in the failure to ensure that a user-supplied pointer is valid prior to dereferencing it. An attacker could leverage this vulnerability to execute code within the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206567

## Disclosure Timeline

- 2016-04-26 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
