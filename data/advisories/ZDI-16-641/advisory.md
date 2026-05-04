# ZDI-16-641: Apple OS X IntelHD5000 IGAccelResource Use-After-Free Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-641
- **ZDI-CAN:** ZDI-CAN-3823
- **Date:** 2016-12-15
- **CVE:** CVE-2016-7582
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** AE25B5B6122635997A168A0B8393D20D
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-641/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the IntelHD5000 kext. The issue lies in the failure to properly validate the existence of an object prior to performing operations on it. An attacker can leverage this vulnerability to escalate privileges under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207170

## Disclosure Timeline

- 2016-06-14 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
