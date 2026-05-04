# ZDI-24-1369: Zimbra GraphQL Cross-Site Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-24-1369
- **ZDI-CAN:** ZDI-CAN-23939
- **Date:** 2024-10-11
- **CVE:** CVE-2024-9665
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N
- **Affected Vendors:** Zimbra
- **Affected Products:** Zimbra
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-24-1369/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Zimbra. User interaction is required to exploit this vulnerability in that the target must open a malicious email message. The specific flaw exists within the implementation of the graphql endpoint. The issue results from the lack of proper protections against cross-site request forgery (CSRF) attacks. An attacker can leverage this vulnerability to disclose information in the context of the target email account.

## Additional Details

Zimbra has issued an update to correct this vulnerability. More details can be found at: https://blog.zimbra.com/2024/10/new-patch-release-reminders-for-missing-attachments-out-of-office-notifications-traffic-light-protocol-tlp-and-mailto-links/

## Disclosure Timeline

- 2024-06-05 - Vulnerability reported to vendor
- 2024-10-11 - Coordinated public release of advisory
- 2024-10-11 - Advisory Updated
