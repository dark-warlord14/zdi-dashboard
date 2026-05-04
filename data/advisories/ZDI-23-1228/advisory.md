# ZDI-23-1228: Samba Spotlight mdssvc RPC Request Type Confusion Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-1228
- **ZDI-CAN:** ZDI-CAN-20228
- **Date:** 2023-08-25
- **CVE:** CVE-2023-34966
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:N/A:L
- **Affected Vendors:** Samba
- **Affected Products:** Samba
- **Credit:** Florent Saudel, Arnaud Gatignol (@thalium_team)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-1228/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Samba. Authentication is not required to exploit this vulnerability. The specific flaw exists within the parsing of Spotlight RPC arguments. The issue results from the lack of proper validation of user-supplied data, which can result in a type confusion condition. An attacker can leverage this in conjunction with other vulnerabilities to execute arbitrary code in the context of the service account.

## Additional Details

Samba has issued an update to correct this vulnerability. More details can be found at: https://www.samba.org/samba/security/CVE-2023-34966.html

## Disclosure Timeline

- 2023-03-22 - Vulnerability reported to vendor
- 2023-08-25 - Coordinated public release of advisory
