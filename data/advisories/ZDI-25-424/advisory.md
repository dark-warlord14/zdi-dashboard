# ZDI-25-424: Mikrotik RouterOS VXLAN Source IP Improper Access Control Vulnerability

## Metadata

- **ZDI ID:** ZDI-25-424
- **ZDI-CAN:** ZDI-CAN-26415
- **Date:** 2025-06-25
- **CVE:** CVE-2025-6443
- **CVSS:** 7.2
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N
- **Affected Vendors:** Mikrotik
- **Affected Products:** RouterOS
- **Credit:** Trend Micro (SHU-HAO, TUNG) (123ojp)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-25-424/
## Vulnerability Details

This vulnerability allows remote attackers to bypass access restrictions on affected installations of Mikrotik RouterOS. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of remote IP addresses when processing VXLAN traffic. The issue results from the lack of validation of the remote IP address against configured values prior to allowing ingress traffic into the internal network. An attacker can leverage this vulnerability to gain access to internal network resources.

## Additional Details

Fixed in RouterOS v7.20

## Disclosure Timeline

- 2025-02-13 - Vulnerability reported to vendor
- 2025-06-25 - Coordinated public release of advisory
- 2025-06-25 - Advisory Updated
