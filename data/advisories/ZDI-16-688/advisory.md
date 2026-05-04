# ZDI-16-688: Apple OS X CoreStorage Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-688
- **ZDI-CAN:** ZDI-CAN-3877
- **Date:** 2017-06-21
- **CVE:** CVE-2016-7603
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** daybreaker@Minionz
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-688/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within CoreStorage. The issue lies with the failure to validate user-supplied arguments which can cause a null pointer dereference. An attacker can leverage this vulnerability to escalate privileges and execute code under the context of the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207423

## Disclosure Timeline

- 2016-08-25 - Vulnerability reported to vendor
- 2017-06-21 - Coordinated public release of advisory
