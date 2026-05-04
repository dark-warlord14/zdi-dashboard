# ZDI-20-1178: VMware Workstation ThinPrint TTCHeader Integer Overflow Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1178
- **ZDI-CAN:** ZDI-CAN-10923
- **Date:** 2020-09-15
- **CVE:** CVE-2020-3990
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** linhlhq of VinCSS (Member of Vingroup)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1178/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the ThinPrint component. Crafted data in a font file can result in an integer overflow before reading from memory. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0020.html

## Disclosure Timeline

- 2020-04-30 - Vulnerability reported to vendor
- 2020-09-15 - Coordinated public release of advisory
