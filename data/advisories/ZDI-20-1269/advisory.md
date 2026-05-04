# ZDI-20-1269: VMware ESXi SLP Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-1269
- **ZDI-CAN:** ZDI-CAN-11563
- **Date:** 2020-10-20
- **CVE:** CVE-2020-3992
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** VMware
- **Affected Products:** ESXi
- **Credit:** Lucas Leong (@_wmliang_) of Trend Micro's Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-1269/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of VMware ESXi. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of SLP messages. The issue results from the lack of validating the existence of an object prior to performing operations on the object. An attacker can leverage this vulnerability to execute code in the context of the SLP daemon.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2020-0023.html

## Disclosure Timeline

- 2020-07-22 - Vulnerability reported to vendor
- 2020-10-20 - Coordinated public release of advisory
