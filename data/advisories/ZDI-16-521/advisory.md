# ZDI-16-521: Apple OS X AppleHSSPIHIDDriver Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-521
- **ZDI-CAN:** ZDI-CAN-3822
- **Date:** 2016-09-20
- **CVE:** CVE-2016-4697
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** Qidan He(@flanker_hqd) from KeenLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-521/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the AppleHSSPIHIDDriver kext. The issue lies in the failure to properly validate the length of user-supplied data prior to copying it to a buffer. An attacker can leverage this vulnerability to escalate privileges under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207170

## Disclosure Timeline

- 2016-06-14 - Vulnerability reported to vendor
- 2016-09-20 - Coordinated public release of advisory
