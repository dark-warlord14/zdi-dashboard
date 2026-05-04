# ZDI-16-643: Apple OS X AppleIntelFramebufferAzul Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-643
- **ZDI-CAN:** ZDI-CAN-3985
- **Date:** 2016-12-15
- **CVE:** CVE-2016-7602
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** OS X
- **Credit:** daybreaker@Minionz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-643/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple OS X. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within AppleIntelFramebufferAzul. The issue lies with the failure to validate user-supplied arguments which can cause a null pointer dereference. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207423

## Disclosure Timeline

- 2016-08-25 - Vulnerability reported to vendor
- 2016-12-15 - Coordinated public release of advisory
