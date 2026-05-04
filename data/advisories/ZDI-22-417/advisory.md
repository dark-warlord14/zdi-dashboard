# ZDI-22-417: (Pwn2Own) Cisco RV340 update-clients Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-417
- **ZDI-CAN:** ZDI-CAN-15893
- **Date:** 2022-02-22
- **CVE:** CVE-2022-20708
- **CVSS:** 6.8
- **CVSS Vector:** AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Cisco
- **Affected Products:** RV340
- **Credit:** Q. Kaiser from IoT Inspector Research Lab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-417/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of Cisco RV340 routers. Although authentication is required to exploit this vulnerability, the existing authentication mechanism can be bypassed. The specific flaw exists within the handling of the update-clients method. The issue results from the lack of proper validation of a user-supplied string before using it to execute a system call. An attacker can leverage this vulnerability to execute code in the context of root.

## Additional Details

Cisco has issued an update to correct this vulnerability. More details can be found at: https://tools.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-smb-mult-vuln-KA9PK6D

## Disclosure Timeline

- 2022-01-26 - Vulnerability reported to vendor
- 2022-02-22 - Coordinated public release of advisory
