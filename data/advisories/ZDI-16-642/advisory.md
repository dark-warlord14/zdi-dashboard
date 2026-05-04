# ZDI-16-642: Apple OS X AppleGraphicsPowerManagement Null Pointer Dereference Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-642
- **ZDI-CAN:** ZDI-CAN-3864
- **Date:** 2016-12-15
- **CVE:** CVE-2016-7609
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** daybreaker@Minionz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-642/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the AppleGraphicsPowerManagement kext. The issue lies in the absence of a check to ensure that a pointer is not null. An attacker can leverage this vulnerability to escalate privileges under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207423

## Disclosure Timeline

- 2016-09-06 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
