# ZDI-12-127: (0Day) HP StorageWorks File Migration Agent RsaFTP.dll Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-127
- **ZDI-CAN:** ZDI-CAN-1190
- **Date:** 2012-07-18
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** StorageWorks
- **Credit:** AbdulAziz Hariri
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-127/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP StorageWorks File Migration Agent. Authentication is not required to exploit this vulnerability. The specific flaw exists within the HsmCfgSvc.exe service which listens by default on TCP port 9111. When processing FTP archives the process does not properly validate the size of the root path specified and proceeds to copy the string into a fixed-length buffer on the stack. This can be exploited to execute arbitrary remote code under the context of the running service.

## Additional Details

The overall design of the File Migration Agent (FMA) assumes it runs as an application on a Windows server. Given the stated purpose of FMA, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the HP StorageWorks File Migration Agent should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2011-04-11 - Vulnerability reported to vendor
- 2012-07-18 - Coordinated public release of advisory
