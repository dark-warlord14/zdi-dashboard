# ZDI-20-553: TP-Link TL-WA855RE login.json Improper Authentication Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-553
- **ZDI-CAN:** ZDI-CAN-10003
- **Date:** 2020-04-28
- **CVE:** CVE-2020-10916
- **CVSS:** 8.0
- **CVSS Vector:** AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** TP-Link
- **Affected Products:** TL-WA855RE
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-553/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to escalate privileges on affected installations of TP-Link TL-WA855RE Wi-Fi extenders. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the first-time setup process. The issue results from the lack of proper validation on first-time setup requests. An attacker can leverage this vulnerability to reset the password for the Admin account and execute code in the context of the device.

## Additional Details

Fixed in version TL-WA855RE(US)_V4_200403

## Disclosure Timeline

- 2020-03-15 - Vulnerability reported to vendor
- 2020-04-28 - Coordinated public release of advisory
