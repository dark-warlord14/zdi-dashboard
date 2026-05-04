# ZDI-21-609: VMware Workstation ThinPrint JPEG2000 Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-609
- **ZDI-CAN:** ZDI-CAN-12832
- **Date:** 2021-05-25
- **CVE:** CVE-2021-21988
- **CVSS:** 6.5
- **CVSS Vector:** AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Workstation
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-609/
## Vulnerability Details

This vulnerability allows local attackers to disclose sensitive information on affected installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target guest system in order to exploit this vulnerability. The specific flaw exists within the ThinPrint component. When parsing JPEG2000 codestreams embedded in EMF files, the process does not properly validate user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to escalate privileges and execute arbitrary code in the context of the hypervisor.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2021-0009.html

## Disclosure Timeline

- 2021-02-03 - Vulnerability reported to vendor
- 2021-05-25 - Coordinated public release of advisory
