# ZDI-20-782: VMware Workstation Shader Bytecode Parsing Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-782
- **ZDI-CAN:** ZDI-CAN-10478
- **Date:** 2020-06-30
- **CVE:** CVE-2020-3970
- **CVSS:** 2.8
- **CVSS Vector:** AV:L/AC:H/PR:L/UI:N/S:C/C:L/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Wei Lei and anhdaden of STAR Labs
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-782/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the parsing of shader bytecode. By manipulating a document's elements, an attacker can trigger a read past the end of an allocated array. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0015.html

## Disclosure Timeline

- 2020-03-03 - Vulnerability reported to vendor
- 2020-06-30 - Coordinated public release of advisory
