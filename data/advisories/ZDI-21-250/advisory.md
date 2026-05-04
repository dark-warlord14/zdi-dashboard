# ZDI-21-250: VMware ESXi SLP Heap-based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-250
- **ZDI-CAN:** ZDI-CAN-12232
- **Date:** 2021-02-24
- **CVE:** CVE-2021-21974
- **CVSS:** 8.8
- **CVSS Vector:** AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** ESXi
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-250/
## Vulnerability Details

This vulnerability allows network-adjacent attackers to execute arbitrary code on affected installations of VMware ESXi. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of SLP messages. The issue results from the lack of proper validation of the length of user-supplied data prior to copying it to a heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of the SLP daemon.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2021-0002.html

## Disclosure Timeline

- 2020-10-30 - Vulnerability reported to vendor
- 2021-02-24 - Coordinated public release of advisory
