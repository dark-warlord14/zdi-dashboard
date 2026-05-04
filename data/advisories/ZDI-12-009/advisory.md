# ZDI-12-009: Citrix Provisioning Services Stream Service 0x40020000 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-009
- **ZDI-CAN:** ZDI-CAN-1291
- **Date:** 2012-01-10
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Citrix
- **Affected Products:** Citrix Provisioning Services
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-009/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Citrix Provisioning Services. Authentication is not required to exploit this vulnerability. The flaw exists within the streamprocess.exe component. This process listens on UDP port 6905. When handling a request type 0x40020000 the process uses the user supplied length in an attempted bounds check before copying to a local stack buffer. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of SYSTEM.

## Additional Details

Citrix has issued an update to correct this vulnerability. More details can be found at: http://support.citrix.com/article/CTX130846

## Disclosure Timeline

- 2011-07-22 - Vulnerability reported to vendor
- 2012-01-10 - Coordinated public release of advisory
