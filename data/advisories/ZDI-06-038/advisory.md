# ZDI-06-038: Citrix MetaFrame IMA Management Module Remote Heap Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-06-038
- **ZDI-CAN:** ZDI-CAN-062
- **Date:** 2006-11-09
- **CVE:** CVE-2006-5821
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Citrix
- **Affected Products:** Metaframe Server
- **Credit:** Eric Detoisien and an anonymous researcher
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-06-038/
## Vulnerability Details

This vulnerability allows attackers to execute arbitrary code on vulnerable installations of Citrix MetaFrame Presentation Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the routine IMA_SECURE_DecryptData1() defined in ImaSystem.dll and is reachable through the Independant Management Architecture (IMA) service (ImaSrv.exe) that listens on TCP port 2512 or 2513. The encryption scheme used is reversible and relies on several 32-bit fields indicating the size of the packet and the offsets to the authentication strings. During the decryption of authentication data an attacker can specify invalid sizes that result in an exploitable heap corruption.

## Additional Details

Citrix has issued an update to correct this vulnerability. More details can be found at: http://support.citrix.com/article/CTX111186

## Disclosure Timeline

- 2006-06-16 - Vulnerability reported to vendor
- 2006-11-09 - Coordinated public release of advisory
