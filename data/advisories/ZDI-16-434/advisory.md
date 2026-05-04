# ZDI-16-434: Apple OS X AppleIntelBDWGraphics Memory Corruption Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-434
- **ZDI-CAN:** ZDI-CAN-3687
- **Date:** 2016-07-20
- **CVE:** CVE-2016-4633
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** 7CD6CBC56470722CD7DEA01561796431
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-434/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the AppleIntelBDWGraphics kernel extension. The issue lies in the failure to properly check user-supplied arguments during an IOKit call. An attacker can leverage this vulnerability to execute code within the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206903

## Disclosure Timeline

- 2016-04-26 - Vulnerability reported to vendor
- 2016-07-20 - Coordinated public release of advisory
