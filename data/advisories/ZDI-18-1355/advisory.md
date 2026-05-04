# ZDI-18-1355: Microsoft Exchange Server NTLM Reflection EWS User Impersonation Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-1355
- **ZDI-CAN:** ZDI-CAN-6548
- **Date:** 2018-11-21
- **CVE:** CVE-2018-8581
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N
- **Affected Vendors:** Microsoft
- **Affected Products:** Exchange
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-1355/
## Vulnerability Details

This vulnerability allows remote attackers to impersonate arbitrary users on vulnerable installations of Microsoft Exchange Server. Authentication is required to exploit this vulnerability. The specific flaw exists within the use of NTLM authentication in Exchange Server. NTLM responses produced by the server can be reflected back to the server to authenticate arbitrary EWS requests. An attacker can leverage this vulnerability to disclose and modify the data of any user of the Exchange server.

## Additional Details

Microsoft has issued an update to correct this vulnerability. More details can be found at: https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2018-8581

## Disclosure Timeline

- 2018-06-29 - Vulnerability reported to vendor
- 2018-11-21 - Coordinated public release of advisory
