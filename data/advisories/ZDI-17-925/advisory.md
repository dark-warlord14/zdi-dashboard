# ZDI-17-925: Apple macOS nsurlstoraged Integer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-925
- **ZDI-CAN:** ZDI-CAN-4927
- **Date:** 2017-11-20
- **CVE:** CVE-2017-13833
- **CVSS:** 4.4
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** Niklas Baumstark and Samuel Gro
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-925/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on vulnerable installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the nsurlstoraged service. The issue results from the lack of proper validation of a reference count, which can result in an integer overflow when incrementing it. An attacker can leverage this vulnerability to escalate privileges under the context of the current service.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT208112

## Disclosure Timeline

- 2017-06-22 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
