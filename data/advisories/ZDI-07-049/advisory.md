# ZDI-07-049: EMC Legato Networker Remote Exec Service Stack Overflow Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-07-049
- **ZDI-CAN:** ZDI-CAN-170
- **Date:** 2007-08-20
- **CVE:** CVE-2007-3618
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** EMC
- **Affected Products:** NetWorker
- **Credit:** Tenable Network Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-07-049/
## Vulnerability Details

These vulnerabilities allow remote attackers to execute arbitrary code on vulnerable installations of EMC Networker. Authentication is not required to exploit this vulnerability. The specific flaws exist in the Networker Remote Exec Service, nsrexecd.exe. The location of this service is available by querying the SUNRPC portmapper on TCP port 111 for service #0x5f3e1, version 1. When supplying a long invalid subcmd to a poll or a kill request, an exploitable stack overflow vulnerability can occur within a call to sprintf().

## Additional Details

EMC has issued updates to correct this vulnerability. More details can be found in knowledge base article esg83899 available from powerlink.emc.com . EMC customers can further contact EMC Software Technical Support at 1-877-534-2867.

## Disclosure Timeline

- 2007-02-23 - Vulnerability reported to vendor
- 2007-08-20 - Coordinated public release of advisory
