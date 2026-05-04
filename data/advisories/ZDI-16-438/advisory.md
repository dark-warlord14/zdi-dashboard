# ZDI-16-438: Apple OS X DspFuncLib Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-438
- **ZDI-CAN:** ZDI-CAN-3694
- **Date:** 2016-07-20
- **CVE:** CVE-2016-4647
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Juwei Lin of Trend Micro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-438/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the handling of DspFuncLib. The issue lies in the failure to remove a reference after freeing an object. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT206903

## Disclosure Timeline

- 2016-04-12 - Vulnerability reported to vendor
- 2016-07-20 - Coordinated public release of advisory
