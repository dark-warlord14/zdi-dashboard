# ZDI-19-963: Oracle VirtualBox Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-963
- **ZDI-CAN:** ZDI-CAN-8418
- **Date:** 2019-11-11
- **CVE:** CVE-2019-2867
- **CVSS:** 8.2
- **CVSS Vector:** AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** huyna of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-963/
## Vulnerability Details

This vulnerability allows local attackers to escalate privileges on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the shader_get_registers_used function. The issue results from the lack of proper validation of user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to escalate privileges and execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpujul2019.html

## Disclosure Timeline

- 2019-07-16 - Vulnerability reported to vendor
- 2019-11-11 - Coordinated public release of advisory
