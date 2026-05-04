# ZDI-17-357: (Pwn2Own) Apple macOS diskarbitrationd Time-Of-Check/Time-Of-Use Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-357
- **ZDI-CAN:** ZDI-CAN-4580
- **Date:** 2017-05-18
- **CVE:** CVE-2017-2533
- **CVSS:** 6.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Niklas Baumstark and Samuel Groß
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-357/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the diskarbitrationd service. The issue lies in the lack of proper validation of paths prior to using them. An attacker can leverage this vulnerability to escalate privileges under the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207797

## Disclosure Timeline

- 2017-03-17 - Vulnerability reported to vendor
- 2017-05-18 - Coordinated public release of advisory
