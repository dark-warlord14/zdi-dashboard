# ZDI-20-1231: Foxit Reader Update Service Incorrect Permission Assignment Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1231
- **ZDI-CAN:** ZDI-CAN-11229
- **Date:** 2020-09-29
- **CVE:** CVE-2020-17414
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Foxit
- **Affected Products:** Reader
- **Credit:** @Kharosx0
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1231/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Foxit Reader. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the configuration files used by the Foxit Reader Update Service. The issue results from incorrect permissions set on a resource used by the service. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of SYSTEM.

## Additional Details

Foxit has issued an update to correct this vulnerability. More details can be found at: https://www.foxitsoftware.com/support/security-bulletins.php

## Disclosure Timeline

- 2020-06-12 - Vulnerability reported to vendor
- 2020-09-29 - Coordinated public release of advisory
- 2020-10-09 - Advisory Updated
