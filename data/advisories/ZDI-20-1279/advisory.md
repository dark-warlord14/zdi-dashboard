# ZDI-20-1279: Oracle VirtualBox Shader Bytecode Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1279
- **ZDI-CAN:** ZDI-CAN-11676
- **Date:** 2020-10-22
- **CVE:** CVE-2020-14884
- **CVSS:** 5.3
- **CVSS Vector:** AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** Oracle
- **Affected Products:** VirtualBox
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1279/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of Oracle VirtualBox. An attacker must first obtain the ability to execute high-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the shader_record_register_usage function. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2020.html

## Disclosure Timeline

- 2020-08-19 - Vulnerability reported to vendor
- 2020-10-22 - Coordinated public release of advisory
