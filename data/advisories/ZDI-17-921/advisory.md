# ZDI-17-921: VMware Workstation NAT IP Fragment Reassembly Heap-based Buffer Overflow Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-921
- **ZDI-CAN:** ZDI-CAN-4909
- **Date:** 2017-11-21
- **CVE:** CVE-2017-4934
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** VMware
- **Affected Products:** VMware Workstation
- **Credit:** Jun Mao of Tencent PC Manager
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-921/
## Vulnerability Details

This vulnerability allows local attackers to execute arbitrary code on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the handling of the NAT IP Fragment Reassembly. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a fixed-length heap-based buffer. An attacker can leverage this vulnerability to elevate privileges and execute arbitrary code under the context of SYSTEM in the host OS.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2017-0018.html

## Disclosure Timeline

- 2017-06-16 - Vulnerability reported to vendor
- 2017-11-21 - Coordinated public release of advisory
