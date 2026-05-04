# ZDI-14-165: (0Day) Rocket Servergraph Admin Center for TSM fileRequestorServlet del Command Denial of Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-165
- **ZDI-CAN:** ZDI-CAN-2248
- **Date:** 2014-06-02
- **CVE:** CVE-2014-3914
- **CVSS:** 7.8
- **CVSS Vector:** AV:N/AC:L/Au:N/C:N/I:N/A:C
- **Affected Vendors:** Rocket Software
- **Affected Products:** Rocket Servergraph
- **Credit:** Andrea Micalizzi (rgod)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-165/
## Vulnerability Details

This vulnerability allows remote attackers to delete arbitrary files on vulnerable installations of Rocket Servergraph Admin Center for Tivoli Storage Manager. Authentication is not required to exploit this vulnerability. The specific flaw exists within the fileRequestServlet servlet. This servlet is vulnerable to a directory traversal which allows for the deletion of arbitrary files when processing del commands. A remote attacker can leverage this vulnerability to cause a denial-of-service condition.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. Vendor Contact Timeline: 04/16/2014 - ZDI emailed the vendor's support requesting contact 04/16/2014 - Automated reply from vendor 05/12/2014 - ZDI emailed the vendor's support requesting contact 05/12/2014 - Automated reply from vendor 05/05/2014 - ZDI telephoned vendor's support line and were told we would receive a callback (no callback) 05/19/2014 - ZDI emailed the vendor's support requesting contact 05/19/2014 - Automated reply from vendor 05/21/2014 - ZDI emailed the vendor's support requesting contact and indicated final attempt/intent to move toward 0-day 06/02/2014 - Public release of advisory -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2014-04-16 - Vulnerability reported to vendor
- 2014-06-02 - Coordinated public release of advisory
