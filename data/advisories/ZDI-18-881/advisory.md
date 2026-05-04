# ZDI-18-881: VMWare Horizon Client wswc_sharedMem_shared Out-Of-Bounds Read Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-881
- **ZDI-CAN:** ZDI-CAN-5797
- **Date:** 2018-08-10
- **CVE:** CVE-2018-6970
- **CVSS:** 1.9
- **CVSS Vector:** AV:L/AC:M/Au:N/C:P/I:N/A:N
- **Affected Vendors:** VMware
- **Affected Products:** Horizon Client
- **Credit:** Steven Seeley (mr_me) of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-881/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on vulnerable installations of VMware Horizon Client. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within messages passed to the wswc_sharedMem_shared shared memory. The issue results from the lack of proper validation of user-supplied data, which can result in a read past the end of an allocated buffer. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of SYSTEM.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2018-0019.html

## Disclosure Timeline

- 2018-04-17 - Vulnerability reported to vendor
- 2018-08-10 - Coordinated public release of advisory
- 2018-08-10 - Advisory Updated
