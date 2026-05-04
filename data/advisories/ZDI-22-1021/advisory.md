# ZDI-22-1021: VMware ESXi TCP/IP Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1021
- **ZDI-CAN:** ZDI-CAN-16259
- **Date:** 2022-07-28
- **CVE:** N/A
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** ESXi
- **Credit:** Reno Robert of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1021/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware ESXi. Authentication is not required to exploit this vulnerability. The specific flaw exists within the TCP/IP kernel module. The issue results from the lack of proper validation of user-supplied data, which can result in a memory corruption condition. An attacker can leverage this vulnerability to execute code in the context of the kernel.

## Additional Details

https://docs.vmware.com/en/VMware-vSphere/7.0/rn/vsphere-esxi-70u3f-release-notes.html https://docs.vmware.com/en/VMware-vSphere/6.7/rn/esxi670-202206001.html https://docs.vmware.com/en/VMware-vSphere/6.5/rn/esxi650-202205001.html

## Disclosure Timeline

- 2022-01-12 - Vulnerability reported to vendor
- 2022-07-28 - Coordinated public release of advisory
- 2022-07-28 - Advisory Updated
