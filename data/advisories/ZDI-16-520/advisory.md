# ZDI-16-520: Apple OS X AppleUpstreamUserClient Out-Of-Bounds Access Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-520
- **ZDI-CAN:** ZDI-CAN-3715
- **Date:** 2016-09-20
- **CVE:** CVE-2016-4700
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Jack Tang of Trend Micro (@jacktang310) Moony Li of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-520/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of the AppleUpstreamUserClient kernel extension. The issue lies in the failure to validate the size of a buffer prior to accessing it. An attacker can leverage this vulnerability to execute code within the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207170

## Disclosure Timeline

- 2016-04-26 - Vulnerability reported to vendor
- 2016-09-20 - Coordinated public release of advisory
