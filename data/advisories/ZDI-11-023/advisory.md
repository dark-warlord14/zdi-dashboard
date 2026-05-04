# ZDI-11-023: Citrix Provisioning Services streamprocess.exe Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-023
- **ZDI-CAN:** ZDI-CAN-746
- **Date:** 2011-01-20
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Citrix
- **Affected Products:** Citrix Provisioning Services
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-023/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Citrix Provisioning Services. Authentication is not required to exploit this vulnerability. The specific flaw exists within the streamprocess.exe component which listens by default on UDP port 6095. When handling a packet of type 0x40020010 the process blindly copies user supplied data into a fixed length buffer on the stack. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Citrix has issued an update to correct this vulnerability. More details can be found at: http://support.citrix.com/article/CTX127149

## Disclosure Timeline

- 2010-06-09 - Vulnerability reported to vendor
- 2011-01-20 - Coordinated public release of advisory
