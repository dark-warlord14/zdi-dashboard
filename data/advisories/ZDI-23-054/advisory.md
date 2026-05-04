# ZDI-23-054: VMware vRealize Operations CaSA Improper Privilege Management Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-054
- **ZDI-CAN:** ZDI-CAN-17957
- **Date:** 2023-01-18
- **CVE:** CVE-2022-31707
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** vRealize
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-054/
## Vulnerability Details

This vulnerability allows remote attackers to escalate privileges on affected installations of VMware vRealize Operations. Authentication is required to exploit this vulnerability. The specific flaw exists within the configuration of CaSA. A crafted administrator command can trigger execution of a privileged operation. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of root.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2022-0034.html

## Disclosure Timeline

- 2022-08-31 - Vulnerability reported to vendor
- 2023-01-18 - Coordinated public release of advisory
