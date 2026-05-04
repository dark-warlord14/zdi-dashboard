# ZDI-20-587: Apple macOS printtool Daemon Improper Input Validation Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-587
- **ZDI-CAN:** ZDI-CAN-9859
- **Date:** 2020-05-06
- **CVE:** CVE-2020-3915
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** macOS
- **Credit:** HyungSeok Han (DaramG) @Theori
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-587/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple macOS. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the printtool daemon. The issue results from the lack of proper validation of printer icon data prior to further processing. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of root.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT211100

## Disclosure Timeline

- 2019-12-06 - Vulnerability reported to vendor
- 2020-05-06 - Coordinated public release of advisory
