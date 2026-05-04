# ZDI-15-121: Apple OS X IOKit IOHIDSecurePromptClient Heap Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-121
- **ZDI-CAN:** ZDI-CAN-2676
- **Date:** 2015-04-08
- **CVE:** CVE-2015-1140
- **CVSS:** 6.8
- **CVSS Vector:** AV:L/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** lokihardt@ASRT
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-121/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within IOKit IOHIDSecurePromptClient. This does not check the length of an attacker-supplied string to the __InsertBytes method before copying it into a fixed length buffer on the heap. This allows an attacker to execute arbitrary code in the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT204659

## Disclosure Timeline

- 2015-01-08 - Vulnerability reported to vendor
- 2015-04-08 - Coordinated public release of advisory
