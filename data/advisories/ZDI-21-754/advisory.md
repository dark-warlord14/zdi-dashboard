# ZDI-21-754: VMware Workstation Tools Uncontrolled Search Path Element Local Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-754
- **ZDI-CAN:** ZDI-CAN-13068
- **Date:** 2021-06-23
- **CVE:** CVE-2021-21999
- **CVSS:** 7.8
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Zeeshan Shaikh (@bugzzzhunter) from NotSoSecure
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-754/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the VGAuthService service. The issue results from the lack of proper validation of a user-supplied OpenSSL configuration file prior to using it. An attacker can leverage this vulnerability to escalate privileges and execute arbitrary code in the context of SYSTEM.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2021-0013.html

## Disclosure Timeline

- 2021-03-03 - Vulnerability reported to vendor
- 2021-06-23 - Coordinated public release of advisory
