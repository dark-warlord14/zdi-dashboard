# ZDI-14-123: (0Day) Borland StarTeam Web Server AttachmentService performCheckoutFile Remote Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-123
- **ZDI-CAN:** ZDI-CAN-1857
- **Date:** 2014-05-05
- **CVE:** N/A
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:N/A:N
- **Affected Vendors:** Borland
- **Affected Products:** StarTeam
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-123/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Borland StarTeam. Authentication is not required to exploit this vulnerability. The specific flaw exists within the AttachmentService servlet in the FILECHECKOUT operation. The performCheckoutFile() function allows for reading and subsequent deletion of an arbitrary file by specifying the file path. A remote attacker can exploit this vulnerability to disclose files from the system.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. Vendor Contact Timeline: June 27, 2013: - Sent email request for contact July 30, 2013: - Sent email request for contact July 31, 2013: - Sent explanation of our request by email August 1, 2013: - Sent request for a PGP key August 2, 2013: - Sent explanation of our request by email August 5, 2013: - Sent request for a PGP key August 14, 2013: - Sent email request for contact February 19, 2014: - Sent email request for contact -- Mitigation: Given the stated purpose of StarTeam, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the Borland StarTeam service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2013-06-27 - Vulnerability reported to vendor
- 2014-05-05 - Coordinated public release of advisory
