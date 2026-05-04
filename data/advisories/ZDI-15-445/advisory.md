# ZDI-15-445: (0Day) Avira Management Console Update Manager Service HTTP Header Use-After-Free Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-445
- **ZDI-CAN:** ZDI-CAN-3118
- **Date:** 2015-09-16
- **CVE:** CVE-2015-7303
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Avira
- **Affected Products:** Management Console
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-445/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Avira Management Console. Authentication is not required to exploit this vulnerability. The specific flaw exists within the handling of HTTP headers by the Update Manager service. By sending overly large headers, an attacker is able to cause memory to be reused after it has been released. An attacker could leverage this to execute arbitrary code under the context of SYSTEM.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI vulnerability disclosure policy on lack of vendor response. 09/03/2015 - ZDI emailed Avira contact and requested contact 09/13/2015 - ZDI emailed Avira security@, secure@, support@ and requested contact 09/13/2015 - Avira replied that the product is nearing EOL and would not be patched 09/14/2015 - ZDI notified the vendor of intent to publish as 0-day -- Mitigation: Given the nature of the vulnerability, the only salient mitigation strategy is to restrict interaction with the service to trusted machines. Only the clients and servers that have a legitimate procedural relationship with the service should be permitted to communicate with it. This could be accomplished in a number of ways, most notably with firewall rules/whitelisting. These features are available in the native Windows Firewall, as described in http://technet.microsoft.com/en-us/library/cc725770%28WS.10%29.aspx and numerous other Microsoft Knowledge Base articles. -- Vendor Patch: http://www.avira.com/en/support-for-home-knowledgebase-detail/kbid/1787

## Disclosure Timeline

- 2015-05-19 - Vulnerability reported to vendor
- 2015-09-16 - Coordinated public release of advisory
