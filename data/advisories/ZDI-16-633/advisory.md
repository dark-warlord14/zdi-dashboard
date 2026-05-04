# ZDI-16-633: Apple OS X IOKit Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-633
- **ZDI-CAN:** ZDI-CAN-3992
- **Date:** 2016-12-13
- **CVE:** CVE-2016-7616
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** daybreaker@Minionz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-633/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within of the IOHDIXController kext. The issue lies from the lack of proper validation to ensure that a pointer is not null prior to accessing it. An attacker can leverage this vulnerability to escalate privileges under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207423

## Disclosure Timeline

- 2016-12-12 - Vulnerability reported to vendor
- 2016-12-13 - Coordinated public release of advisory
