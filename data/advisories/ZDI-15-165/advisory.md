# ZDI-15-165: Apple OS X IOHIDSecurePromptClient Untrusted Pointer Dereference Arbitrary Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-165
- **ZDI-CAN:** ZDI-CAN-2814
- **Date:** 2015-04-29
- **CVE:** CVE-2015-1140
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Vitaliy Toropov
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-165/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of calls to IOHIDSecurePromptClient. The issue lies in the failure to properly sanitize user-supplied pointers before they are dereferenced. An attacker can leverage this vulnerability to overwrite arbitrary kernel memory.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT204659

## Disclosure Timeline

- 2015-03-27 - Vulnerability reported to vendor
- 2015-04-29 - Coordinated public release of advisory
