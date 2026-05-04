# ZDI-23-1497: Apple iTunes Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1497
- **ZDI-CAN:** ZDI-CAN-16895
- **Date:** 2023-10-04
- **CVE:** CVE-2022-26773
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apple
- **Affected Products:** iTunes
- **Credit:** @decoder_it
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1497/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Apple iTunes. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the Apple Mobile Device Service. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: https://support.apple.com/en-us/HT213259

## Disclosure Timeline

- 2022-06-22 - Vulnerability reported to vendor
- 2023-10-04 - Coordinated public release of advisory
