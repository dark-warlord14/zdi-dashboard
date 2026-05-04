# ZDI-21-1110: VMware vCenter Server Appliance External Control of File Path Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-21-1110
- **ZDI-CAN:** ZDI-CAN-13636
- **Date:** 2021-09-22
- **CVE:** CVE-2021-22009
- **CVSS:** 4.0
- **CVSS Vector:** AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:L
- **Affected Vendors:** VMware
- **Affected Products:** vCenter Server Appliance
- **Credit:** Sergey Gerasimov and George webpentest Noseevich of SolidLab
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-21-1110/
## Vulnerability Details

This vulnerability allows local attackers to create a denial-of-service condition on affected installations of VMware vCenter Server Appliance. An attacker must first obtain the ability to execute low-privileged code on the target system in order to exploit this vulnerability. The specific flaw exists within the processing of jsonrpc messages. A crafted request can trigger a file read operation of a blocking or slow character stream. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

VMware has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2021-0020.html

## Disclosure Timeline

- 2021-05-26 - Vulnerability reported to vendor
- 2021-09-22 - Coordinated public release of advisory
