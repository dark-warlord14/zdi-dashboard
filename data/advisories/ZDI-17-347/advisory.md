# ZDI-17-347: (Pwn2Own) Apple macOS speechsynthesisd Unsigned Dylib Loading Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-347
- **ZDI-CAN:** ZDI-CAN-4581
- **Date:** 2017-05-15
- **CVE:** CVE-2017-2534 , CVE-2017-6977
- **CVSS:** 4.6
- **CVSS Vector:** AV:L/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Niklas Baumstark and Samuel Groß
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-347/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the speechsynthesisd service. The issue results from the lack of proper validation of a library prior to loading it. An attacker can leverage this vulnerability to escalate privileges under the context of the current service.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT207797

## Disclosure Timeline

- 2017-03-15 - Vulnerability reported to vendor
- 2017-05-15 - Coordinated public release of advisory
