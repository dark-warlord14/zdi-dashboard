# ZDI-18-1333: Apple macOS IOFramebufferUserClient Race Condition Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1333
- **ZDI-CAN:** ZDI-CAN-6834
- **Date:** 2018-10-31
- **CVE:** CVE-2018-4422
- **CVSS:** 7.0
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1333/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the IOFramebufferUserClient IOkit user client. The issue results from the lack of proper locking when performing operations on an object. An attacker can leverage this vulnerability to escalate privileges and execute code as the kernel.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/kb/HT201222

## Disclosure Timeline

- 2018-07-19 - Vulnerability reported to vendor
- 2018-10-31 - Coordinated public release of advisory
