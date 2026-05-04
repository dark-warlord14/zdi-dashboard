# ZDI-12-008: Citrix Provisioning Services streamprocess.exe vDisk Name Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-008
- **ZDI-CAN:** ZDI-CAN-1188
- **Date:** 2012-01-10
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Citrix
- **Affected Products:** Citrix Provisioning Services
- **Credit:** AbdulAziz Hariri of ThirdEyeTesters
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-008/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Citrix Provisioning Services. Authentication is not required to exploit this vulnerability. The specific flaw exists within the streamprocess.exe component which listens for UDP traffic on multiple ports, beginning with 6905. When handling a packet which requests a vDisk name, the user-supplied length value is not properly validated. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

Citrix has issued an update to correct this vulnerability. More details can be found at: http://support.citrix.com/article/CTX130846

## Disclosure Timeline

- 2011-04-01 - Vulnerability reported to vendor
- 2012-01-10 - Coordinated public release of advisory
