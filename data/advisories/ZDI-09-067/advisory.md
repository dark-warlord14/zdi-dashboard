# ZDI-09-067: Novell NetWare NFS Portmapper and RPC Module Stack Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-067
- **ZDI-CAN:** ZDI-CAN-497
- **Date:** 2009-09-30
- **CVE:** N/A
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Novell
- **Affected Products:** Netware
- **Credit:** Nick DeBaggis Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-067/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Novell Netware NFS Portmapper daemon. Authentication is not required to exploit this vulnerability. The specific flaw exists within the processing of CALLIT RPC calls. The vulnerable daemon explicitly trusts a length field when receiving data which is later copied into a stack buffer, potentially resulting in a stack overflow. Successful exploitation of this vulnerability can lead to remote code execution under the context of the daemon.

## Additional Details

Novell has issued an update to correct this vulnerability. More details can be found at: http://download.novell.com/Download?buildid=1z3z-OsVCiE~

## Disclosure Timeline

- 2009-06-23 - Vulnerability reported to vendor
- 2009-09-30 - Coordinated public release of advisory
