# ZDI-12-175: (0Day) HP SiteScope SOAP Call create Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-175
- **ZDI-CAN:** ZDI-CAN-1463
- **Date:** 2012-08-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** SiteScope
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-175/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP SiteScope. Authentication is not required to exploit this vulnerability. The specific flaw exists because HP SiteScope allows unauthenticated SOAP calls to be made to the SiteScope service. One of those calls is create() which allows unauthenticated user to create a new user account for the service. This account has access to an DownloadFilesHandler which contains a flaw that allows you to download any file from the server inclusing the server configuration files that contains the admin credentials. This can lead to remote code execution under the context of the current process.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigation: Given the stated purpose of SiteScope, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the HP SiteScope service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
