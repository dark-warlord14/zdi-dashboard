# ZDI-11-094: (0 day) Hewlett-Packard StorageWorks File Migration Agent Remote Archive Tampering Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-094
- **ZDI-CAN:** ZDI-CAN-850
- **Date:** 2011-02-28
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** StorageWorks
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-094/
## Vulnerability Details

This vulnerability allows remote attackers to compromise the archive records on vulnerable installations of HP StorageWorks File Migration Agent. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HsmCfgSvc.exe service responsible for managing archive stores. The archive manager is susceptible to tampering due to a failure to enforce authentication from remote users. An attacker could exploit this flaw to compromise the server managing the archives and arbitrarily modify the archive data store under the context of the File Migration Agent software.

## Additional Details

The overall design of the File Migration Agent (FMA) assumes it runs as an application on a Windows server. Given the stated purpose of FMA, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the HP StorageWorks File Migration Agent should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2011-02-28 - Coordinated public release of advisory
