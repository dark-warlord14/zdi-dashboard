# ZDI-15-155: (0Day) Realtek SDK miniigd AddPortMapping SOAP Action Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-155
- **ZDI-CAN:** ZDI-CAN-2435
- **Date:** 2015-04-24
- **CVE:** CVE-2014-8361
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Realtek
- **Affected Products:** rtl81xx SDK
- **Credit:** Ricky "HeadlessZeke" Lawshae
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-155/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Realtek SDK. Authentication is not required to exploit this vulnerability. The specific flaw exists within the miniigd SOAP service. The issue lies in the handling of the NewInternalClient requests due to a failure to sanitize user data before executing a system call. An attacker could leverage this vulnerability to execute code with root privileges.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. Vendor Contact Timeline: 08/13/2014 - ZDI wrote to vendor requesting contact and PGP 09/04/2014 - ZDI wrote to vendor requesting contact and PGP 09/29/2014 - ZDI wrote to vendor requesting contact and PGP 10/22/2014 - ZDI wrote to vendor requesting contact and PGP, indicated "final" email attempt and informed of intent to 0-day 04/24/2015 - Public release of advisory -- Mitigation: Given the stated purpose of Realtek SDK, and the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with products using Realtek SDK service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles.

## Disclosure Timeline

- 2014-08-13 - Vulnerability reported to vendor
- 2015-04-24 - Coordinated public release of advisory
