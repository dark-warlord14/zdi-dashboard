# ZDI-23-1114: ESET Smart Security Link Following Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1114
- **ZDI-CAN:** ZDI-CAN-20587
- **Date:** 2023-08-15
- **CVE:** CVE-2023-3160
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** ESET
- **Affected Products:** Smart Security
- **Credit:** Filip Dragovic (@filip_dragovic)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1114/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of ESET Smart Security. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the ekrn service. By creating a symbolic link, an attacker can abuse the service to delete a file. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

ESET has issued an update to correct this vulnerability. More details can be found at: https://support.eset.com/en/ca8466-eset-customer-advisory-local-privilege-escalation-vulnerability-fixed-in-eset-security-products-for-windows

## Disclosure Timeline

- 2023-04-28 - Vulnerability reported to vendor
- 2023-08-15 - Coordinated public release of advisory
