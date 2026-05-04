# ZDI-08-090: RealNetworks Helix Server DataConvertBuffer Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-090
- **ZDI-CAN:** ZDI-CAN-333
- **Date:** 2008-12-16
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** RealNetworks
- **Affected Products:** Helix Server
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-090/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of RealNetworks Helix Server. Authentication is not required to exploit this vulnerability. The specific flaw exists while processing malformed base64 encoded data from a SET_PARAMETER command containing the DataConvertBuffer header within an RTSP packet. The service fails to check that the data was properly decoded. The process then uses a faulty return value as a size parameter leading to an exploitable heap based buffer overflow. Exploitation of this vulnerability allows an attacker to execute arbitrary code under the context of the SYSTEM user.

## Disclosure Timeline

- 2008-05-13 - Vulnerability reported to vendor
- 2008-12-16 - Coordinated public release of advisory
- 2021-07-15 - Advisory Updated
