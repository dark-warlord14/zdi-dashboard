# ZDI-08-089: RealNetworks Helix DNA Server RTSP DESCRIBE Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-089
- **ZDI-CAN:** ZDI-CAN-293
- **Date:** 2008-12-16
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** RealNetworks
- **Affected Products:** Helix Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-089/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of RealNetworks Helix Server. User interaction is not required to exploit this vulnerability. Authentication is not required to exploit this vulnerability. The specific flaw exists within the rmserver.exe process while processing the Proxy-Require header of an RTSP response. The service fails to check the length of the field leading to an exploitable heap based buffer overflow. Exploitation of this vulnerability allows an attacker to execute arbitrary code under the context of the SYSTEM user.

## Disclosure Timeline

- 2008-02-07 - Vulnerability reported to vendor
- 2008-12-16 - Coordinated public release of advisory
