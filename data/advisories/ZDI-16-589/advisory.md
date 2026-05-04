# ZDI-16-589: Apple OS X AppleSMC smcHandleYPCEvent Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-589
- **ZDI-CAN:** ZDI-CAN-3908
- **Date:** 2016-11-02
- **CVE:** CVE-2016-4678
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** daybreaker@Minionz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-589/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within AppleSMC's smcHandleYPCEvent. The process does not properly validate the existence of an object prior to performing operations on it. An attacker can leverage this vulnerability to escalate privileges under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT201222

## Disclosure Timeline

- 2016-08-23 - Vulnerability reported to vendor
- 2016-11-02 - Coordinated public release of advisory
