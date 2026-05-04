# ZDI-18-779: VMware Workstation SetGuestInfo Null Pointer Dereference Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-779
- **ZDI-CAN:** ZDI-CAN-6079
- **Date:** 2018-07-26
- **CVE:** CVE-2018-6972
- **CVSS:** 4.9
- **CVSS Vector:** AV:L/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** VMware
- **Affected Products:** VMware Workstation
- **Credit:** Hahna Latonick and Kevin Fujimoto
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-779/
## Vulnerability Details

This vulnerability allows local attackers to deny service on vulnerable installations of VMware Workstation. An attacker must first obtain the ability to execute low-privileged code on a guest OS in order to exploit this vulnerability. The specific flaw exists within the SetGuestInfo RPC function. A crafted request can trigger the dereference of a null pointer. An attacker can leverage this vulnerability to create a denial-of-service condition to users of the guest OS.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2018-0018.html

## Disclosure Timeline

- 2018-04-17 - Vulnerability reported to vendor
- 2018-07-26 - Coordinated public release of advisory
- 2018-07-26 - Advisory Updated
