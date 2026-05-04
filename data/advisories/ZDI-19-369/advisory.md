# ZDI-19-369: VMware Workstation Shader Bytecode Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-369
- **ZDI-CAN:** ZDI-CAN-7195
- **Date:** 2019-04-17
- **CVE:** CVE-2019-5520
- **CVSS:** 2.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** instructor
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-369/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the parsing of shader bytecode. By manipulating a document's elements, an attacker can trigger a read past the end of an allocated array. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2019-0006.html

## Disclosure Timeline

- 2018-08-30 - Vulnerability reported to vendor
- 2019-04-17 - Coordinated public release of advisory
