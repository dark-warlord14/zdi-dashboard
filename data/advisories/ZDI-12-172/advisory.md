# ZDI-12-172: (0Day) HP Operations Orchestration RSScheduler Service JDBC Connector Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-172
- **ZDI-CAN:** ZDI-CAN-1456
- **Date:** 2012-08-29
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Operations Orchestra
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-172/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Operations Orchestration. Authentication is not required to exploit this vulnerability. The specific flaw exists within the RSScheduler service JDBC component of Operations Orchestra which listens by default on TCP port 9001. The component is vulnerable to SQL injection attacks. Remote, unauthenticated attackers can exploit this vulnerability by injecting malicious SQL into the target, which could ultimately lead to arbitrary code execution under the context of the SYSTEM user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigation: The overall design of Operations Orchestra assumes it runs as an application on a Windows server. Given the stated purpose of Operations Orchestra, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the HP Operations Orchestra service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2011-12-19 - Vulnerability reported to vendor
- 2012-08-29 - Coordinated public release of advisory
